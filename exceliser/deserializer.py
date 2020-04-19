import inspect
import json

from typing import Any
from openpyxl.workbook import Workbook
from openpyxl.worksheet._write_only import WriteOnlyWorksheet
from openpyxl.cell import WriteOnlyCell
from openpyxl.styles import Font, Alignment, Border, Side, Color


# TODO: Implement font colors, comments and cell fills.


class WorbookDeserializer:

    __slots__ = {"_json_file", "_json_decoder", "_workbook", "_output_name"}

    def __init__(self, path: str, output_name: str, json_decoder=None):
        """
        :param path: Path to JSON file.
        :param output_name: Name for output excel file.
        :param json_encoder: JSON encoder (defaults to python builtin json lib)
        """
        # value shared between functions; endproduct of deserialization
        self._workbook = Workbook(
            write_only=True)
        self._json_decoder = json_decoder or json
        self._json_file = self._read_json_file(path, self._json_decoder)
        self._output_name = output_name

    def deserialize(self, path: str = None, output_name: str = None, json_decoder=None):
        """ Deserializes given json file to excel file """
        if path:
            decoder = json_decoder or self._json_encoder
            self._json_file = self._read_json_file(path, decoder)

        if output_name:
            self._output_name = output_name

        for sheet in self._json_file.get('worksheets'):
            self._deserialize_sheet(sheet)

        self._workbook.save(self._output_name)

    def _deserialize_sheet(self, data: dict) -> None:
        worksheet = self._workbook.create_sheet(title=data.get('title'))
        for row in data.get('rows'):
            row_data = []
            for col_idx, cell_data in enumerate(row.get('cells')):
                # because the WriteOnlySheet does not support
                # adding cell, rather appening whole rows it is
                # neccessary to append None values to row in order
                # to preserve cell column index
                cell_col_idx = cell_data.get('column')
                if col_idx + 1 != cell_col_idx:
                    row_data.extend([None] * (cell_col_idx - (col_idx + 1)))

                cell = self._create_cell(worksheet, cell_data)
                row_data.append(cell)

            worksheet.append(row_data)

    def _create_cell(self, worksheet: WriteOnlyWorksheet, data: dict) -> WriteOnlyCell:
        cell = WriteOnlyCell(ws=worksheet, value=data.get('value'))
        cell.column = data.get('column')
        cell.row = data.get('row')

        cell.font = self._create_cell_font(data.get('font'))
        cell.alignment = self._dict_to_object(data.get('alignment'), Alignment)
        cell.border = self._create_cell_borders(data.get('border'))
        return cell

    def _create_cell_font(self, data: dict) -> Font:
        # create color object from color dict first
        if 'color' in data:
            data['color'] = self._create_color(data['color'])
        return self._dict_to_object(data, Font)

    def _create_cell_borders(self, data: dict) -> Border:
        """
        Creates sides from cell dictionary and combines them into Border object.
        :param data: Dictionary holding cell borders data.
        :return: Border object holding styles for cell side borders.
        """
        border_data = {}
        for side in inspect.getfullargspec(Border.__init__).args:
            side_data = data.get(side)
            if isinstance(side_data, dict):
                if 'color' in side_data:
                    color_data = side_data.pop('color')
                    if isinstance(color_data, dict):
                        side_data['color'] = self._create_color(color_data)
                border_data[side] = self._dict_to_object(side_data, Side)
        return self._dict_to_object(border_data, Border)

    def _create_color(self, color_data: dict) -> Color:
        # TODO: Implement colors for font
        if isinstance(color_data['index'], str):
            color_data['index'] = int(color_data['index'], base=16)
        color_data['index'] = 16777215
        return self._dict_to_object(color_data, Color)

    @staticmethod
    def _dict_to_object(data: dict, _object: Any) -> object:
        """ Initializes given object from dictionary """
        return _object(**{arg: value for arg, value in data.items()
                          if arg in inspect.getfullargspec(_object.__init__).args})

    @staticmethod
    def _read_json_file(path: str, json_decoder):
        with open(path, 'r') as file:
            return json_decoder.loads(file.read())

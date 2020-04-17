import orjson

from openpyxl.workbook import Workbook
from openpyxl.worksheet._write_only import WriteOnlyWorksheet
from openpyxl.cell import WriteOnlyCell


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
        self._json_decoder = json_decoder or orjson
        self._json_file = self._read_json_file(path, self._json_decoder)
        self._output_name = output_name

    def deserialize(self, path: str = None, output_name: str = None, json_decoder=None):
        """ Deserializes given json file to excel file """
        if path:
            decoder = json_decoder or self._json_encoder
            self._json_file = self._read_json_file(path, decoder)

        for sheet in self._json_file.get('worksheets'):
            self._deserialize_sheet(sheet)

        self._workbook.save(self._output_name)

    def _deserialize_sheet(self, data: dict) -> None:
        worksheet = self._workbook.create_sheet(title=data.get('title'))
        for row in data.get('rows'):
            row_data = list()
            for col_idx, cell_data in enumerate(row.get('cells')):
                # because the WriteOnlySheet does not support
                # adding cell, rather appening whole rows it is
                # neccessary to append None values to row in order
                # to preserve cell column index
                cell_col_idx = cell_data.get('column')
                print(col_idx, cell_col_idx)
                if col_idx + 1 != cell_col_idx:
                    row_data.extend([None] * (cell_col_idx - (col_idx + 1)))

                cell = self._create_cell(worksheet, cell_data)
                row_data.append(cell)

            worksheet.append(row_data)

    @staticmethod
    def _create_cell(worksheet: WriteOnlyWorksheet, data: dict) -> WriteOnlyCell:
        cell = WriteOnlyCell(ws=worksheet, value=data.get('value'))
        cell.column = data.get('column')
        cell.row = data.get('row')
        return cell

    @staticmethod
    def _read_json_file(path: str, json_decoder):
        with open(path, 'r') as file:
            return json_decoder.loads(file.read())

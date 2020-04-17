import json
import collections
from typing import Any
import openpyxl

from openpyxl.worksheet.worksheet import Worksheet
from openpyxl.cell.cell import Cell

IGNORED_ATTRS = ["copy", "parent"]


class WorkbookSerializer:

    __slots__ = {"workbook", "json_encoder"}

    def __init__(self, path: str, json_encoder=None) -> None:
        self.workbook = self._read_workbook(path)
        self.json_encoder = json_encoder or json

    def serialize(self):
        """Serializes Excel worbook (file) to json format."""
        return dict(
            worksheets=[
                self._serialize_sheet(worksheet)
                for worksheet in self.workbook.worksheets
            ]
        )

    def _serialize_sheet(self, worksheet: Worksheet) -> dict:
        return dict(
            title=worksheet.title,
            columns=[self._serialize_column(
                col, idx) for idx, col in enumerate(worksheet.columns)],
        )

    def _serialize_column(self, column: tuple, column_index: int) -> dict:
        return dict(index=column_index + 1,
                    cells=[self._serialize_cell(cell) for cell in column if cell.value])

    def _serialize_cell(self, cell: Cell) -> dict:
        return self._object_to_dict(cell)

    def _object_to_dict(self, _object: Any) -> dict:
        return {name: self._get_object_attribute(_object, name)
                for name in dir(_object) if not name.startswith("_")
                and not self._attr_is_callable(_object, name)
                and name not in IGNORED_ATTRS}

    def _get_object_attribute(self, _object, name):
        attr_value = getattr(_object, name)
        if self._value_is_builtin_type(attr_value):
            return attr_value
        return self._object_to_dict(attr_value)

    @staticmethod
    def _value_is_builtin_type(value: Any) -> bool:
        return value.__class__.__module__ == "builtins"

    @staticmethod
    def _attr_is_callable(_object: Any, attr: str) -> bool:
        try:
            return isinstance(getattr(_object, attr), collections.Callable)
        except NotImplementedError:
            return True

    @staticmethod
    def _read_workbook(path: str, formatting_info: bool = True):
        """
        Reads excel file into memory.

        By default formatting info is True, which does 
        take more memory but provides additional info about workbook.
        """
        return openpyxl.open(filename=path)

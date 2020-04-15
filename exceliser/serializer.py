import json
import xlrd


class WorkbookSerializer:

    __slots__ = {"worbook", "json_encoder"}

    def __init__(self, path: str, json_encoder=None) -> None:
        self.workbook = self._read_workbook(path)
        self.json_encoder = json_encoder or json

    def serialize(self):
        pass

    def _read_workbook(self, path: str, formatting_info: bool = True):
        """
        Reads excel file into memory.

        By default formatting info is True, which does 
        take more memory but provides additional info about workbook.
        """
        return xlrd.open_worbook(path, formatting_info=formatting_info)

import json
from . import WorkbookSerializer
from . import WorbookDeserializer

"""
    Main API for serializing and deserializing 
    Excel documents
"""


def serialize(path: str):
    return WorkbookSerializer(path).serialize()


def deserialize(path: str, output_name: str, json_decoder=None):
    return WorbookDeserializer(path, output_name, json_decoder).deserialize()

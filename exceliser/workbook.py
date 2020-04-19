import json
from . import WorkbookSerializer
from . import WorbookDeserializer

"""
    Main API for serializing and deserializing 
    Excel documents
"""


def serialize(path: str):
    return WorkbookSerializer(path).serialize()


def deserialize(path: str, json_decoder=None):
    return WorbookDeserializer(path, json_decoder).deserialize()

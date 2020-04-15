import json
from .serializer import WorkbookSerializer

"""
    Main API for serializing and deserializing 
    Excel documents
"""


def serialize(path: str, json_encoder=None):
    serializer = WorkbookSerializer(path, json_encoder)
    return serializer.serialize()


def deserialize(path: str, json_decoder=None):
    pass

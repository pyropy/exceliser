import json
from .serializer import WorkbookSerializer
from .deserializer import WorbookDeserializer

"""
    Main API for serializing and deserializing 
    Excel documents
"""


def serialize(path: str, json_encoder=None):
    serializer = WorkbookSerializer(path, json_encoder)
    return serializer.serialize()


def deserialize(path: str, output_name: str, json_decoder=None):
    deserializer = WorbookDeserializer(path, output_name, json_decoder)
    return deserializer.deserialize()

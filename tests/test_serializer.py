from exceliser import WorkbookSerializer


def test_serialize_workbook(serializer_workbook_path):
    """ Tests if any errors will occure during serialization of worbook """
    serialized_workbook = WorkbookSerializer(
        serializer_workbook_path).serialize()

    assert serialized_workbook
    assert type(serialized_workbook) == dict
    assert 'properties' in serialized_workbook
    assert 'worksheets' in serialized_workbook

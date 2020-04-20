from exceliser import WorkbookSerializer


def test_serialize_workbook(serializer_workbook_path):
    """ Tests if any errors will occure during serialization of worbook """
    serialized_workbook = WorkbookSerializer(
        serializer_workbook_path).serialize()

    assert serialized_workbook
    assert type(serialized_workbook) == dict
    assert 'properties' in serialized_workbook
    assert 'worksheets' in serialized_workbook
    assert len(serialized_workbook['worksheets']
               ) == 2, "There should be two worksheets in given workbook."

    first_worksheet = serialized_workbook['worksheets'][0]
    assert type(first_worksheet) == dict
    assert 'rows' in first_worksheet
    assert len(first_worksheet['rows']) == 1

    first_row = first_worksheet['rows'][0]

    assert type(first_row) == dict
    assert 'cells' in first_row
    assert len(
        first_row['cells']) == 2, "There should be only two cells in first row of first worksheet."

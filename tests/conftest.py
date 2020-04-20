import pytest


@pytest.fixture
def serializer_workbook_path() -> str:
    """
    Path to excel workbook used by serializer tests.
    """
    return 'tests/data/serializer/test.xlsx'

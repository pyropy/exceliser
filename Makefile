help:
	@echo "Tests\n"
	@echo "make test_serializer - Run tests for serializer"
	@echo "make test_workbook   - Run tests for workbook"

test:
	@pytest tests/

test_serializer:
	@pytest tests/test_serializer.py
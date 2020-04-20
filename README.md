# Excel JSON

> NOTE: This is still WIP so bugs might occure.

## Description

**Exceliser** is a tool for helping you **serialize** your excel documents to json or **deserialize** json back to excel document.

## Installation

To install this package simply run following command in your terminal:

```bash
pip install exceliser
```

## Examples

### Serialization

```python
from exceliser.workbook import serialize

# serialize data to dict
data = serialize(path="/path/to/myworkbook.xlsx")
```

### Deserialization

```python
from exceliser.workbook import deserialize

# deserialize data from dict to worbook
workbook = deserialize(path="/path/to/mydata.json")

# save deserialized worbook as excel file
worbook.save('myworbook.xlsx')
```

## Development

### Running tests

To run all tests simply run following `make` command in your terminal:

```bash
make test
```

To see rest of the commands, including ones for running tests type following in the terminal:

```bash
make help
```

## Motivation

Serialization of excel documents to json makes them suitable for storing to database and deserialized when needed rather then keeping them as files.

## Contributors

* None, but you can be the first one.

## Author

* Srdjan Stankovic
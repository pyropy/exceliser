import click
import json
from exceliser.workbook import serialize as _serialize
from exceliser.workbook import deserialize as _deserialize


@click.command()
@click.option("--file", help="Filepath for your file", required=True, type=str)
@click.option("--output-name", help="Name of your output file", required=True, type=str)
@click.option("--serialize/--deserialize", default=True)
def main(file, serialize, output_name):
    """ Serializes/deserializes your documents """
    if serialize:
        result = _serialize(file)
        output_name = output_name.replace(".json", "")
        json.dump(result, open("{}.json".format(output_name), "w"))
    else:
        # TODO: Implement deserialization
        _deserialize(file, json)


if __name__ == "__main__":
    main()

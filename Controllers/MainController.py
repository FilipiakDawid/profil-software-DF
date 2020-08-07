from Models.AddJSON import AddJSON
import ReadJsonFile
import argparse

parser = argparse.ArgumentParser(description='Controller ')
parser.add_argument('--installfromFile', help="Insert Values to DataBase from JSON file", action='store_true')
args = parser.parse_args()


def add_json_file():
    file = ReadJsonFile.readfile("persons.json")
    json_model = AddJSON()
    json_model.add_to_base_json(file)



if args.installfromFile:
    add_json_file()
else:
    print(parser.print_help())

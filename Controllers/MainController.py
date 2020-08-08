from Models.AddJSON import AddJSON
import ReadJsonFile
import argparse

parser = argparse.ArgumentParser(description='Main Controller')
parser.add_argument('--insertdata', help="Insert Values to DataBase from JSON file", choices=['API', 'Local'])
args = parser.parse_args()


def add_json_file(choice):
    if choice == 'Local':
        file = ReadJsonFile.read_file_local("persons.json")
    else:
        file = ReadJsonFile.read_file_from_api("https://randomuser.me/api/", '25')

    if file is not None:
        json_model = AddJSON()
        json_model.add_to_base_json(file)
        print("Successfully added to the base")
    else:
        print("Problem with reading the file from: " + choice)


try:
    if args.insertdata:
        add_json_file(args.insertdata)
    else:
        print(parser.print_help())
except BaseException as err:
    print(err)


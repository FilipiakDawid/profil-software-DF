from Models.AddJSON import AddJSON
import ReadJsonFile


class MainController:

    def add_json_file(self):
        file = ReadJsonFile.readfile("../persons.json")
        json_model = AddJSON()
        json_model.add_to_base_json(file)

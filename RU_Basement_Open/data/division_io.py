import json
from models.division_mdl import DivisionMdl
from data.functions import  *

class DivisionIO:
    def __init__(self, division_filename = "RU_Basement_Open/file/division.json") -> None:
        self.division_filename = division_filename

    def get_divisions_from_file(self):
        '''returns data of divisions from json file as a list of objects'''

        self.data = load_file_data(self.division_filename)

        divisions = []

        for i in self.data["division_details"]:
            division = DivisionMdl(i["id"], i["name"], i["team_ids"], i["host_name"], i["phone_nr"], i["start_date"], i["end_date"], i["type"], i["rounds"], i["matches"])
            divisions.append(division)

        return divisions
    def write_division_person_to_file(self, divisions:list):
        '''takes in updated list of division objects converts it to a list of dicts, 
        and writes it to the json file'''

        new_divisions = []
        for x in divisions:
            new_divisions.append(to_dict(x))
        division_details = {"division_details": new_divisions}
        division_details_json = json.dumps(division_details, indent=4)
        write_file_data(self.division_filename, division_details_json)
    
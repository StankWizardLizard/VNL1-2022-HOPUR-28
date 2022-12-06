import json
from models.division_mdl import DivisionMdl
from data.functions import *


class DivisionIO:
    def __init__(self, directory="files", filename="division.json") -> None:
        self.division_filename = f"{directory}/{filename}"

    def get_divisions_from_file(self):
        '''returns data of divisions from json file as a list of objects'''

        self.data = load_file_data(self.division_filename)

        divisions = []
        try:
            for i in self.data["division_details"]:
                division = DivisionMdl(id=i["id"], name=i["name"], team_ids=i["team_ids"], host_name=i["host_name"], phone_nr=i["phone_nr"],
                                    start_date=i["start_date"], end_date=i["end_date"], type=i["type"], rounds=i["rounds"], matches=i["matches"])
                divisions.append(division)
        except KeyError:
            pass
        
        return divisions

    def write_division_person_to_file(self, divisions: list):
        '''takes in updated list of division objects converts it to a list of dicts, 
        and writes it to the json file'''

        new_divisions = []
        for x in divisions:
            new_divisions.append(to_dict(x))
        division_details = {"division_details": new_divisions}
        division_details_json = json.dumps(
            division_details, indent=4, ensure_ascii=False)
        write_file_data(self.division_filename, division_details_json)

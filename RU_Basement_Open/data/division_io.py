import json
from models.division_mdl import DivisionMdl
from data.functions import  *

class DivisionIO:
    def __init__(self, division_filename = "RU_Basement_Open/file/division.json") -> None:
        self.division_filename = division_filename
        self.data = load_file_data(self.division_filename)

    def get_division_from_file(self):
        pass
    def write_division_person_to_file(self):
        pass
    
import json
from models.team_mdl import TeamMdl
from data.functions import  *

class TeamIO:
    def __init__(self, team_filename = "RU_Basement_Open/file/division.json") -> None:
        self.team_filename = team_filename
        self.data = load_file_data(self.team_filename)
    def get_team_from_file(self):
        pass
    def write_team_person_to_file(self):
        pass
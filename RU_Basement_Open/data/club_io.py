import json
from models.club_mdl import ClubMdl
from data.functions import  *

class ClubIO:
    def __init__(self, club_filename = "RU_Basement_Open/file/club.json") -> None:
        self.club_filename = club_filename
        self.data = load_file_data(self.club_filename)

    def get_club_from_file(self):
        pass
    def write_club_person_to_file(self):
        pass
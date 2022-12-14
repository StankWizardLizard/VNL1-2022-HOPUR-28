import json
from models.club_mdl import ClubMdl
from data.functions import *


class ClubIO:
    """ Handles reading and writing club data from storage files"""
    def __init__(self, directory="files", filename="club.json") -> None:
        self.club_filename = f"{directory}/{filename}"

    def get_clubs_from_file(self):
        '''returns data of clubs from json file as a list of objects'''

        self.data = load_file_data(self.club_filename)

        clubs = []
        try:
            for i in self.data["club_details"]:
                club = ClubMdl(
                    name=i["name"], address=i["address"], phone_nr=i["phone"],
                    id=i["id"], teams_id=i["teams_id"])

                clubs.append(club)
        except KeyError:
            pass
        
        return clubs

    def write_club_person_to_file(self, clubs: list):
        '''takes in updated list of club objects converts it to a list of dicts, 
        and writes it to the json file'''

        new_clubs = []
        for x in clubs:
            new_clubs.append(to_dict(x))
        club_details = {"club_details": new_clubs}
        club_details_json = json.dumps(
            club_details, indent=4, ensure_ascii=False)
        write_file_data(self.club_filename, club_details_json)

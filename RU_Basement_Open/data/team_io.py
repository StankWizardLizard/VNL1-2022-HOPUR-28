import json
from models.team_mdl import TeamMdl
from data.functions import *


class TeamIO:
    def __init__(self, directory="files", filename="team.json") -> None:
        self.team_filename = f"{directory}/{filename}"

    def get_teams_from_file(self):
        '''returns data of teams from json file as a list of objects'''

        self.data = load_file_data(self.team_filename)

        teams = []

        for i in self.data["team_details"]:
            team = TeamMdl(name=i["name"], player_ids=i["player_ids"],
                           captain_id=i["captain_id"], id=i["id"])
            teams.append(team)

        return teams

    def write_team_person_to_file(self, teams: list):
        '''takes in updated list of team objects converts it to a list of dicts, 
        and writes it to the json file'''

        new_teams = []
        for x in teams:
            new_teams.append(to_dict(x))
        team_details = {"team_details": new_teams}
        team_details_json = json.dumps(
            team_details, indent=4, ensure_ascii=False)
        write_file_data(self.team_filename, team_details_json)

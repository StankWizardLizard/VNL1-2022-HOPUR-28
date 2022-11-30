import json
from models.match_mdl import MatchMdl
from data.functions import  *

class MatchIO:
    def __init__(self, match_filename = "file/match.json"):
        self.match_filename = match_filename
    def get_matches_from_file(self):
        '''returns data of matches from json file as a list of objects'''

        self.data = load_file_data(self.match_filename)

        matches = []

        for i in self.data["match_details"]:
            match = MatchMdl(i["date"], i["home_team"], i["away_team"], i["home_team_players"], i["away_team_players"], i["division_id"], i["results"], i["quality_points"], i["id"] )
            matches.append(match)

        return matches
    def write_match_to_file(self, matches:list):
        '''takes in updated list of match objects, converts it to a list of dicts, 
        and writes it to the json file'''

        new_matches = []
        for x in matches:
            new_matches.append(to_dict(x))
        match_details = {"match_details": new_matches}
        matches_details_json = json.dumps(match_details, indent=4, ensure_ascii=False)
        write_file_data(self.match_filename, matches_details_json)
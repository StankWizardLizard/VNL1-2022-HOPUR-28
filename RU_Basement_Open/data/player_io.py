import json
from models.player_mdl import PlayerMdl
from data.functions import *


class PlayerIO:
    def __init__(self, directory="files", filename="player.json"):
        self.player_filename = f"{directory}/{filename}"

    def get_players_from_file(self):
        '''returns data of players from json file as a list of objects'''

        self.data = load_file_data(self.player_filename)

        players = []
        try:
            for i in self.data["player_details"]:
                player = PlayerMdl(name=i["name"], ssn=i["ssn"], mobile_nr=i["mobile_nr"], home_nr=i["home_nr"],
                                address=i["address"], email=i["email"], id=i["id"], team_id=i["team_id"],club_id=i["club_id"])
                players.append(player)
        except KeyError:
            pass
        
        return players

    def write_player_to_file(self, players: list):
        '''takes in updated list of player objects converts it to a list of dicts, 
        and writes it to the json file'''

        new_players = []
        for x in players:
            new_players.append(to_dict(x))
        player_details = {"player_details": new_players}
        players_details_json = json.dumps(
            player_details, indent=4, ensure_ascii=False)
        write_file_data(self.player_filename, players_details_json)

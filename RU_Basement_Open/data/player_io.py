import json
from models.player_mdl import PlayerMdl
from data.functions import  *

class PlayerIO:
    def __init__(self, player_filename = "file/player.json"):
        self.player_filename = player_filename

    def get_players_from_file(self):
        '''returns data of players from json file as a list of objects'''

        self.data = load_file_data(self.player_filename)

        players = []

        for i in self.data["player_details"]:
            player = PlayerMdl(i["name"], i["ssn"], i["mobile_nr"], i["home_nr"], i["address"], i["email"], i["id"], i["team_id"] )
            players.append(player)

        return players

    def write_player_to_file(self, players:list):
        '''takes in updated list of player objects converts it to a list of dicts, 
        and writes it to the json file'''

        new_players = []
        for x in players:
            new_players.append(to_dict(x))
        player_details = {"player_details": new_players}
        players_details_json = json.dumps(player_details, indent=4, ensure_ascii=False)
        write_file_data(self.player_filename, players_details_json)


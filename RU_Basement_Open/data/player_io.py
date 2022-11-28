import json

class PlayerIO:
    def __init__(self, player_filename = "RU_Basement_Open/file/player.json"):
        self.player_filename = player_filename
        self.data = self._load_file_data()

    def _load_file_data(self):
        '''loads the json file data'''

        f = open(self.player_filename, encoding="U")
        data = json.load(f)
        f.close()
        return data

    def get_player_from_file_by_ssn(self, player_ssn):
        '''returns data of player with x ssn number'''
        
        for i in self.data["player_details"]:
            if i["ssn"] == player_ssn:
                return i["name"]
    
    def get_players_from_file(self, player_ssn):
        '''returns data of all players in json file'''
        
        for i in self.data["player_details"]:
            if i["ssn"] == player_ssn:
                return i["name"]

    def write_player_to_file(self):
        pass

test = PlayerIO()
print(test.get_player_from_file(123))

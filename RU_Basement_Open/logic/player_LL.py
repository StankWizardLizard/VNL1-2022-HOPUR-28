from functions.get_random_id import get_random_id


class PlayerLL():
    def __init__(self, data_connection):
        self.data_wrapper = data_connection

    def create_player(self, player):
        """Takes a player object and forwards it to the data layer"""
        player.id = get_random_id()
        self.data_wrapper.write_person_to_file(player)


    def get_player(self, id):
        players = self.data_wrapper.get_person_from_file()
        for player in players:
            if player["id"] == id:
                return player

    def get_all_players(self):
        return self.data_wrapper.get_person_from_file()
    

from functions.get_random_id import get_random_id


class PlayerLL():
    def __init__(self, data_connection):
        self.data_wrapper = data_connection

    def create_player(self, player):
        """Takes a player object and forwards it to the data layer"""
        player.id = get_random_id()
        print("SAVING BEEP BOOP")  # TODO: Connect to IO
        return player #TODO: remove once IO connected

    def get_player(self, id):
        pass
    
    def get_all_players(self):
        pass
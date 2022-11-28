from data.data_wrapper import Data_Wrapper
from logic.player_LL import PlayerLL

class LogicWrapper:
    def __init__(self):
        self.data_wrapper = Data_Wrapper()
        self.player_logic = PlayerLL(self.data_wrapper)
        
    def create_player(self, player):
        # TODO: remove variable once IO connected 
        a = self.player_logic.create_player(player) 
        return a
    
    def get_player(self, id):
        pass
    
    def get_all_players(self):
        pass
    
from data.data_wrapper import Data_Wrapper
from logic.match_LL import MatchLL
from logic.player_LL import PlayerLL

class LogicWrapper:
    def __init__(self):
        self.data_wrapper = Data_Wrapper()
        self.player_logic = PlayerLL(self.data_wrapper)
        self.match_logic = MatchLL(self.data_wrapper)
        # self.division_logic = DivisionLL(self.data_wrapper)
        # self.team_logic = TeamLL(self.data_wrapper)
        # self.club_logic = ClubLL(self.data_wrapper)
        
        
    def create_player(self, player):
        # TODO: remove variable once IO connected 
        a = self.player_logic.create_player(player) 
        return a
    
    def get_player(self, id):
        pass
    
    def get_all_players(self):
        pass
    
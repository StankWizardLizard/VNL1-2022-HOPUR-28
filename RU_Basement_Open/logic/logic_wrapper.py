from data.data_wrapper import Data_Wrapper
from logic.division_LL import DivisionLL
from logic.player_LL import PlayerLL
from logic.match_LL import MatchLL
from logic.club_LL import ClubLL
from logic.team_LL import TeamLL

class LogicWrapper:
    def __init__(self):
        self.data_wrapper = Data_Wrapper()
        self.division_logic = DivisionLL(self.data_wrapper)
        self.player_logic = PlayerLL(self.data_wrapper)
        self.match_logic = MatchLL(self.data_wrapper)
        self.team_logic = TeamLL(self.data_wrapper)
        self.club_logic = ClubLL(self.data_wrapper)
        
    #----- Division methods -----#
    def create_division(self,division):
        self.division_logic.create_division(division)
    def get_leaderboard(self):
        self.division_logic.get_leaderboard()
    def get_division(self, id):
        self.division_logic.get_division(id)
        
    #----- Player methods -----#
    def create_player(self, player):
        self.player_logic.create_player(player)
    def get_player(self, id):
        self.player_logic.get_player(id)
    def get_all_players(self):
        self.player_logic.get_all_players()
    
    #----- Match methods -----#
    def get_all_matches(self):
        self.match_logic.get_all_matches()
    def get_match(self, id):
        self.match_logic.get_match(id)
    def get_upcoming_matches(self):
        self.match_logic.get_upcoming_matches()
    def get_concluded_matches(self):
        self.match_logic.get_concluded_matches()
    def create_match(self, match):
        self.match_logic.create_match()
    def set_date(self, id, new_date):
        self.match_logic.set_date(id, new_date)
    def set_results(self, id, results):
        self.match_logic(id, results)
    
    #----- Team methods -----#
    def get_all_teams(self):
        return self.team_logic.get_all_teams()
    def get_team(self, id):
        return self.team_logic.get_team(id)
    def create_team(self, team):
        return self.team_logic.create_team(team)        

    #----- Club methods -----#
    def get_club(self, id):
        return self.club_logic.get_club(id)
    def get_all_clubs(self):
        return self.club_logic.get_all_clubs()
    def create_club(self, club):
        return self.club_logic.create_club(club)
    
from data.data_wrapper import DataWrapper
from logic.club_LL import ClubLL
from logic.division_LL import DivisionLL
from logic.master_LL import MasterLL
from logic.match_LL import MatchLL
from logic.player_LL import PlayerLL
from logic.team_LL import TeamLL

class LogicWrapper:
    def __init__(self):
        self.data_wrapper = DataWrapper()
        self.player_logic = PlayerLL(self.data_wrapper)
        self.match_logic = MatchLL(self.data_wrapper)
        self.division_logic = DivisionLL(self.data_wrapper)
        self.team_logic = TeamLL(self.data_wrapper)
        self.club_logic = ClubLL(self.data_wrapper)
        
        self.master_logic = MasterLL(self.match_logic, self.division_logic, self.data_wrapper)
        
        
        
    #----- Master methods -----#
    def generate_division_matches(self, team_ids, division_id):
        self.master_logic.generate_division_matches(team_ids, division_id)

    #----- Division methods -----#
    def create_division(self, division):
        return self.division_logic.create_division(division)

    def get_leaderboard(self):
        return self.master_logic.get_leaderboard()

    def get_division(self, id):
        return self.division_logic.get_division(id)

    def get_all_divisions(self):
        return self.division_logic.get_all_divisions()

    def add_team_to_division(self, team_id, division_id):
        return self.division_logic.add_team(team_id, division_id)
    
    def add_matches_to_division(self, match_ids:list, division_id):
        self.division_logic.add_matches(match_ids, division_id)

    def set_division_dates(self, start_date, end_date, division_id):
        self.division_logic.set_dates(start_date, end_date, division_id)
        
    def division_name_exists(self, division_name):
        return self.division_logic.name_exists(division_name)    
        
    #----- Player methods -----#
    def create_player(self, player):
        return self.player_logic.create_player(player)

    def get_player(self, id):
        return self.player_logic.get_player(id)

    def get_all_players(self):
        return self.player_logic.get_all_players()
    
    def player_ssn_exists(self, ssn):
        return self.player_logic.ssn_exists(ssn)

    def get_players_by_club(self,clubs):
        return self.player_logic.get_players_by_club(clubs)
    
    def player_ssn_exists(self, ssn):
        return self.player_logic.ssn_exists(ssn)

    #----- Match methods -----#
    def get_all_matches(self):
        return self.match_logic.get_all_matches()

    def get_match(self, id):
        return self.match_logic.get_match(id)

    def get_upcoming_matches(self):
        return self.match_logic.get_upcoming_matches()

    def get_concluded_matches(self):
        return self.match_logic.get_concluded_matches()

    def create_match(self, match):
        self.match_logic.create_match(match)
    
    def generate_matches(self, team_ids, division_id):
        return self.match_logic.gen_matches(team_ids, division_id)

    def set_match_date(self, id, new_date):
        self.match_logic.set_date(id, new_date)

    def set_match_results(self, id, results):
        self.match_logic.set_results(id, results)

    def get_division_start_and_end_date(self, match_ids):
        return self.match_logic.get_start_and_end_date(match_ids)
        
        
    #----- Team methods -----#
    def get_all_teams(self):
        return self.team_logic.get_all_teams()

    def get_team(self, id):
        return self.team_logic.get_team(id)

    def create_team(self, team):
        return self.team_logic.create_team(team)

    def add_player_to_team(self, player_id, team_id):
        self.team_logic.add_player(player_id, team_id)

    def promote_player(self, player_id, team_id):
        self.team_logic.promote_to_captain(player_id, team_id)

    def get_captain(self, team_id):
        return self.team_logic.get_captain(team_id)
    
    def get_team_id_by_name(self, team_name):
        return self.team_logic.get_id_by_name(team_name)

    #----- Club methods -----#
    def get_club(self, id):
        return self.club_logic.get_club(id)

    def get_all_clubs(self):
        return self.club_logic.get_all_clubs()

    def create_club(self, club):
        return self.club_logic.create_club(club)

    def add_team_to_club(self, team_id, club_id):
        self.club_logic.add_team(team_id, club_id)

    def club_name_exists(self, club_name):
        return self.club_logic.name_exists(club_name)

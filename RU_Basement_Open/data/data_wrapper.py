from data.player_io import PlayerIO
from data.match_io import MatchIO
from data.division_io import DivisionIO
from data.team_io import TeamIO
from data.club_io import ClubIO

class DataWrapper:
    def __init__(self):
        self.player_io = PlayerIO()
        self.match_io = MatchIO()
        self.division_io = DivisionIO()
        self.team_io = TeamIO()
        self.club_io = ClubIO()

    def get_all_players(self):
        return self.player_io.get_players_from_file()
    
    def write_players(self, list_of_players):
        self.player_io.write_player_to_file(list_of_players)
    
    def get_all_matches(self):
        return self.match_io.get_matches_from_file()
    
    def write_matches(self, list_of_matches):
        self.match_io.write_match_to_file(list_of_matches)
    
    def get_all_divisions(self):
        return self.division_io.get_divisions_from_file()

    def write_divisions(self, list_of_divsions):
        self.division_io.write_division_person_to_file(list_of_divsions)

    def get_all_teams(self):
        return self.team_io.get_teams_from_file()

    def write_teams(self, list_of_teams):
        self.team_io.write_team_person_to_file(list_of_teams)

    def get_all_clubs(self):
        return self.club_io.get_clubs_from_file()

    def write_clubs(self, list_of_teams):
        self.club_io.write_club_person_to_file(list_of_teams)

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

    def get_players_from_file(self):
        return self.player_io.get_players_from_file()
    
    def write_player_to_file(self, list_of_players):
        return self.player_io.write_player_to_file(list_of_players)
    
    def get_matches_from_file(self):
        return self.match_io.get_matches_from_file()
    
    def write_match_to_file(self, list_of_matches):
        return self.match_io.write_match_to_file(list_of_matches)
    
    def get_divisions_from_file(self):
        return self.division_io.get_divisions_from_file()

    def write_division_person_to_file(self, list_of_divsions):
        return self.division_io.write_division_person_to_file(list_of_divsions)

    def get_teams_from_file(self):
        return self.team_io.get_teams_from_file()

    def write_team_person_to_file(self, list_of_teams):
        return self.team_io.write_team_person_to_file(list_of_teams)

    def get_clubs_from_file(self):
        return self.club_io.get_clubs_from_file()

    def write_club_person_to_file(self, list_of_teams):
        return self.club_io.write_club_person_to_file(list_of_teams)

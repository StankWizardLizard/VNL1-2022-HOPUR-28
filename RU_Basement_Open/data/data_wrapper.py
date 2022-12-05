from data.player_io import PlayerIO
from data.match_io import MatchIO
from data.division_io import DivisionIO
from data.team_io import TeamIO
from data.club_io import ClubIO

class DataWrapper:
    def __init__(self):
        self.DIRECTORY = "files"
        self.player_io = PlayerIO(directory=self.DIRECTORY)
        self.match_io = MatchIO(directory=self.DIRECTORY)
        self.division_io = DivisionIO(directory=self.DIRECTORY)
        self.team_io = TeamIO(directory=self.DIRECTORY)
        self.club_io = ClubIO(directory=self.DIRECTORY)

    #----- Player methods -----#
    def get_all_players(self):
        return self.player_io.get_players_from_file()
    def write_players(self, list_of_players):
        self.player_io.write_player_to_file(list_of_players)

    #----- Match methods -----#
    def get_all_matches(self):
        return self.match_io.get_matches_from_file()
    def write_matches(self, list_of_matches):
        self.match_io.write_match_to_file(list_of_matches)

    #----- Division methods -----#
    def get_all_divisions(self):
        return self.division_io.get_divisions_from_file()
    def write_divisions(self, list_of_divsions):
        self.division_io.write_division_person_to_file(list_of_divsions)

    #----- Team methods -----#
    def get_all_teams(self):
        return self.team_io.get_teams_from_file()
    def write_teams(self, list_of_teams):
        self.team_io.write_team_person_to_file(list_of_teams)

    #----- Club methods -----#
    def get_all_clubs(self):
        return self.club_io.get_clubs_from_file()
    def write_clubs(self, list_of_teams):
        self.club_io.write_club_person_to_file(list_of_teams)

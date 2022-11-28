from person_io import PersonIO
from match_io import MatchIO
from division_io import DivisionIO
from team_io import TeamIO
from club_io import ClubIO

class DataWrapper:
    def __init__(self):
        self.person_io = PersonIO()
        self.match_io = MatchIO()
        self.division_io = DivisionIO()
        self.team_io = TeamIO()
        self.club_io = ClubIO()

    def get_person_from_file(self):
        return self.person_io.get_person_from_file()
    
    def write_person_to_file(self):
        return self.person_io.write_person_to_file()
    
    def get_match_from_file(self):
        return self.match_io.get_match_from_file()
    
    def write_match_to_file(self):
        return self.match_io.write_match_to_file()
    
    def get_division_from_file(self):
        return self.division_io.get_division_from_file()

    def write_division_person_to_file(self):
        return self.division_io.write_division_person_to_file()

    def get_team_from_file(self):
        return self.team_io.get_team_from_file()

    def write_team_person_to_file(self):
        return self.team_io.write_team_person_to_file()

    def get_club_from_file(self):
        return self.club_io.get_club_from_file()

    def write_club_person_to_file(self):
        return self.club_io.write_club_person_to_file()

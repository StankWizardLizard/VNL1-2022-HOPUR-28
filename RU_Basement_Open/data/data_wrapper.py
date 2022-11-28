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
        

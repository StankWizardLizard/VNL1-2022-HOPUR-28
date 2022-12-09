from functions.get_random_id import get_random_id


class ClubLL():
    """Club logic layer class. Takes input model class from ui layer"""
    def __init__(self, data_connection):
        self.data_wrapper = data_connection
        self.clubs = ""
        self._update_clubs()

    # ----- Internal methods -----#
    def _update_clubs(self):
        """Gets all clubs from data layer"""
        self.clubs = self.data_wrapper.get_all_clubs()

    def _write_clubs(self):
        """Sends club data to data layer to update"""
        self.data_wrapper.write_clubs(self.clubs)

    def _find_club(self, id):
        """ Searches for a club by id. If it exists, return it.
        If not, return False """
        for club in self.clubs:
            if club.id == id:
                return club
        raise IndexError

    # ----- Reading methods -----#

    def get_club(self, id):
        """Returns a club from the data layer by id"""
        self._update_clubs()
        return self._find_club(id)

    def get_all_clubs(self):
        """Returns a list of all clubs from the data layer"""
        self._update_clubs()
        return self.clubs

    def name_exists(self, name):
        """Takes a name. If it exists on a club, return True.
        If not, return False"""
        self._update_clubs()
        for club in self.clubs:
            if club.name == name:
                return True
        return False

    def get_teams(self, club_id):
        """Takes a club id, returns a list of that clubs team ids"""
        return self.get_club(club_id).teams_id

    # ----- Writing methods -----#

    def create_club(self, club):
        """Takes a club object and saves it to the data layer"""
        self._update_clubs()
        club.id = get_random_id()  # add a unique id
        self.clubs.append(club)
        self._write_clubs()
        return club.id

    def add_team(self, team_id, club_id):
        """Take id's for a team and a club, adds that team to the club"""
        self._update_clubs()
        club = self._find_club(club_id)
        club.teams_id.append(team_id)
        self._write_clubs()

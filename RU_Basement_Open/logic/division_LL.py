
from functions.get_random_id import get_random_id


class DivisionLL():

    """Division logic layer class. Takes input model class from ui layer"""

    def __init__(self, data_wrapper):
        """

        :division_mdl: TODO

        """
        self.data_wrapper = data_wrapper
        self.divisions = ""
        self._update_divisions()

    # ----- helper methods -----#
    def _update_divisions(self):
        """Gets all divisions from data layer"""
        self.divisions = self.data_wrapper.get_all_divisions()

    def _write_divisions(self):
        """Sends team data to data layer to update"""
        self.data_wrapper.write_divisions(self.divisions)

    def _find_division(self, id):
        """Searches for a division by id. If it exists, return it.
        If not, return False"
        """
        for division in self.divisions:
            if division.id == id:
                return division
        raise IndexError

    # ----- Reading methods -----#

    def get_division(self, division_id):
        """TODO: Docstring for get_division.
        :returns: TODO

        """
        self._update_divisions()
        return self._find_division(division_id)

    def get_match_ids(self, division_id):
        """Takes a division id and returns a list of keys for it's matches"""
        self._update_divisions()
        return self._find_division(division_id).matches
    
    def get_team_ids(self, division_id):
        """Takes a division id and returns a list of keys for it's teams"""
        self._update_divisions()
        return self._find_division(division_id).team_ids
    
    def name_exists(self, division_name):
        """Takes a name. If it exists on a division, return True.
        If not, return False"""
        self._update_divisions()
        for division in self.divisions:
            if division.name == division_name:
                return True
        return False

    # ----- Writing methods -----#
    def create_division(self, division):
        """
        Creates new devision. Gets division object as input and sends to storage layer
        """
        self._update_divisions()
        division.id = get_random_id()
        self.divisions.append(division)
        self._write_divisions()
        return division.id

    def add_team(self, team_id, division_id):
        """Take id's for a tame and a division.
        Registers that team to the division."""
        self._update_divisions()
        division = self._find_division(division_id)
        division.team_ids.append(team_id)
        self._write_divisions()

    def add_matches(self, match_ids, division_id):
        """ Take a list of match ids and a division id.
        Register those matches to the division"""
        self._update_divisions()
        division = self._find_division(division_id)
        division.matches = match_ids
        self._write_divisions()

    def set_dates(self, start_date, end_date, division_id):
        """Takes a start and end date, and a division id.
        Sets the divison's dates"""
        self._update_divisions()
        division = self._find_division(division_id)
        division.start_date = start_date
        division.end_date = end_date
        self._write_divisions()

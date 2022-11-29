from functions.get_random_id import get_random_id
from models import match_mdl


class MatchLL():
    def __init__(self, data_connection):
        self.data_wrapper = data_connection
        self.matches = ""
        self._update_matches

    #----- Internal methods -----#
    def _update_matches(self):
        """Gets all matches from data layer"""
        self.matches = self.data_wrapper.get_all_matches()

    def _write_matches(self):
        """Sends match data to data layer to update"""
        self.data_wrapper.write_matches(self.matches)

    #----- Reading methods -----#
    def get_all_matches(self):
        """Returns a list of all matches"""
        self._update_matches()
        return self.matches

    def get_match(self, id):
        """Returns a match by id from data layer"""
        self._update_matches
        for match in self.matches:
            if match.id == id:
                return match
        raise IndexError

    def get_upcoming_matches(self):
        """Gets all matches from data layer and returns
        those that have no documented results"""
        self._update_matches()
        ret_list = []
        for match in self.matches:
            if not match.results:
                ret_list.append(match)
        return ret_list

    def get_concluded_matches(self):
        """Gets all matches from data layer and returns
        those that have a documented result"""
        self._update_matches()
        ret_list = []
        for match in self.matches:
            if match.results:
                ret_list.append(match)
        return ret_list

    #----- Writing methods -----#
    def create_match(self, match):
        """Takes a match object and forwards it to the data layer"""
        self._update_matches()
        match.id = get_random_id()
        self.matches.append(match)
        self._write_matches()

    def set_date(self, id, new_date):
        """Sets a matches date and updates data layer"""
        self._update_matches
        for match in self.matches:
            if match.id == id:
                match.date = new_date
                self._write_matches()
                return
        raise IndexError

    def set_results(self, id, results):
        """Sets a matches results and uptades data layer"""
        self._update_matches
        for match in self.matches:
            if match.id == id:
                match.results = results
                self._write_matches()
                return
        raise IndexError

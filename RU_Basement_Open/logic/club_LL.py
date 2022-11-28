from functions.get_random_id import get_random_id

class ClubLL():
    def __init__(self, data_connection):
        self.data_wrapper = data_connection
        self.clubs = ""
        self._update_clubs()
    
    #----- Internal methods -----#
    def _update_clubs(self):
        """Gets all clubs from data layer"""
        self.clubs = self.data_wrapper.get_all_clubs()
    
    def _write_clubs(self):
        """Sends club data to data layer to update"""
        self.data_wrapper.write_matches(self.clubs)
    
    #----- Reading methods -----#
        
    def get_club(self, id):
        """Returns a club from the data layer by id"""
        self._update_clubs()
        for club in self.clubs:
            if club.id == id:
                return club
        raise IndexError

    def get_all_clubs(self):
        """Returns a list of all clubs from the data layer"""
        self._update_clubs()
        return self.clubs
    
    #----- Writing methods -----#    
    def create_club(self, club):
        """Takes a club object and saves it to the data layer"""
        self._update_clubs()
        club.id = get_random_id() # add a unique id
        self.clubs.append(club)
        self._write_clubs()
    
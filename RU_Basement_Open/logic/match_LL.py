from functions.get_random_id import get_random_id

class MatchLL():
    def __init__(self, data_connection):
        self.data_wrapper = data_connection
        
    def create_match(self, match):
        """Takes a match object and forwards it to the data layer"""
        match.id = get_random_id()
        print("SAVING BEEP BOOP")  # TODO: Connect to IO
        return match #TODO: remove once IO connected
    
    def get_all_matches(self):
        """Gets all matches from data layer"""
        # self.data_wrapper.get_all_matches()
        # return matches
        pass
    
    def get_match(self, id):
        """Gets a match my id from data layer"""
        # matches = self.get_all_matches
        # return match where id = match.id ##pseudo
        pass
    
    def get_upcoming_matches(self):
        """Get all matches which have not concluded from data layer"""
        # 
        pass
    
    def get_concluded_matchesself(self):
        pass
    
    def change_date(self):
        pass
    
    def set_results(self): # TODO: Needed?
        pass
    
    def change_results(self):
        pass
    
    
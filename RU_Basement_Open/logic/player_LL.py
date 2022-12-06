from functions.get_random_id import get_random_id


class PlayerLL():
    def __init__(self, data_connection):
        self.data_wrapper = data_connection
        self.players = ""
        self._update_players()
    
    #----- Internal methods -----#
    def _update_players(self):
        """Gets all players from data layer"""
        self.players = self.data_wrapper.get_all_players()
        
    def _write_players(self):
        """Sends player data to data layer to update"""
        self.data_wrapper.write_players(self.players)

    #----- Reading methods -----#
    """Returns a match by id from data layer"""
    def get_player(self, id):
        self._update_players()
        for player in self.players:
            if player.id == id:
                return player
        raise IndexError # If player not found

    def get_all_players(self):
        """Returns a list of all matches"""
        return self.data_wrapper.get_all_players()
    
    def get_players_by_club(self,club):
        """Returns a list of all players by club"""
        all_players = self.get_all_players()
        players_of_club = []
        for player in all_players:
            if club.id == player.club_id:
                players_of_club.append(player)
        return players_of_club

    
    def ssn_exists(self, ssn):
        """Takes an ssn. If it exists on a player, return True.
        If not, return False"""
        self._update_players()
        for player in self.players:
            if player.ssn == ssn: # if ssn
                return True
        return False 

    def ssn_exists(self, ssn):
        """Takes an ssn. If it exists on a player, return True.
        If not, return False"""
        self._update_players()
        for player in self.players:
            if player.ssn == ssn: # if ssn
                return True
        return False 

    #----- Writing methods -----#
    def create_player(self, player):
        """Takes a player object and forwards it to the data layer"""
        self._update_players()
        player.id = get_random_id()
        self.players.append(player)
        self._write_players()
        return player.id
    
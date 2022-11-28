from functions.get_random_id import get_random_id
from models import team_mdl


class TeamLL():
    def __init__(self, data_connection):
        self.data_wrapper = data_connection
        self.teams = ""
        self._update_teams()
        
    #----- Internal methods -----#
    def _update_teams(self):
        """Gets all teams from data layer"""
        self.teams = self.data_wrapper.get_all_teams()
    
    def _write_teams(self):
        """Sends team data to data layer to update"""
        self.data_wrapper.write_matches(self.teams)
    
    #----- Reading methods -----#
    def get_all_teams(self):
        """Returns a list of all teams from the data layer"""
        self._update_teams()
        return self.teams
    
    def get_team(self, id):
        """Returns a team from the data layer by id"""
        self._update_teams()
        for team in self.teams:
            if team.id == id:
                return team
        raise IndexError

    #----- Writing methods -----""
    def create_team(self, team):
        """Takes a team object and saves it to the data layer"""
        self._update_teams()
        team.id = get_random_id() # add a unique id
        self.teams.append(team)
        self._write_teams()
        
        

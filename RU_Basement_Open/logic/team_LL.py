from functions.get_random_id import get_random_id
from models import team_mdl


class TeamLL():
    """ Team logic layer class. Takes input model class from ui layer"""
    def __init__(self, data_connection):
        self.data_wrapper = data_connection
        self.teams = ""
        self._update_teams()

    # ----- Internal methods -----#
    def _update_teams(self):
        """Gets all teams from data layer"""
        self.teams = self.data_wrapper.get_all_teams()

    def _write_teams(self):
        """Sends team data to data layer to update"""
        self.data_wrapper.write_teams(self.teams)

    def _find_team(self, id):
        """ Searches for a team by id. If it exists, return it.
        If not, return False """
        for team in self.teams:
            if team.id == id:
                return team
        raise IndexError

    # ----- Reading methods -----#
    def get_all_teams(self):
        """Returns a list of all teams from the data layer"""
        self._update_teams()
        return self.teams

    def get_team(self, id):
        """Returns a team from the data layer by id"""
        self._update_teams()
        return self._find_team(id)

    def get_captain(self, team_id):
        """Takes a team id and returns it's captains player id"""
        self._update_teams()
        team = self._find_team(team_id)
        if team:
            return team.captain_id
        else:
            raise IndexError

    def get_players(self, team_id):
        """ Takes a team id, returns that teams player ids"""
        return self.get_team(team_id).player_ids

    def team_name_exists(self, name, team_ids):
        """Takes name and a list of team ids, if that name exists on any of the teams,
        return True, else return False"""
        for team_id in team_ids:
            team = self.get_team(team_id)
            if team.name == name:
                return True
        return False

    # ----- Writing methods -----#
    def create_team(self, team):
        """Takes a team object and saves it to the data layer"""
        self._update_teams()
        team.id = get_random_id()  # add a unique id
        self.teams.append(team)
        self._write_teams()
        return team.id

    def add_player(self, player_id, team_id):
        """Take id's for a team and a player, adds that player to the team"""
        self._update_teams()
        try:
            team = self._find_team(team_id)
            team.player_ids.append(player_id)
            self._write_teams()
        except IndexError:
            raise IndexError

    def promote_to_captain(self, player_id, team_id):
        """Takes id's for a player and a team. Promotes that player to captain,
        if he's a part of the team"""
        self._update_teams()
        team = self._find_team(team_id)
        if player_id not in team.player_ids:
            raise IndexError
        else:  # Assign new captain
            team.captain_id = player_id
            self._write_teams()

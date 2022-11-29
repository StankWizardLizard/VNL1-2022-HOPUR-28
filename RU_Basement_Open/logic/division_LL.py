
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

    def _count_legs(self, home, results):
        win_home = 0
        for leg in results:
            if home:
                if leg[0] > leg[1]:
                    win_home += 1
        win_away = 7-win_round
        return win_home, win_away

    def _calculate_record(self, team, matches):
        """
        Calculates win loss record for each team
        :returns: [team.name, win_games, loss_games,win_round, loss_round]

        """
        match_counter = 0
        win_games = 0
        loss_games = 0
        win_round = 0
        loss_round = 0
        for match in matches:
            if team.id == match.homeTeam:
                win_legs, loss_legs = self._count_legs(True, match.results)
            elif team.id == match.awayTeam:
                loss_legs, win_legs = self._count_legs(False, match.results)
            else:
                continue
            if win_legs >= 4:
                win_games += 1
            else:
                loss_games += 1
            win_round += win_legs
            loss_round += loss_legs

        return [team.name, win_games, loss_games, win_round, loss_round]

        return record

    def _sort_leaderboard(self, leaderboard):
        """
        fully sorts leaderboard by wins, leg wins, and then alphabetically
          :returns: leaderboard

          """
        leaderboard.sort(key=lambda x: x[1], reverse=True)
        for i in range(leaderboard)-1:
            a_wins = leaderboard[i][1],
            a_leg_wins = leaderboard[i][3]
            a_name = leaderboard[i][0],
            a = leaderboard[i]
            b_wins = leaderboard[i+1][1],
            b_leg_wins = leaderboard[i+1][3]
            b_name = leaderboard[i+1][0]

            if a_wins == b_wins:
                if a_leg_wins < b_leg_wins:
                    leaderboard[i] = leaderboard[i+1]
                    leaderboard[i+1] = a
                elif a_leg_wins == b_leg_wins:
                    if a_name < b_name:
                        leaderboard[i] = leaderboard[i+1]
                        leaderboard[i+1] = a
        return leaderboard
    #----- Reading methods -----#

    def get_leaderboard(self):
        """TODO: gets_leaderboard and returns to ui
        :returns: leaderboard

        """
        matches = self.data_wrapper.get_all_matches()
        teams = self.data_wrapper.get_all_teams()
        leaderboard = []
        for team in teams:
            leaderboard.append(self._calculate_record(team, match))
        leaderboard = self._sort_leaderboard(leaderboard)
        return leaderboard

    def get_division(self, division_id):
        """TODO: Docstring for get_division.
        :returns: TODO

        """
        self._update_divisions()
        return self._find_division(division_id)


    #----- Writing methods -----#
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
        if division:
            division.team_ids.append(team_id)
            self._write_divisions()

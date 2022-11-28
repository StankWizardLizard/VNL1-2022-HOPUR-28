
from functions.get_random_id import get_random_id

class DivisionLL():

    """Division logic layer class. Takes input model class from ui layer"""

    def __init__(self, data_wrapper) :
        """

        :division_mdl: TODO

        """
        self.data_wrapper = data_wrapper
    def create_division(self,division):
        """
        Creates new devision. Gets division object as input and sends to storage layer
        """
        division.id = get_random_id()
        self.storage.write_division_person_to_file(division)
        return "returned!"

    def _count_legs(self,home,results):
        win_home = 0
        for leg in results:
            if home:
                if leg[0]>leg[1]:
                    win_home += 1
        win_away = 7-win_round
        return win_home, win_away



    def _calculate_record(self,team, matches):
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
                loss_games +=1
            win_round += win_legs
            loss_round += loss_legs


        return [team.name, win_games,loss_games,win_round,loss_round]





        return record
    def _sort_leaderboard(self, leaderboard):
        """
        fully sorts leaderboard by wins, leg wins, and then alphabetically
          :returns: leaderboard

          """
        leaderboard.sort(key=lambda x: x[1], reverse = True)
        for i in range(leaderboard)-1:
            a_wins = leaderboard[i][1]
            a_leg_wins = leaderboard[i][3]
            a_name = leaderboard[i][0]
            a = leaderboard[i]
            b_wins = leadboard[i+1][1]
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
    def get_leaderboard(self):
        """TODO: gets_leaderboard and returns to ui
        :returns: leaderboard

        """
        matches = self.data_wrapper.get_all_matches()
        teams = self.data_wrapper.get_all_teams()
        leaderboard = []
        for team in teams:
            leaderboard.append(self._calculate_record(team,match))
        leaderboard= self._sort_leaderboard(leaderboard)
        return leaderboard



    def get_division(self, division_id):
        """TODO: Docstring for get_division.
        :returns: TODO

        """
        divisions = self.data_wrapper.get_division_from_file()
        for division in divisions:
            if division["id"] == division_id:
                return division 


       

        

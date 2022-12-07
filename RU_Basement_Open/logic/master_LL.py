

class MasterLL:
    def __init__(self, match_logic_connection, division_logic_connection, team_logic_connection, player_logic_connection, data_wrapper):
        self.match_logic = match_logic_connection
        self.division_logic = division_logic_connection
        self.team_logic = team_logic_connection
        self.player_logic = player_logic_connection
        self.data_wrapper = data_wrapper

    def update_division_start_and_end_date(self, division_id):
        match_ids = self.division_logic.get_match_ids(division_id)
        start_date, end_date = self.match_logic.get_start_and_end_date(
            match_ids)
        self.division_logic.set_dates(start_date, end_date, division_id)

    def generate_division_matches(self, division_id):
        team_ids = self.division_logic.get_team_ids(division_id)
        match_ids = self.match_logic.gen_matches(team_ids, division_id)
        self.division_logic.add_matches(match_ids, division_id)
        self.update_division_start_and_end_date(division_id)

    def postpone_match(self, new_date, division_id, match_id):
        self.match_logic.set_date(self, match_id, new_date)
        self.update_division_start_and_end_date(division_id)

    def _get_players_by_division(self, division_id):
        """Takes a division id, returns a list of all players competing in that division"""
        # get all teams in division
        team_ids = self.division_logic.get_team_ids(division_id)
        player_ids = []
        players = []
        # get all players in each team
        for team_id in team_ids:
            curr_player_ids = self.team_logic.get_players(team_id)
            # append current teams players to all players
            player_ids = player_ids + curr_player_ids
        # get player object for each player id
        for player_id in player_ids:
            player = self.player_logic.get_player(player_id)
            players.append(player)
        return players

    def get_player_leaderboard_by_division(self, division_id, category):
        """Takes a division id and a category, returns a sorted list 
        of player by their score in the specified category"""
        players = self._get_players_by_division(division_id)
        result_list = []
        # Get result for each player and store in a dict with their name
        for player in players:
            if category == "inshot":
                _, result, _ = self.match_logic.get_player_highest_shots_by_division(
                    player.id, division_id)
            elif category == "outshot":
                _, _, result = self.match_logic.get_player_highest_shots_by_division(
                    player.id, division_id)
            elif category == "qps":
                result = self.match_logic.get_player_total_qps_by_division(
                    player.id, division_id)

            result_list.append({"player_name": player.name, "result": result})
        # Sort dictionary by name
        result_list = sorted(
            result_list, key=lambda x: x["result"], reverse=True)
        return result_list

    def get_leaderboard(self):
        """TODO: gets_leaderboard and returns to ui
        :returns: leaderboard

        """
        matches = self.data_wrapper.get_all_matches()
        teams = self.data_wrapper.get_all_teams()
        leaderboard = []
        for team in teams:
            leaderboard.append(self._calculate_record(team, matches))
        leaderboard = self._sort_leaderboard(leaderboard)
        return leaderboard

    def _count_legs(self, home, results):
        win_home = 0
        for leg in results:
            if home:
                if leg[0] > leg[1]:
                    win_home += 1
        win_away = 7-win_home
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
            if team.id == match.home_team:
                win_legs, loss_legs = self._count_legs(True, match.results)
            elif team.id == match.away_team:
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
        for i in range(len(leaderboard)-1):
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

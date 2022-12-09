

class MasterLL:
    def __init__(self, match_logic_connection, division_logic_connection, team_logic_connection, player_logic_connection, club_logic_connection, data_wrapper):
        """ Master logic layer class, handles complicated methods that needs data from more than one model type"""
        self.match_logic = match_logic_connection
        self.division_logic = division_logic_connection
        self.team_logic = team_logic_connection
        self.player_logic = player_logic_connection
        self.club_logic = club_logic_connection
        self.data_wrapper = data_wrapper

    def get_players_by_division(self, division_id):
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
        players = self.get_players_by_division(division_id)
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




    def get_player_statistics_by_division(self, player_id, division_id, last_n_matches):
        """Takes a player and division id, returns a dict containing that players
        name, his winrate in 301, 501, cricket and quad-501 along with his total
        quality points, highest in- and outshot and highest shot overall."""
        total_score_dict = {   
        "score_501" : [0, 0,0],
        "score_301" : [0, 0,0],
        "score_cricket" : [0, 0,0],
        "score_501_quad" : [0, 0,0]
        }
        player_matches = []
        matches = self.match_logic.get_matches_by_division(division_id)
        for match in matches:
            if player_id in (match.home_team_players + match.away_team_players):
                player_matches.append(match)

        # Filter for last n matches
        if last_n_matches is not None:
            if last_n_matches > len(player_matches):
                raise IndexError(f"{last_n_matches} exeeds matches played by player")
            matches = player_matches[-last_n_matches:]
        
        for match in matches:
            if match.results != []:
                score = self._count_player_wins_in_match(player_id, match)
                # Add results to total score
                for key in total_score_dict:
                    total_score_dict[key] = [sum(value) for value in zip(total_score_dict[key], score[key])]
        return total_score_dict
            
    def _count_player_wins_in_match(self, player_id, match):
        """Takes a player id and a matcj object, counts and returns the players winrates"""
        def increment_score(score_ls, win):
            if win:
                score_ls[0] = score_ls[0] + 1
            else:
                score_ls[1] = score_ls[1] + 1

        score_501 = [0, 0, 0]
        score_301 = [0, 0, 0]
        score_cricket = [0, 0, 0]
        score_501_quad = [0, 0, 0]
        # when 0 <= i <= 3 game type is 501
        # when i = 4 game type is 301
        # when i = 5 game type is cricket
        # when i = 6 game type is 501 quad
        for i, game in enumerate(match.results):
            # Check whether the player won or lost the game
            # if not game:
            #     continue
            if player_id in game['home_plr']:
                if game['result'][0] > game['result'][1]:
                    win = True
                if game['result'][0] < game['result'][1]:
                    win = False
            elif player_id in game['away_plr']:
                if game['result'][0] < game['result'][1]:
                    win = True
                if game['result'][0] > game['result'][1]:
                    win = False
            else:
                continue
            # Increment score for a game type depending on which game is being read
            if 0 <= i and i <= 3:
                increment_score(score_501, win)
            if i == 4:
                increment_score(score_301, win)
            if i == 5:
                increment_score(score_cricket, win)
            if i == 6:
                increment_score(score_501_quad, win)    
        # Clalculate winrates for all types
        if score_501[0] + score_501[1] == 0:
            score_501[2] = 0
        else:
            score_501[2]=score_501[0]/(score_501[0]+score_501[1])*100
        
        if score_301[0] + score_301[1] == 0:
            score_301[2] = 0
        else:
            score_301[2]=score_301[0]/(score_301[0]+score_301[1])*100
        
        if score_cricket[0] + score_cricket[1] == 0:
            score_cricket[2] = 0
        else:
            score_cricket[2]=score_cricket[0]/(score_cricket[0]+score_cricket[1])*100
        
        if score_501_quad[0] + score_501_quad[1] == 0:
            score_501_quad[2] = 0
        else:
            score_501_quad[2]=score_501_quad[0]/(score_501_quad[0]+score_501_quad[1])*100
        
       
        return {
            "score_301": score_301,
            "score_501": score_501,
            "score_cricket": score_cricket,
            "score_501_quad": score_501_quad,
        }

    def _count_legs(self, results):
        """ Takes a match results and returns how many legs were won by home and away respectively"""
        win_home = 0
        for leg in results:
            if leg['result'][0] > leg['result'][1]:
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
            if match.results == []:
                continue
            if team.id == match.home_team:
                win_legs, loss_legs = self._count_legs(match.results)
            elif team.id == match.away_team:
                loss_legs, win_legs = self._count_legs(match.results)
            else:
                continue
            if win_legs >= 4:
                win_games += 1
            else:
                loss_games += 1
            win_round += win_legs
            loss_round += loss_legs

        return [team.name, win_games, loss_games, win_round, loss_round]

    def _sort_leaderboard(self, leaderboard):
        """
        fully sorts leaderboard by wins, leg wins, and then alphabetically
          :returns: leaderboard

          """
        leaderboard.sort(key=lambda x: x[1], reverse=True)
        for i in range(len(leaderboard)-1):
            a_wins = int(leaderboard[i][1])
            a_leg_wins = int(leaderboard[i][3])
            a_name = str(leaderboard[i][0])
            a = leaderboard[i]
            b_wins = int(leaderboard[i+1][1])
            b_leg_wins = int(leaderboard[i+1][3])
            b_name = str(leaderboard[i+1][0])

            if a_wins == b_wins:
                if a_leg_wins < b_leg_wins:
                    leaderboard[i] = leaderboard[i+1]
                    leaderboard[i+1] = a
                elif a_leg_wins == b_leg_wins:
                    if a_name < b_name:
                        leaderboard[i] = leaderboard[i+1]
                        leaderboard[i+1] = a
        return leaderboard

    def update_division_start_and_end_date(self, division_id):
        """Takes a division id, scans that divisions matches and finds the lowest and highest dates.
        Then updates the divisions start and end date accordingly"""
        match_ids = self.division_logic.get_match_ids(division_id)
        start_date, end_date = self.match_logic.get_start_and_end_date(
            match_ids)
        self.division_logic.set_dates(start_date, end_date, division_id)

    def generate_division_matches(self, division_id, start_date, days_between_matchdays, rounds):
        """ Takes a division id, start date, rest days and rounds, generates matches and allocates teams to 
        match days with specified rest days between them"""
        team_ids = self.division_logic.get_team_ids(division_id)
        match_ids = self.match_logic.gen_matches(
            team_ids, division_id, start_date, days_between_matchdays, rounds)
        self.division_logic.add_matches(match_ids, division_id)
        self.update_division_start_and_end_date(division_id)

    def postpone_match(self, new_date, division_id, match_id):
        """ Takes a date string, a division id and a match id, sets that matches date as the new date
        and updates the divisions start or end date if needed"""
        self.match_logic.set_date(match_id, new_date)
        self.update_division_start_and_end_date(division_id)

    def get_player_leaderboard_by_division(self, division_id, category):
        """Takes a division id and a category, returns a sorted list 
        of player by their score in the specified category"""
        players = self.get_players_by_division(division_id)
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

    def get_player_statistics_by_division(self, player_id, division_id, last_n_matches):
        """Takes a player and division id, returns a dict containing that players
        name, his winrate in 301, 501, cricket and quad-501 along with his total
        quality points, highest in- and outshot and highest shot overall."""
        total_score_dict = {
            "score_501": [0, 0, 0],
            "score_301": [0, 0, 0],
            "score_cricket": [0, 0, 0],
            "score_501_quad": [0, 0, 0]
        }
        player_matches = []
        matches = self.match_logic.get_matches_by_division(division_id)
        for match in matches:
            if player_id in (match.home_team_players + match.away_team_players):
                player_matches.append(match)

        # Filter for last n matches
        if last_n_matches is not None:
            if last_n_matches > len(player_matches):
                raise IndexError(
                    f"{last_n_matches} exeeds matches played by player")
            matches = player_matches[-last_n_matches:]

        for match in matches:
            if match.results != []:
                score = self._count_player_wins_in_match(player_id, match)
                # Add results to total score
                for key in total_score_dict:
                    total_score_dict[key] = [sum(value) for value in zip(
                        total_score_dict[key], score[key])]

        return total_score_dict

    def get_leaderboard(self, divison):
        """TODO: gets_leaderboard and returns to ui
        :returns: leaderboard

        """

        all_matches = self.data_wrapper.get_all_matches()
        matches_in_division = []
        for match in all_matches:
            if match.division_id == divison.id:
                matches_in_division.append(match)

        all_teams = self.data_wrapper.get_all_teams()
        teams_in_division = []

        for team in all_teams:
            if team.id in divison.team_ids:
                teams_in_division.append(team)

        leaderboard = []
        for team in teams_in_division:
            leaderboard.append(self._calculate_record(
                team, matches_in_division))
        leaderboard = self._sort_leaderboard(leaderboard)
        return leaderboard

    def get_division_unplayed_match_ids(self, division_id):
        """ Takes a division id, returns unplayed matches in that division"""
        unplayed_match_ids = []
        match_ids = self.division_logic.get_match_ids(division_id)
        for match_id in match_ids:
            match = self.match_logic.get_match(match_id)
            if match.results == []:
                unplayed_match_ids.append(match_id)
        return unplayed_match_ids
    
    def get_team_names_by_division(self, division_id):
        """Takes match id and returns the team names that are playing matches"""
        team_names = []

        unplayed_match_ids = self.get_division_unplayed_match_ids(division_id)
        team_ids = self.match_logic.get_teams(unplayed_match_ids)
        for match in team_ids:
            a = []
            for team_id in match:
                team_name = self.team_logic.get_team(team_id).name
                a.append(team_name)
            team_names.append(tuple(a))
        return team_names

    def team_name_exists_on_club(self, name, club_id):
        """Takes a team name and a club id, if that team name exists on that club, return True
        else return False"""
        team_ids = self.club_logic.get_teams(club_id)
        return self.team_logic.team_name_exists(name, team_ids)


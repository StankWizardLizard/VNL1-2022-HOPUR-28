from datetime import date
from functions.get_random_id import get_random_id
from models.match_mdl import MatchMdl
from collections import defaultdict


class MatchLL():
    def __init__(self, data_connection):
        self.data_wrapper = data_connection
        self.matches = ""
        self._update_matches

    # ----- Internal methods -----#
    def _count_qps(self, qp_str):
        qp_ls = qp_str.strip().split(",")
        score = 0
        for turn in qp_ls:
            # In or out shot
            if "n" in turn or "u" in turn:
                score += 1
                turn = turn.replace("n", "")
                turn = turn.replace("u", "")

            # Regular 301 or 501 throw
            if turn.isnumeric():
                turn = int(turn)
                if turn > 93:
                    score += 1
                if turn > 119:
                    score += 1
                if turn > 169:
                    score += 1
                continue

            # Cricket hit
            if "h" in turn:
                turn = int(turn.replace("h", ""))
                if turn > 4:
                    score += 1
                if turn > 6:
                    score += 1
                if turn == 9:
                    score += 1
                continue

            # Cricket Bullseye
            if "b" in turn:
                turn = int(turn.replace("b", ""))
                score += turn
                if turn >= 5:
                    score -= 1
        return score

    def _get_highest_shots(self, qp_str):
        """Takes a quality point string, returns the values of 
        the highest inshot, outshot and shot found"""
        qp_ls = qp_str.strip().split(",")
        highest_shot = 0
        highest_inshot = 0
        highest_outshot = 0
        for turn in qp_ls:
            # If the turn was an inshot
            if "n" in turn:
                turn = int(turn.replace("n", ""))
                if turn > highest_inshot:
                    highest_inshot = turn
            # if the turn was an outshot
            elif "u" in turn:
                turn = int(turn.replace("u", ""))
                if turn > highest_outshot:
                    highest_outshot = turn
            # else the turn was a regular shot
            elif turn.isnumeric():
                turn = int(turn)
                if turn > highest_shot:
                    highest_shot = turn

        # if a in- or outshot was higher than the current highest
        # regular shot, set the regular shot to match.
        if highest_inshot > highest_shot:
            highest_shot = highest_inshot
        if highest_outshot > highest_shot:
            highest_shot = highest_outshot

        return highest_shot, highest_inshot, highest_outshot

    def _update_matches(self):
        """Gets all matches from data layer"""
        self.matches = self.data_wrapper.get_all_matches()

    def _write_matches(self):
        """Sends match data to data layer to update"""
        self.data_wrapper.write_matches(self.matches)

    def _find_match(self, id):
        """ Searches for a match by id. If it exists, return it.
        If not, return False """
        for match in self.matches:
            if match.id == id:
                return match
        raise IndexError

    # ----- Reading methods -----#
    def get_all_player_qp_strings(self, player_id):
        """Takes a player id, returns a dictionary of divisions as keys 
        and a list of that player's quality point strings from all matches 
        in that division as values"""
        self._update_matches()
        matches = self.get_all_matches()
        qp_dict = defaultdict(list)
        for match in matches:
            for player in match.quality_points:
                if player == player_id:
                    qp_dict[match.division_id].append(
                        match.quality_points[player])
        return qp_dict

    def get_player_total_qps_by_division(self, player_id, division_id):
        """Takes a player and division id, returns the player's total 
        quality points scored from all matches in that division"""
        qp_dict = self.get_all_player_qp_strings(player_id)
        qp_ls = qp_dict[division_id]
        total_score = 0
        for qp_str in qp_ls:
            total_score += self._count_qps(qp_str)
        return total_score

    def get_player_highest_shots_by_division(self, player_id, division_id):
        """Takes a player and division_id, returns the player's scores for his
        highest in-, out and regular shots he hit in all matches of that division"""
        qp_dict = self.get_all_player_qp_strings(player_id)
        qp_ls = qp_dict[division_id]
        highest_shot = 0
        highest_inshot = 0
        highest_outshot = 0
        for qp_str in qp_ls:
            shot, inshot, outshot = self._get_highest_shots(qp_str)
            if shot > highest_shot:
                highest_shot = shot
            if inshot > highest_inshot:
                highest_inshot = inshot
            if outshot > highest_outshot:
                highest_outshot = outshot
        return highest_shot, highest_inshot, highest_outshot

    def get_all_matches(self):
        """Returns a list of all matches"""
        self._update_matches()
        return self.matches

    def get_match(self, id):
        """Returns a match by id from data layer"""
        self._update_matches()
        return self._find_match(id)

    def get_matches_by_division(self, division_id):
        """Takes a division id, returns a list of match objects for that division """
        self._update_matches()
        match_ls = []
        for match in self.matches:
            if match.division_id == division_id:
                match_ls.append(match)
        return match_ls

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

    def get_date(self, id):
        """Takes a match id, returns the matches date"""
        match = self._find_match(id)
        date_ls = match.date.split("-")
        year, month, day = [int(x) for x in date_ls]
        match_date = date(year, month, day)
        return match_date

    def get_start_and_end_date(self, match_ids: list):
        """Takes a list of match ids and returns the
        lowest and highest date found"""
        dates = []
        for id in match_ids:
            dates.append(self.get_date(id))
        return (str(min(dates)), str(max(dates)))

    # ----- Writing methods -----#

    def gen_matches(self, team_ids: list, division_id):
        if len(team_ids) % 2:
            team_ids.append("c")
        l = len(team_ids)

        t1 = team_ids[:l//2]
        t2 = team_ids[l//2:]

        match_days = []
        for _ in range(l-1):
            x = t1.pop()
            t2.append(x)

            y = t2.pop(0)
            t1.insert(1, y)

            fixtures = list(zip(t1, t2))
            for fixture in fixtures:
                if "c" in fixture:
                    fixtures.remove(fixture)
                    break

            match_days.append(fixtures)

        i = 1
        match_ids = []
        for day in match_days:
            for matchup in day:
                t1, t2 = matchup
                match = MatchMdl(f"2022-12-{i}", t1,  # TODO: Take division start date
                                 t2, division_id=division_id)
                match_id = self.create_match(match)
                match_ids.append(match_id)
            i += 1

        return match_ids

    def create_match(self, match):
        """Takes a match object and forwards it to the data layer"""
        self._update_matches()
        match.id = get_random_id()
        self.matches.append(match)
        self._write_matches()
        return match.id

    def set_date(self, id, new_date):
        """Sets a matches date and updates data layer"""
        self._update_matches()
        match = self._find_match(id)
        match.date = new_date
        self._write_matches

    def set_results(self, id, results):
        """Sets a matches results and uptades data layer"""
        self._update_matches()
        match = self._find_match(id)
        match.results = results
        self._write_matches()

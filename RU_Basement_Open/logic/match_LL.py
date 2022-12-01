from itertools import combinations
from datetime import date
from functions.get_random_id import get_random_id
from models.match_mdl import MatchMdl


class MatchLL():
    def __init__(self, data_connection):
        self.data_wrapper = data_connection
        self.matches = ""
        self._update_matches
        
    #----- Internal methods -----#
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

    #----- Reading methods -----#
    def get_all_matches(self):
        """Returns a list of all matches"""
        self._update_matches()
        return self.matches

    def get_match(self, id):
        """Returns a match by id from data layer"""
        self._update_matches()
        return self._find_match(id)

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
    
    def get_start_and_end_date(self, match_ids:list):
        """Takes a list of match ids and returns the
        lowest and highest date found"""
        dates = []
        for id in match_ids:
            dates.append(self.get_date(id))
        return (str(min(dates)), str(max(dates)))
            

    #----- Writing methods -----#
    def gen_matches(self, team_ids: list, division_id):
        def team_in_list():
            for matchup in match_day_ls:
                if team_1 in matchup or team_2 in matchup:
                    return True
            return False
        
        def move_team_to_front(lst, team):
            targetvalue = [matchup for matchup in lst if team in matchup]
            if targetvalue:
                targetvalue = targetvalue[0]
                lst.insert(0, lst.pop(lst.index(targetvalue)))
        
        matchups_unassigned = [comb for comb in combinations(team_ids, 2)]
        matchups_unassigned.insert(0, matchups_unassigned.pop(len(matchups_unassigned)-1))
        matchups_unassigned.insert(0, matchups_unassigned.pop(len(matchups_unassigned)-1))

        # print(matchups_unassigned)
        match_days_ls = []
        leftover = ""
        while len(matchups_unassigned):
            match_day_ls = []
            competing_teams_set = set()
            
            if leftover:
                move_team_to_front(matchups_unassigned, leftover)
            
            for matchup in matchups_unassigned[:]:
                team_1, team_2 = matchup
                if not team_in_list():
                    competing_teams_set.update(matchup)
                    match_day_ls.append(matchup)
                    matchups_unassigned.remove(matchup)
            
            # x = Find team that did not compete
            leftover = set(team_ids) - competing_teams_set
            if leftover:
                leftover = next(iter(leftover))
            else:
                leftover=None
                
            # print(leftover)
            match_days_ls.append(match_day_ls)
            
            
        i = 1
        match_ids = []
        for day in match_days_ls:
            for matchup in day:
                t1, t2 = matchup
                match = MatchMdl(f"2022-12-{i}",t1, t2, division_id=division_id)
                match_id = self.create_match(match)
                match_ids.append(match_id)
            i += 1
        return match_ids
                    
        # Print match days
        # print("\nmatch days: ")
        # for match_day in match_days_ls:
        #     print(match_day)
        # print("no of match days: ", len(match_days_ls))        
            
            
            
        
        

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

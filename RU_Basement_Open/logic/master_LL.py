

class MasterLL:
    def __init__(self, match_logic_connection, division_logic_connection):
        self.match_logic = match_logic_connection
        self.division_logic = division_logic_connection
        
    def update_division_start_and_end_date(self, division_id):
        match_ids = self.division_logic.get_match_ids(division_id)
        start_date, end_date= self.match_logic.get_start_and_end_date(match_ids)
        self.division_logic.set_dates(start_date, end_date, division_id)
    
    def generate_division_matches(self, team_ids, division_id):
        match_ids = self.match_logic.gen_matches(team_ids, division_id)
        self.division_logic.add_matches(match_ids, division_id)
        self.update_division_start_and_end_date(division_id)
        
    def postpone_match(self, new_date, division_id, match_id):
        self.match_logic.set_date(self, match_id, new_date)
        self.update_division_start_and_end_date(division_id)

        
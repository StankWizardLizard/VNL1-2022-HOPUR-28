

class MasterLL:
    def __init__(self, match_logic_connection, division_logic_connection):
        self.match_logic = match_logic_connection
        self.division_logic = division_logic_connection
    
    def generate_division_matches(self, team_ids, division_id):
        match_ids = self.match_logic.gen_matches(team_ids, division_id)
        self.division_logic.add_matches(match_ids, division_id)
        start_date, end_date= self.match_logic.get_start_and_end_date(match_ids)
        self.division_logic.set_dates(start_date, end_date, division_id)
        



        
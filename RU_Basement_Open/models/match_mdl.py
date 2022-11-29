class MatchMdl():
    def __init__(
            self, date:str="", home_team:str="", away_team:str="",
            home_team_players:list=[], away_team_players:list=[],
            division_id:str="", results:list="str", quality_points:dict={}, id:str=""):

        self.date = date
        self.home_team = home_team
        self.away_team = away_team
        self.home_team_players = home_team_players
        self.away_team_players = away_team_players
        self.results = results
        self.quality_points = quality_points
        self.division_id = division_id 
        self.id = id  
        
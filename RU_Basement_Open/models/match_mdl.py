class MatchMdl():
    def __init__(
            self, date, home_team, away_team,
            home_team_players, away_team_players,
            results, quality_points, division_id, id=""):

        self.date = date
        self.home_team = home_team
        self.away_team = away_team
        self.home_team_players = home_team_players
        self.away_team_players = away_team_players
        self.results = results
        self.quality_points = quality_points
        
        self.division_id = division_id # Assign
        self.id = id # Generate 
        
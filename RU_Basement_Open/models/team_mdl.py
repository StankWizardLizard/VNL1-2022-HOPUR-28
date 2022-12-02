class TeamMdl():
    def __init__(
            self, name:str="", player_ids:list=[],
            captain_id:str="", id:str=""):

        self.name = name

        self.captain_id = captain_id
        self.player_ids = player_ids
        self.id = id  # Generate!

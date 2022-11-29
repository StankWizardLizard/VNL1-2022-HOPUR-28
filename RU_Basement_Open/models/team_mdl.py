class TeamMdl():
    def __init__(
            self, name, player_ids=[],
            captain_id="", id=""):

        self.name = name

        self.captain_id = captain_id
        self.player_ids = player_ids
        self.id = id  # Generate!

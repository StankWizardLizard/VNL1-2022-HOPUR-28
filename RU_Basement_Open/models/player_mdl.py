class PlayerMdl():
    def __init__(
            self, name:str="", ssn:str="", mobile_nr:str="",
            home_nr:str="", address:str="", email:str="",
            team_id:str="", id:str="", captain:bool = False, club_id:str=""):

        self.name = name
        self.ssn = ssn
        self.mobile_nr = mobile_nr
        self.home_nr = home_nr
        self.address = address
        self.email = email
        self.captain = captain
        self.club_id = club_id
        self.id = id  # Generate
        self.team_id = team_id  # Assign in logic


class PlayerMdl():
    def __init__(
            self, name, ssn, mobile_nr,
            home_nr, address, email,
            team_id, id="", captain = False):

        self.name = name
        self.ssn = ssn
        self.mobile_nr = mobile_nr
        self.home_nr = home_nr
        self.address = address
        self.email = email
        self.captain = captain

        self.id = id  # Generate
        self.team_id = team_id  # Assign in logic


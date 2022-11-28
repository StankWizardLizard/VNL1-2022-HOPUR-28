
class PlayerMdl():
    def __init__(
            self, name, SSN, mobile_nr,
            home_nr, address, email,
            team_id, id=""):

        self.name = name
        self.SSN = SSN
        self.mobile_nr = mobile_nr
        self.home_nr = home_nr
        self.address = address
        self.email = email

        self.id = id  # Generate
        self.team_id = team_id  # Assign in logic

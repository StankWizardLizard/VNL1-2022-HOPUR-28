class PlayerMdl():
    """ A model class for storing player information"""
    def __init__(
            self, name:str="", ssn:str="", mobile_nr:str="",
            home_nr:str="", address:str="", email:str="",
            id:str="",club_id:str=""):

        self.name = name
        self.ssn = ssn
        self.mobile_nr = mobile_nr
        self.home_nr = home_nr
        self.address = address
        self.email = email
        self.club_id = club_id
        self.id = id  # Generate


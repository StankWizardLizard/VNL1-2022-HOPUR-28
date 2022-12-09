class ClubMdl:
    """ A model class for storing club information"""
    def __init__(
            self, name:str="", address:str="",
            phone_nr:str="", id:str="", teams_id:list=[]):

        self.id = id
        self.teams_id = teams_id
        self.name = name
        self.address = address
        self.phone = phone_nr

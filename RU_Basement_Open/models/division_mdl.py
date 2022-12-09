class DivisionMdl:
    """ A model class for storing division information"""
    def __init__(
            self,  name:str,  host_name:str="", phone_nr:str="", 
            type:str= "L",rounds:int=0, team_ids:list=[], matches:list=[], start_date:str="", end_date:str="", id:str="",):

        self.id = id
        self.name = name
        self.team_ids = team_ids
        self.host_name = host_name
        self.phone_nr = phone_nr
        self.start_date = start_date
        self.end_date = end_date
        self.type = type
        self.rounds = rounds
        self.matches = matches


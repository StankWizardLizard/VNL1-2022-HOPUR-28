class DivisionMdl:
    def __init__(
            self, id:str="", name:str="", team_ids:list=[], host_name:str= "",
            phone_nr:str="", start_date:str="", end_date:str="",
            type:str= "L",rounds:int=0, matches:list=[]):

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


class ClubMdl:
    def __init__(self, name, address, phone_nr, id="", teams_id=[]):
        self.id = id
        self.teams_id = teams_id
        self.name = name
        self.address = address
        self.phone = phone_nr

from models.player_mdl import PlayerMdl
from models.club_mdl import ClubMdl
from models.team_mdl import TeamMdl
from models.division_mdl import DivisionMdl

def create_player(
    logic_wrapper, name:str="", ssn:str="",
    mobile_nr:str="", home_nr:str="", address:str="", email:str=""):
    '''takes in info about player and turns it into an object that it passes down to the logic layer
    to create a player and returns the id of the player'''

    player = PlayerMdl(name=name, ssn=ssn, mobile_nr=mobile_nr, home_nr=home_nr, address=address, email=email)
    player_id = logic_wrapper.create_player(player)
    return player_id

def create_club(logic_wrapper, name:str="", address:str="", phone:str=""):
    '''takes in info about club and turns it into an object that it passes down to the logic layer
    to create a division and returns the id of the club'''

    club = ClubMdl(name = name, address = address, phone_nr = phone)
    club_id = logic_wrapper.create_club(club)
    return club_id

def create_team(logic_wrapper, name:str=""):
    '''takes in name of a team and turns it into an object that it sends down to the logic layer
    to create a team and returns the id of the team'''
    team = TeamMdl(name = name)
    team_id = logic_wrapper.create_team(team)
    return team_id

def create_division(
    logic_wrapper, name:str ="", team_ids:list=[], 
    host_name:str="", phone_nr:str="",rounds:int=1):
    '''takes in info about division and turns it into an object that it passes down to the logic layer
    to create a division and returns the id of the division'''

    division = DivisionMdl(name = name, team_ids=team_ids, host_name=host_name, phone_nr=phone_nr, rounds=rounds)
    division_id = logic_wrapper.create_division(division)
    return division_id

def get_all_teams(logic_wrapper):
    '''returns a list of all teams'''

    teams = logic_wrapper.get_all_teams()
    return teams

def get_all_players(logic_wrapper):
    '''returns a list of all players'''

    players = logic_wrapper.get_all_players()
    return players

def get_division(logic_wrapper, division_id = "0"):
    '''returns a division object by id'''

    try:
        division = logic_wrapper.get_division(division_id)
        return division
    except IndexError:
        print("No division with that ID")

def get_all_matches(logic_wrapper):
    '''returns a list of all matches'''

    matches = logic_wrapper.get_all_matches()
    return matches

def get_all_clubs(logic_wrapper):
    '''returns a list of all clubs'''

    clubs = logic_wrapper.get_all_clubs()
    return clubs

def get_all_unplayed_matches(logic_wrapper):
    '''returns a list of all unplayed matches'''

    unplayed_matches = logic_wrapper.get_upcoming_matches()
    return unplayed_matches
    
def get_all_concluded_matches(logic_wrapper):
    '''returns a list of all concluded matches'''

    played_matches = logic_wrapper.get_concluded_matches()
    return played_matches

def get_player(logic_wrapper, id):
    '''returns a player object by id'''
    try: 
        player = logic_wrapper.get_player(id)
        return player
    except IndexError:
        print("No player with that ID")

#untested 

'''def set_date(logic_wrapper):
    id = input("Input match ID: ")
    new_date = input("Input new date YYYY-MM-DD: ")
    logic_wrapper.set_date(id, new_date)
    print_matches(logic_wrapper)'''

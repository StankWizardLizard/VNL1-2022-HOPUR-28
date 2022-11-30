from models.player_mdl import PlayerMdl
from models.club_mdl import ClubMdl
from models.team_mdl import TeamMdl
from models.division_mdl import DivisionMdl

def create_player(logic_wrapper):
    name = input("Enter the name of the player: ")
    ssn = input("Enter the ID number of the player: ")
    mobile_nr = input("Enter the mobile number of the player: ")
    home_nr = input("Enter the home number of the player: ")
    address = input("Enter the address of the player: ")
    email = input("Enter the email of the player: ")
    player = PlayerMdl(name=name, ssn=ssn, mobile_nr=mobile_nr, home_nr=home_nr, address=address, email=email)
    id = logic_wrapper.create_player(player)
    return id

def create_club(logic_wrapper):
    name = input("Enter the name of the club: ")
    address = input("Enter the address of the club: ")
    phone = input("Enter the phone number of the club: ")
    club = ClubMdl(name = name, address = address, phone_nr = phone)
    logic_wrapper.create_club(club)

def create_team(logic_wrapper):
    name = input("Enter the name of the team: ")
    team = TeamMdl(name = name)
    logic_wrapper.create_team(team)

def create_division(logic_wrapper):
    name = input("Enter the name of the division: ")
    team_ids = []
    add_teams = _yes_or_no("Do you want to add a team? ")
    while add_teams.lower() == "y":
        team_id = input("Enter the id of team: ")
        team_ids.append(team_id)
        add_teams = _yes_or_no("Do you want to add a team? ")
    host_name = input("Enter the name of the host: ")
    phone_nr = input("Enter the phone number of the division: ")
    rounds = input("Enter the number of rounds: ")
    division = DivisionMdl(name = name, team_ids=team_ids, host_name=host_name, phone_nr=phone_nr, rounds=rounds)
    logic_wrapper.create_division(division)

def print_teams(logic_wrapper):
    teams = logic_wrapper.get_all_teams()
    for team in teams:
        print(team)

def print_players(logic_wrapper):
    players = logic_wrapper.get_all_players()
    for player in players:
        print(player)

def print_divisions(logic_wrapper):
    division_id = input("input division id: ")
    try:
        division = logic_wrapper.get_division(division_id)
        print(division)
    except IndexError:
        print("No division with that ID")

def print_matches(logic_wrapper):
    matches = logic_wrapper.get_all_matches()
    for match in matches:
        print(match)
        print("")

def print_clubs(logic_wrapper):
    clubs = logic_wrapper.get_all_clubs()
    for club in clubs:
        print(club)

def _yes_or_no(text):
    y_or_no = input(f"{text} y/n")
    while y_or_no.lower() != "y" and y_or_no.lower() != "n":
        y_or_no = input(f"Invalid input, {text} y/n")
    return y_or_no

def print_all_unplayed_matches(logic_wrapper):
    unplayed_matches = logic_wrapper.get_upcoming_matches()
    for match in unplayed_matches:
        print (match)
        print("")
    
def print_all_played_matches(logic_wrapper):
    played_matches = logic_wrapper.get_concluded_matches()
    for match in played_matches:
        print(match)
        print("")

def get_player(logic_wrapper):
    id = input("Input player ID: ")
    print(logic_wrapper.get_player(id))

#untested

def set_date(logic_wrapper):
    id = input("Input match ID: ")
    new_date = input("Input new date YYYY-MM-DD: ")
    logic_wrapper.set_date(id, new_date)
    print_matches(logic_wrapper)
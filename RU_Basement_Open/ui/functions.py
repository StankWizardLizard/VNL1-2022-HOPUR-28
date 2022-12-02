from models.player_mdl import PlayerMdl
from models.club_mdl import ClubMdl
from models.team_mdl import TeamMdl
from models.division_mdl import DivisionMdl

def generate_table(table_format:list=[["NR", 4], ["Name", 6]], table_data:list=[["", ""]]):
    '''
    Takes in a list of table columns and width of column, and a list of lists with data in those colums,
    then prints a table from those inputs
    '''
    #constants
    EMPTY = ""
    SEPERATOR_DATA = "│"
    SEPERATOR_HEADER = "┬"
    SEPERATOR_BETWEEN = "┼"
    SEPERATOR_FOOTER = "┴"
    END_HEADER = "┐"
    END_BETWEEN = "┤"
    END_FOOTER = "┘"

    #table
    if table_format:
        try:

            #creates lists of lines and header data
            lines = [f"{EMPTY:─^{table_format[i][1]}}" for i in range(len(table_format))]
            header_data_list = [f"{table_format[i][0]:^{table_format[i][1]}}" for i in range(len(table_format))]
        except IndexError:
            print("Error table data incorrect")

        #initial strings that will be printed
        header_data = "│"
        header_top = "┌"
        between = "├"
        footer = "└"

        #converts header data list into a string with headers
        for x in header_data_list:
            header_data = header_data + x + SEPERATOR_DATA
        
        #generates lines for table in string format
        header_top = _generate_lines(header_top, lines, SEPERATOR_HEADER, END_HEADER)
        between = _generate_lines(between, lines, SEPERATOR_BETWEEN, END_BETWEEN)
        footer = _generate_lines(footer, lines, SEPERATOR_FOOTER, END_FOOTER)

        #prints header
        print(header_top)
        print(header_data)
        print(between)

        #prints table_data or an empty table if table_data is empty
        if table_data:
            for j in range(len(table_data)):
                contents_data_list = [f"{table_data[j][i]:^{table_format[i][1]}}" for i in range(len(table_format))]
                contents = "│"
                for e in range(len(contents_data_list)):
                    contents = contents + contents_data_list[e] + SEPERATOR_DATA
                print(contents)
                if j < len(table_data)-1:
                    print(between)
        else:
            contents_data_list = [f"{EMPTY:^{table_format[i][1]}}" for i in range(len(table_format))]
            contents = "│"
            for e in range(len(contents_data_list)):
                contents = contents + contents_data_list[e] + SEPERATOR_DATA
            print(contents)

        #prints footer
        print(footer)
    else:
        print("Error missing table data")

def _generate_lines(string:str, lines:list, seperator:str, end:str):
    '''
    takes in the starting string, a list of line strings, seperator, and end
    then generates a string of lines with for the generate_table function
    '''
    for i  in range(len(lines)):
        if i < len(lines)-1:
            string = string + lines[i] + seperator
        else:
            string = string + lines[i] + end
    return string

def display_menu_options(list_of_displays:list=[], showing_page:int=0):
		'''returns a string listing the available options of the menu'''

		if showing_page == 0:
			if len(list_of_displays) > 1:
				return "(N)ext page, (Q)uit"
			else:
				return "(Q)uit"
		elif showing_page+1 == len(list_of_displays):
			return "(B)ack Page, (Q)uit"
		else:
			return"(N)ext page, (B)ack Page, (Q)uit"

def get_leaderboard(logic_wrapper):
    leaderboard = logic_wrapper.get_leaderboard()
    return leaderboard


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

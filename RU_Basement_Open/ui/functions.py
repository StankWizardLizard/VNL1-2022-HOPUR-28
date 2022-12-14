from models.player_mdl import PlayerMdl
from models.club_mdl import ClubMdl
from models.team_mdl import TeamMdl
from models.division_mdl import DivisionMdl
from datetime import datetime
import string
import re

def generate_table(table_format:list=[["NR", 4], ["Name", 6]], table_data:list=[]):
    '''
    Takes in a list of table columns and width of column, and a list of lists with strings in those colums,
    then prints a table from those strings 
    (can take in list of strings as well if one column in the row has more than one entry)
    example:
    table_format = [[column1 name, column1 width], [column2 name, column2 width]]
    table_data = [["column1 info", "column2 info"], ["column1 info", "column2 info"]...]
    generate_table(table_format, table_data)
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

    # Checks if table_data was provided, if not it just prints an error code
    if table_format:
        try:

            #creates a list of lines for each column (to seperate rows) and header data
            lines = [f"{EMPTY:─^{table_format[i][1]}}" for i in range(len(table_format))]
            header_data_list = [f"{table_format[i][0]:^{table_format[i][1]}}" for i in range(len(table_format))]
        except IndexError:
            print("Error: table format incorrect")

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
        if table_data:
            print(between)  
        else:
            print(footer)    

        #prints table_data or an empty table if table_data is empty
        try:
            if table_data:
                for j in range(len(table_data)):
                    # Checks if row needs to be larger for more than one entry in a column (if column data is given as a list of strings instead of a string)
                    # Sets size of the row (how many lines needed) as the size of the largest list
                    column_size = 1
                    for y in range(len(table_data[j])):
                        if type(table_data[j][y]) is list:
                            if column_size < len(table_data[j][y]):
                                column_size = len(table_data[j][y])
                    middle = column_size // 2
                    for c in range(column_size):
                        contents_data_list = [
                            # If column data is a list that has a c index in that list then it  the c index of that list
                            f"{table_data[j][i][c]:^{table_format[i][1]}}" if type(table_data[j][i]) is list and len(table_data[j][i]) > c 
                            # If column data is a list that doesn't have a c index or is a string and c is not the middle line, it prints nothing at the c column line
                            else f"{EMPTY:^{table_format[i][1]}}" if type(table_data[j][i]) is list and len(table_data[j][i]) <= c or c != middle  
                            # If it's a string, and the row length is normal or it's the approxamitely middle line of the row,
                            else f"{table_data[j][i]:^{table_format[i][1]}}" 
                            for i in range(len(table_format))
                        ]
                        contents = "│"
                        for e in range(len(contents_data_list)):
                            contents = contents + contents_data_list[e] + SEPERATOR_DATA
                        print(contents)
                        if c == column_size-1:
                            if j < len(table_data)-1:
                                print(between)
                #prints footer
                print(footer)
        except TypeError:
            print("Error: wrong data type")

    else:
        print("Error: missing table data")

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

def display_menu_options(how_many_pages:int=1, showing_page:int=0):
		'''returns a string listing the available options of the menu'''

		if showing_page == 0:
			if how_many_pages > 0:
				return "(N)ext page, (Q)uit"
			else:
				return "(Q)uit"
		elif showing_page == how_many_pages:
			return "(B)ack Page, (Q)uit"
		else:
			return"(N)ext page, (B)ack Page, (Q)uit"

def get_leaderboard(logic_wrapper):
    leaderboard = logic_wrapper.get_leaderboard()
    return leaderboard


def remove_punctuation(input_str):
    """Removes all punctuation and whitespaces from a string"""
    input_str = input_str.translate(str.maketrans('', '', string.punctuation)) # Remove punctuation
    input_str = ''.join(input_str.split()) # Remove whitespaces
    return input_str

def get_date_input(display_string: str):
    """Takes a string to display, asks for user input and validates if it is a date
    of format 'YYYY-MM-DD' """
    while True:
        choice = input(display_string).strip()
        try:
            start_date = datetime.strptime(choice, '%Y-%m-%d')
            if start_date < datetime.now():
                print(f"{start_date} has already passed")
                continue
            return choice
        except ValueError:
            print("Invalid input, date should be on format YYYY-MM-DD")

def get_input(display_string: str, number: bool = False, email: bool = False, isInt = False,isStr = False, length=None):
    """Takes a string to display, asks for user input and does basic validation,
    returns input once it's valid"""
    while True:
        valid = True
        error_str = ""
        choice = input(display_string).strip()
        # Remove filler characters and check if the user'sm choice is numeric
        if number:
            choice = remove_punctuation(choice)
            if not choice.isnumeric():
                valid = False
                error_str = " is not a number, try again..."
        # Check whether the user's choice is a valid email
        if email:
            # Email validating regular expression
            regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            if not (re.fullmatch(regex, choice)):
                valid = False
                error_str = " is not a valid email, try again..."
        # Check whether the user's choice is empty
        if choice == "":
            valid = False
            error_str = "Empty input, try again..."
        # Return user's choice if all checks succeded
        
        if isInt:
            try:
                if "." in choice:
                    error_str = "Input must be integer"
                else:
                    return int(choice)
            except ValueError:
                error_str = "Input must be an integer, try again"
                valid = False
                
        if length is not None and valid == True:
            if len(choice) != length:
                valid = False
                error_str = f" is invalid, input must be of lenght {length}"
        if valid:
            return choice
        print(choice + error_str)



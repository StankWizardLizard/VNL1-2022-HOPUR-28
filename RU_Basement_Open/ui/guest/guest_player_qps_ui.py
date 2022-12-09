from ui.menu_frame import MenuFrame
from ui.functions import *
from models.division_mdl import DivisionMdl

class QPSTable(MenuFrame):
    def __init__(self,logic_wrapper, os, division:DivisionMdl = DivisionMdl("Reykjavik Open")):
            super().__init__(logic_wrapper, os)
            self.division = division #  Takes in the division you selected in the list of Divisions
            self.NR_OF_ENTRIES = 20 #  Number of entries displayed per page 

    def display_menu(self, division_leaderboard, showing_page):
        """Creates the format for the division leaderboard table then fills in data from division_leaderboard 
        and feeds it to generate_table function to print a leaderboards table for the divsion"""

        # Constants
        NUMBER = "NR" # Header for "NR" column
        PLAYER_NAME= "Player Name" # Header for "Team Name" column
        Q_PTS = "Quality Pts" # Header for "Wins" column
        NR = 4 # Width of "NR" column
        TN = 40 # Width of "Team Name" column
        WS = 15 # Width of "Wins" column


        #  Format of table with a list of lists containing strings for each column ex. [[column name, column width], [column name, column width]]
        table_format = [[NUMBER, NR], [PLAYER_NAME, TN], [Q_PTS, WS]]
        try:
        
            #  Fills in the list data for table with lists containing data for every row (make sure every row has data for all columns)
            table_data = []
            # Range starts from which page you are viewing times how many entries per page,
            # to which page you are viewing times how many entries per page plus how many entries there are in that page.
            for i in range(
                showing_page*self.NR_OF_ENTRIES,
                showing_page*self.NR_OF_ENTRIES+len(division_leaderboard[showing_page*self.NR_OF_ENTRIES:showing_page*self.NR_OF_ENTRIES+self.NR_OF_ENTRIES])
                ):
                team_nr = str(i + 1+  showing_page * self.NR_OF_ENTRIES) + ")"
                team_name = f'{division_leaderboard[i]["player_name"]}'
                wins = f'{division_leaderboard[i]["result"]}'
                table_data.append([team_nr, team_name, wins])

            # Generates a table with the correct format and data
            # example:
            # table_format = [[column1 name, column1 width], [column2 name, column2 width]]
            # table_data = [["column1 info", "column2 info"], ["column1 info", "column2 info"]...]
            # generate_table(table_format, table_data)
            generate_table(table_format, table_data)
        except IndexError:
            # Generates an empty table if division_leaderboard gives wrong data
            generate_table(table_format, [])

    def prompt_option(self, showing_page:int=0):
        '''Calls the a method to print a table of teh division leaderboard then a method to print menu options, 
        then takes input from the user to choose an option from the list of options printed for the division table'''
        division_leaderboard = self.logic_wrapper.get_player_leaderboard_by_division(self.division.id,"qps")
        pages_number = len(division_leaderboard) // self.NR_OF_ENTRIES
        while True:
            self.clear_menu()
            self.display_menu(division_leaderboard=division_leaderboard, showing_page=showing_page)
            print("press Q to go back: ")
            choice2 = input(" > ")
            choice2 = choice2.lower()

            match choice2:
                #  if user wants to see the next NR_OF_ENTRIES items
                case "n":
                    if showing_page == pages_number:
                        input("Invalid Input!")
                    else:
                        showing_page += 1

                #  if user wants to see the last NR_OF_ENTRIES items
                case "b":
                    if showing_page == 0:
                        input("Invalid Input!")
                    else:
                        showing_page -= 1

                #  if user wants to quit and return to the last page
                case "q":
                    break
                
                #  undocumented inputs get disregarded
                case _:
                    input("Invalid Input!")
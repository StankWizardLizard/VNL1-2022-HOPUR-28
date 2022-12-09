from ui.functions import *
from ui.menu_frame import MenuFrame

class PlayersTableUI(MenuFrame):
    def __init__(self,logic_wrapper, os,team = ""):
        super().__init__(logic_wrapper, os)
        self.NR_OF_ENTRIES = 10
        self.team = team


    def _get_display_menu_sizes(self, list_of_players:list=[], showing_page:int=0):
        '''returns all the size caluclations for "Showing x-y of z players" in display_menu'''

        # The z number for the "Showing x-y of z players"
        all_players_size = len(list_of_players) 

        # The x number for the "Showing x-y of z players"
        showing_players_size_start = 1 + showing_page * self.NR_OF_ENTRIES

        # The y number for the "Showing x-y of z players" 
        showing_players_size_end = showing_players_size_start + len(list_of_players[showing_players_size_start: (showing_page+1) * self.NR_OF_ENTRIES+1])

        return all_players_size, showing_players_size_end, showing_players_size_start


    def display_menu(self, showing_page:int = 0, list_of_players: list= []):
        """Display the menu screen for the players table"""
        """Creates the format for the players table then fills in data from list_of_players 
        and feeds it to generate_table function to print a table for the players"""

        NUMBER = "NR" # Header for the "NR" column
        PLAYER_NAME = "Player Name" # Header for the "Player Name" column
        PN = 40 # Width of "Player Name" column
        NR = 4 # Width of "NR" column

        # Prints "Showing "x-y of z players"
        all_players_size, showing_players_size_end, showing_players_size_start = self._get_display_menu_sizes(list_of_players=list_of_players, showing_page=showing_page)
        print(f"Showing {showing_players_size_start}-{showing_players_size_end} of {all_players_size} players")

        # Format of table with a list of lists containing strings for each column ex. [[column name, column width], [column name, column width]]
        table_format = [[NUMBER, NR], [PLAYER_NAME, PN]]
        try:
        
            # Fills in the list data for table with lists containing data for every row (make sure every row has data for all columns)
            table_data = []
            # Range starts from which page you are viewing times how many entries per page,
            # to which page you are viewing times how many entries per page plus how many entries there are in that page.
            for i in range(showing_page*self.NR_OF_ENTRIES, showing_page*self.NR_OF_ENTRIES+len(list_of_players[showing_page*self.NR_OF_ENTRIES:showing_page*self.NR_OF_ENTRIES+self.NR_OF_ENTRIES])):
                player_nr = str(i+1) + ")"
                player_name = list_of_players[i].name
                if self.team:
                    if self.team.captain_id == list_of_players[i].id :
                        player_name = player_name + "(C)"
                table_data.append([player_nr, player_name])

            # Generates a table with the correct format and data
            # example:
            # table_format = [[column1 name, column1 width], [column2 name, column2 width]]
            # table_data = [["column1 info", "column2 info"], ["column1 info", "column2 info"]...]
            # generate_table(table_format, table_data)
            generate_table(table_format, table_data)
        except IndexError:
            # Generates an empty table if list_of_players gives wrong data
            generate_table(table_format, [])


    def prompt_option(self, showing_page:int = 0):
        '''Calls the a method to print a table of all players then a method to print menu options, 
        then takes input from the user to choose an option from the list of options printed for the players table'''
        if not self.team:
            list_of_players = self.logic_wrapper.get_all_players()
        else:
            list_of_players = []
            team_players = self.logic_wrapper.get_players(self.team.id)
            for x in team_players:
                list_of_players.append(self.logic_wrapper.get_player(x))
        page_numbers = len(list_of_players)//self.NR_OF_ENTRIES

        while True:
            self.clear_menu()
            self.display_menu(showing_page=showing_page, list_of_players=list_of_players)
            print(display_menu_options(showing_page=showing_page, how_many_pages=page_numbers))
            choice = input(" > ")
            choice = choice.lower()

            match choice:
                #  if user wants to see the next self.NR_Of_ENTRIES items
                case "n":
                    if showing_page == page_numbers:
                        input("Invalid Input!")
                    else:
                        showing_page += 1

                #  if user wants to see the last self.NR_OF_ENTRIES items
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
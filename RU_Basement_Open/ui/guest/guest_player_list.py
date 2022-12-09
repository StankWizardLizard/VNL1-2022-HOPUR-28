from ui.menu_frame import MenuFrame
from ui.functions import *
from ui.guest.guest_player_stats_ui import PlayerStats
from models.division_mdl import DivisionMdl
class PlayerList(MenuFrame):
    def __init__(self,logic_wrapper, os, division:DivisionMdl = DivisionMdl("Reykjavik Open")):
            super().__init__(logic_wrapper, os)
            self.division = division
            self.NR_OF_ENTRIES = 1

    def display_menu(self, showing_page:int=0, players_in_div:list=[]):
        """Display the menu screen for the  matches"""

        #Constants
        NUMBER = "NR"
        TEAM_NAME = "Team Name"
        NR = 4 #Length of number box
        TN = 40 #Length of team name box


        #Format rows of table with a list of lists [row name, row width]
        table_format = [[NUMBER, NR], [TEAM_NAME, TN]] 


        try:
            
            #Fills in data for table by with a list of lists containing data for every row
            table_data = []
            for i in range(
                showing_page*self.NR_OF_ENTRIES,
                showing_page*self.NR_OF_ENTRIES+len(players_in_div[showing_page*self.NR_OF_ENTRIES:showing_page*self.NR_OF_ENTRIES+self.NR_OF_ENTRIES])
                ):
                player_nr = str(i + 1) + ")"
                player_name = f"{players_in_div[i].name}"
                table_data.append([player_nr, player_name])

            #Generates a table with the correct format and data
            generate_table(table_format, table_data)
            return players_in_div
        except IndexError:
            generate_table(table_format, [])

    def prompt_option(self, showing_page:int=0):
        '''Prompts the user to choose an option from a list of options for the division table'''
        players_in_div = self.logic_wrapper.get_players_by_division(self.division.id)
        
        pages_number = len(players_in_div) // 10
        while True:
            self.clear_menu()
            self.display_menu(showing_page, players_in_div)
            print(display_menu_options(showing_page=showing_page, how_many_pages=pages_number))
            choice = input(" > ")
            choice = choice.strip().lower()

            match choice:
                case "n":
                    if showing_page == pages_number:
                        input("Invalid Input!")
                    else:
                        showing_page += 1

                # if user wants to see the last NR_OF_ENTRIES items
                case "b":
                    if showing_page == 0:
                        input("Invalid Input!")
                    else:
                        showing_page -= 1

                # if user wants to quit
                case "q":
                    break
                case _:
                    
                    if choice.isnumeric():
                        if int(choice) > len(players_in_div):
                            print("oopsie")
                            continue
                        player_stats = PlayerStats(self.logic_wrapper,self.os,players_in_div[int(choice)-1],self.division)
                        player_stats.prompt_option()
                    else: 
                        input("Invalid Input!")
                # undocumented inputs get disregarded


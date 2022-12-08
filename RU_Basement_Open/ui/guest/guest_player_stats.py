
from ui.menu_frame import MenuFrame
from ui.functions import *
from models.division_mdl import DivisionMdl
class PlayerStats(MenuFrame):
    def __init__(self,logic_wrapper, os, player):
            super().__init__(logic_wrapper, os)
            self.player = player
            self.NR_OF_ENTRIES = 10
    def display_menu(self, division_leaderboard:list=[], showing_page:int=0):
        """Display the menu screen for the  matches"""
        #Constants
        PLAYER_NAME = "Player Name"
        Q_PTS = "Quality Points"
        INN_PTS = "Innbound points"
        OUT_PTS = "Outbount points"
        PN = 40 #Length of team name box
        Q = 15
        I = 15
        O = 15
        #Format rows of table with a list of lists [row name, row width]
        table_format = [[PLAYER_NAME, PN], [Q_PTS, Q],[INN_PTS,I],[OUT_PTS,O]] 
        try:
            
            #Fills in data for table by with a list of lists containing data for every row
            table_data = []
            player_name = f"{self.player.name}"
            quality_pts = f"{}"
            innbound_pts = "{}"
            outbound_pts = "{}"
            table_data.append([player_name,quality_pts,innbound_pts,outbound_pts])
            #Generates a table with the correct format and data
            generate_table(table_format, table_data)
        except IndexError:
            generate_table(table_format, [])
    def prompt_option(self, showing_page:int=0):
        '''Prompts the user to choose an option from a list of options for the division table'''
        while True:

            self.clear_menu()
            self.display_menu()
            choice = input(" > ")
            choice = choice.lower()
            match choice:
                case "q":
                    break
                case _:
                   input("Invalid Input!")
                                # undocumented inputs get disregarded
                                #                  case _:
                                #                      input("Invalid Input!")

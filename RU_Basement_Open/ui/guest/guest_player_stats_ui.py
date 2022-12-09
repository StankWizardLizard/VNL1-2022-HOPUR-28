
from ui.menu_frame import MenuFrame
from ui.functions import *
from models.division_mdl import DivisionMdl
class PlayerStats(MenuFrame):
    def __init__(self,logic_wrapper, os, player,division):
            super().__init__(logic_wrapper, os)
            self.player = player
            self.division = division
            self.NR_OF_ENTRIES = 10
    def display_menu(self,games_past):
        """Display the menu screen for the  matches"""
        #Constants
        PLAYER_NAME = "Player Name"
        Q_PTS = "Quality Points"
        HIGH_PTS = "Highest Shot"
        INN_PTS = "Innbound points"
        OUT_PTS = "Outbound points"
        S_501 = "501 WINS/LOSS/%"
        S_301 = "301 WINS/LOSS/%"
        S_CRICKET = "Cricket WINS/LOSS/%"
        S_QUAD = "Quad WINS/LOSS/%"
        
        PN = 40 #Length of team name box
        Q = 20



        #Format rows of table with a list of lists [row name, row width]
        table_format = [[PLAYER_NAME, PN], [Q_PTS, Q],[HIGH_PTS,Q],[INN_PTS,Q],[OUT_PTS,Q],[S_501,Q],[S_301,Q],[S_CRICKET,Q],[S_QUAD,Q]] 
        try:
            
            #Fills in data for table by with a list of lists containing data for every row
            table_data = []
            player_name = f"{self.player.name}"
            quality_pts = f"{self.logic_wrapper.get_player_total_qps_by_division(self.player.id,self.division.id)}"
            h_s, i_s,o_s = self.logic_wrapper.get_player_highest_shots_by_division(self.player.id,self.division.id,int(games_past))
            highest_shot = f"{h_s}"
            innbound_pts = f"{i_s}"
            outbound_pts = f"{o_s}"
            score_stats = self.logic_wrapper.get_player_statistics_by_division(self.player.id,self.division.id,games_past)
            score_5 = f'{score_stats["score_501"][0]}/{score_stats["score_501"][1]}/{score_stats["score_501"][2]}'
            score_3 = f'{score_stats["score_301"][0]}/{score_stats["score_301"][1]}/{score_stats["score_301"][2]}'
            score_cri = f'{score_stats["score_cricket"][0]}/{score_stats["score_cricket"][1]}/{score_stats["score_cricket"][2]}'
            score_5_q = f'{score_stats["score_501_quad"][0]}/{score_stats["score_501_quad"][1]}/{score_stats["score_501_quad"][2]}'
            table_data.append([player_name,quality_pts,highest_shot,innbound_pts,outbound_pts,score_5,score_3,score_cri,score_5_q])
            #Generates a table with the correct format and data
            generate_table(table_format, table_data)
            return None
        except IndexError:
            games_past = input("Matches exeeds played by player Try again (Q to quit): ")
            try:
                self.display_menu(games_past)
            except (ValueError,IndexError):
                if games_past.lower() == "q":
                    return "Quit"
                else:
                    games_past = input("Input must be an integer try again (Q to quit):")
                    if games_past.lower() == "q":
                        return "Quit"
                    self.display_menu(games_past)
    def prompt_option(self, showing_page:int=0):
        '''Prompts the user to choose an option from a list of options for the division table'''
        while True:

            self.clear_menu()
            try:
                games_past = input("Enter how many games in the past (Press enter for since beginning, Press Q to go back)")
                
                self.clear_menu()
                quit_str =self.display_menu(games_past)
            except ValueError:
                if games_past.lower() == "q":
                    break
                print("Number must be integer")
                continue
            if quit_str == "Quit":
                break
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

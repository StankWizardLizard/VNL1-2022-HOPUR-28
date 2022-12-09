from ui.menu_frame import MenuFrame
from ui.functions import *
from ui.guest.guest_player_stats_ui import PlayerStats
from models.division_mdl import DivisionMdl
class PlayerList(MenuFrame):
    def __init__(self,logic_wrapper, os, division:DivisionMdl = DivisionMdl("Reykjavik Open")):
            super().__init__(logic_wrapper, os)
            self.division = division
            self.NR_OF_ENTRIES = 10

    def display_menu(self, showing_page:int=0):
        """Display the menu screen for the  matches"""

        #Constants
        NUMBER = "NR"
        TEAM_NAME = "Team Name"
        NR = 4 #Length of number box
        TN = 40 #Length of team name box

        print(self.division.name)

        #Format rows of table with a list of lists [row name, row width]
        table_format = [[NUMBER, NR], [TEAM_NAME, TN]] 
        players_in_div = []
        all_teams = self.logic_wrapper.get_all_teams()
        for team_id in self.division.team_ids:
            for team in all_teams:
                if team_id == team.id:
                    for player in team.player_ids:
                        players_in_div.append(self.logic_wrapper.get_player(player))

        try:
            
            #Fills in data for table by with a list of lists containing data for every row
            table_data = []
            for i in range(
                showing_page*self.NR_OF_ENTRIES,
                showing_page*self.NR_OF_ENTRIES+len(players_in_div[showing_page*self.NR_OF_ENTRIES:showing_page*self.NR_OF_ENTRIES+self.NR_OF_ENTRIES])
                ):
                player_nr = str(i + 1+  showing_page * self.NR_OF_ENTRIES) + ")"
                player_name = f"{players_in_div[i].name}"
                table_data.append([player_nr, player_name])

            #Generates a table with the correct format and data
            generate_table(table_format, table_data)
            return players_in_div
        except IndexError:
            generate_table(table_format, [])

    def prompt_option(self, showing_page:int=0):
        '''Prompts the user to choose an option from a list of options for the division table'''
        division_leaderboard = self.logic_wrapper.get_leaderboard(self.division)
        pages_number = len(division_leaderboard) // 2
        while True:
            self.clear_menu()
            players_in_div = self.display_menu()
            print(display_menu_options(showing_page=showing_page, how_many_pages=pages_number))
            choice = input(" > ")
            choice = choice.lower()

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
                        player_stats = PlayerStats(self.logic_wrapper,self.os,players_in_div[int(choice)-1],self.division)
                        player_stats.prompt_option()
                    else: 
                        input("Invalid Input!")
                # undocumented inputs get disregarded

'''
print("Divisions")
print("┌────┬──────────────────────────────────────┬──────┬──────┬──────────┐")
print("│ NR │ Team Name                            │ Wins │ Loss │ Legs won │")
print("├────┼──────────────────────────────────────┼──────┼──────┼──────────┤")
print("│100)│ Team Name 1                          │ 1    │ 2    │ 2        │")
print("├────┼──────────────────────────────────────┼──────┼──────┼──────────┤")
print("│100)│ Team Name 1                          │ 1    │ 2    │ 2        │")
print("├────┼──────────────────────────────────────┼──────┼──────┼──────────┤")
print("│100)│ Team Name 1                      	   │ 1    │ 2    │ 2        │")
print("├────┼──────────────────────────────────────┼──────┼──────┼──────────┤")
print("│100)│ Team Name 1                          │ 1    │ 2    │ 2        │")
print("├────┼──────────────────────────────────────┼──────┼──────┼──────────┤")
print("│100)│ Team Name 1                          │ 1    │ 2    │ 2        │")
print("├────┼──────────────────────────────────────┼──────┼──────┼──────────┤")
print("│100)│ Team Name 1                          │ 1    │ 2    │ 2        │")
print("├────┼──────────────────────────────────────┼──────┼──────┼──────────┤")
print("│100)│ Team Name 1                          │ 1    │ 2    │ 2        │")
print("├────┼──────────────────────────────────────┼──────┼──────┼──────────┤")
print("│100)│ Team Name 1                          │ 1    │ 2    │ 2        │")
print("├────┼──────────────────────────────────────┼──────┼──────┼──────────┤")
print("│100)│ Team Name 1                          │ 1    │ 2    │ 2        │")
print("├────┼──────────────────────────────────────┼──────┼──────┼──────────┤")
print("│100)│ Team Name 1                          │ 1    │ 2    │ 2        │")
print("└────┴──────────────────────────────────────┴──────┴──────┴──────────┘")
print("(N)ext page, (B)ack Page, (Q)uit or Team Number")
'''
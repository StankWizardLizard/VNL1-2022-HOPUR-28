from ui.menu_frame import MenuFrame
from ui.functions import *
from models.division_mdl import DivisionMdl

class DivisionTableUI(MenuFrame):
	def __init__(self,logic_wrapper, os, division:DivisionMdl = DivisionMdl("Reykjavik Open")):
			super().__init__(logic_wrapper, os)
			self.division = division
			self.NR_OF_ENTRIES = 10

	def display_menu(self, division_leaderboard:list=[], showing_page:int=0):
		"""Display the menu screen for the  matches"""

		#Constants
		NUMBER = "NR"
		TEAM_NAME = "Team Name"
		WINS = "Wins"
		LOSS = "Loss"
		LEGS_WON = "Legs Won"
		NR = 4 #Length of number box
		TN = 40 #Length of team name box
		WL = 6 #Length of wins/loss box
		LW = 10 #Length oflegs won box

		print(self.division.name)

		#Format rows of table with a list of lists [row name, row width]
		table_format = [[NUMBER, NR], [TEAM_NAME, TN], [WINS, WL], [LOSS, WL], [LEGS_WON, LW]]
		try:
			
			#Fills in data for table by with a list of lists containing data for every row
			table_data = []
			for i in range(
				showing_page*self.NR_OF_ENTRIES,
				showing_page*self.NR_OF_ENTRIES+len(division_leaderboard[showing_page*self.NR_OF_ENTRIES:showing_page*self.NR_OF_ENTRIES+self.NR_OF_ENTRIES])
				):
				team_nr = str(i + 1+  showing_page * self.NR_OF_ENTRIES) + ")"
				team_name = f"{division_leaderboard[i][0]}"
				wins = f"{division_leaderboard[i][1]}"
				loss = f"{division_leaderboard[i][2]}"
				legs_won = str(division_leaderboard[i][3])
				table_data.append([team_nr, team_name, wins, loss, legs_won])

			#Generates a table with the correct format and data
			generate_table(table_format, table_data)
		except IndexError:
			generate_table(table_format, [])

	def prompt_option(self, showing_page:int=0):
		'''Prompts the user to choose an option from a list of options for the division table'''
		division_leaderboard = self.logic_wrapper.get_leaderboard(self.division)
		pages_number = len(division_leaderboard) // 2
		while True:
			self.clear_menu()
			self.display_menu()
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

				# undocumented inputs get disregarded
				case _:
					input("Invalid Input!")

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
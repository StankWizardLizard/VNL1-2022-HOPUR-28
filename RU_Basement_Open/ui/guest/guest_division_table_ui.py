from ui.menu_frame import MenuFrame
from ui.functions import *
from models.division_mdl import DivisionMdl

class DivisionTableUI(MenuFrame):
	def __init__(self,logic_wrapper, os, division:DivisionMdl = DivisionMdl("Reykjavik Open")):
			super().__init__(logic_wrapper, os)
			self.division = division #  Takes in the division you selected in the list of Divisions
			self.NR_OF_ENTRIES = 20 #  Number of entries displayed per page 

	def display_menu(self, division_leaderboard:list=[], showing_page:int=0):
		"""Creates the format for the division leaderboard table then fills in data from division_leaderboard 
		and feeds it to generate_table function to print a leaderboards table for the divsion"""

		# Constants
		NUMBER = "NR" # Header for "NR" column
		TEAM_NAME = "Team Name" # Header for "Team Name" column
		WINS = "Wins" # Header for "Wins" column
		LOSS = "Losses" # Header for "Losses" column
		LEGS_WON = "Legs Won" # Header for "Legs Won" column
		NR = 4 # Width of "NR" column
		TN = 40 # Width of "Team Name" column
		WS = 6 # Width of "Wins" column
		LS = 8 # Width of "Losses" column
		LW = 10 # Width of "Legs Won" column

		print(self.division.name)

		#  Format of table with a list of lists containing strings for each column ex. [[column name, column width], [column name, column width]]
		table_format = [[NUMBER, NR], [TEAM_NAME, TN], [WINS, WS], [LOSS, LS], [LEGS_WON, LW]]
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
				team_name = f"{division_leaderboard[i][0]}"
				wins = f"{division_leaderboard[i][1]}"
				loss = f"{division_leaderboard[i][2]}"
				legs_won = f"{division_leaderboard[i][3]}"
				table_data.append([team_nr, team_name, wins, loss, legs_won])

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
		division_leaderboard = self.logic_wrapper.get_leaderboard(self.division)
		pages_number = len(division_leaderboard) // self.NR_OF_ENTRIES
		while True:
			self.clear_menu()
			self.display_menu(division_leaderboard=division_leaderboard, showing_page=showing_page)
			print(display_menu_options(showing_page=showing_page, how_many_pages=pages_number))
			choice = input(" > ")
			choice = choice.strip().lower()

			match choice:
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
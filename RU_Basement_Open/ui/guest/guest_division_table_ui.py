from ui.menu_frame import MenuFrame
from ui.functions import *

class DivisionTableUI(MenuFrame):
	def __init__(self,logic_wrapper, os):
			super().__init__(logic_wrapper, os)

	def _get_division_leaderboard_in_correct_format(self):
		division_leaderboard = get_leaderboard(self.logic_wrapper)
		new_leaderboard = []
		if len(division_leaderboard) > 10:
			for i in range(0, (len(division_leaderboard)//10)):
				division_page = []
				for e in range(i*10, i*10+10):
					division_page.append(division_leaderboard[e])
				if len(division_leaderboard) % 10 != 0:
					division_page = []
					for x in division_leaderboard[len(division_leaderboard)-len(division_leaderboard) % 10:]:
						division_page.append(x)
				new_leaderboard.append(division_page)
		else:
			division_page = []
			for x in division_leaderboard:
				division_page.append([x])
			new_leaderboard.append(division_page)
		return new_leaderboard
	def display_menu(self, division_leaderboard:list=[], showing_page:int=0):
		"""Display the menu screen for the  matches"""
		NUMBER = "NR"
		TEAM_NAME = "Team Name"
		WINS = "Wins"
		LOSS = "Loss"
		LEGS_WON = "Legs Won"
		NR = 4 #Length of number box
		TN = 40 #Length of team name box
		WL = 6 #Length of wins/loss box
		LW = 10 #Length oflegs won box

		print("Division")

		#Format of table with a list of lists [row name, row width]
		table_format = [[NUMBER, NR], [TEAM_NAME, TN], [WINS, WL], [LOSS, WL], [LEGS_WON, LW]]
		try:
			
			#Fills in data for table 
			table_data = []
			for i in range(len(division_leaderboard[showing_page])):
				team_nr = str(i + showing_page * 10) + ")"
				team_name = f"{division_leaderboard[showing_page][i][0]}"
				wins = f"{division_leaderboard[showing_page][i][1]}"
				loss = f"{division_leaderboard[showing_page][i][2]}"
				legs_won = str(division_leaderboard[showing_page][i][3])
				table_data.append([team_nr, team_name, wins, loss, legs_won])

			#Generates a table with the correct format and data
			generate_table(table_format, table_data)
		except IndexError:
			generate_table(table_format, [])

	def prompt_option(self, division_id:str="", showing_page:int=0):
		'''Prompts the user to choose an option from a list of options for the division table'''
		'''division_leaderboard = self._get_division_leaderboard_in_correct_format()'''
		division_leaderboard = [["1"]]
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

				# if user wants to see the last 10 items
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
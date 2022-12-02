from ui.menu_frame import MenuFrame
from ui.functions import *

class DivisionsTableUI(MenuFrame):
	def __init__(self,logic_wrapper, os):
			super().__init__(logic_wrapper, os)

	def display_menu(self, list_of_division:list=[], showing_page:int=0):
		"""Display the menu screen for the  matches"""
		EMPTY = "" 
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

		#Table header
		print(f"┌{EMPTY:─^{NR}}┬{EMPTY:─^{TN}}┬{EMPTY:─^{WL}}┬{EMPTY:─^{WL}}┬{EMPTY:─^{LW}}┐")
		print(f"│{NUMBER:^{NR}}│{TEAM_NAME:^{TN}}│{WINS:^{WL}}│{LOSS:^{WL}}│{LEGS_WON:^{LW}}│")
		print(f"├{EMPTY:─^{NR}}┼{EMPTY:─^{TN}}┼{EMPTY:─^{WL}}┼{EMPTY:─^{WL}}┼{EMPTY:─^{LW}}┤")

		#Table contents
		try:
			for i in range(len(list_of_division[showing_page])):
				team_nr = str(i + showing_page * 10) + ")"
				team_name = f"{list_of_division[showing_page][i][0]}"
				wins = f"{list_of_division[showing_page][i][1]}"
				loss = f"{list_of_division[showing_page][i][2]}"
				legs_won = str(list_of_division[showing_page][i][3])
				print(f"│{team_nr:^4}│{team_name:^{TN}}│{wins:^{WL}}│{loss:^{WL}}│{legs_won:^{LW}}│")
		except IndexError:
			print(f"│{EMPTY:^4}│{EMPTY:^{TN}}│{EMPTY:^{WL}}│{EMPTY:^{WL}}│{EMPTY:^{LW}}│")

		#Table footer
		print(f"└{EMPTY:─^{NR}}┴{EMPTY:─^{TN}}┴{EMPTY:─^{WL}}┴{EMPTY:─^{WL}}┴{EMPTY:─^{LW}}┘")

	def prompt_option(self, division_id:str="", showing_page:int=0):
		list_of_division = get_division(self.logic_wrapper, division_id=division_id)
		while True:
			self.clear_menu()
			self.display_menu()
			choice = input(" > ")
			choice = choice.lower()

			match choice:
				case "n":
					if showing_page+1 == len(list_of_division):
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
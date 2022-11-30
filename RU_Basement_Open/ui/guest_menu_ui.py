from ui.unplayed_matches_ui import UnplayedMatchesUI 
from ui.divisions_table_ui import DivisionsTableUI
from ui.matches_ui import MatchesUI
from ui.teams_ui import TeamsUI

class GuestMenuUI:
	def __init__(self, logic_wrapper, os):
		self.status = "Guest"
		self.logic_wrapper = logic_wrapper
		self.os = os


	def clear_menu(self):
		"""Clears the menu screen"""
		if(self.os.name == "nt"):
			self.os.system("cls")
		else:
			self.os.system("clear")


	def display_menu(self):
		"""Displays the menu screen for the guest"""
	
		print(f"Logged in as {self.status}")
		print("┌─────────────────────┐")
		print("│1) Show Teams        │")
		print("│2) Unplayed Matches  │")
		print("│3) Results           │")
		print("│4) Division Table    │")
		print("│                     │")
		print("│q) Log out           │")
		print("└─────────────────────┘")


	def prompt_option(self):
		"""Prompts the user to choose an option from a list of options"""
	
		while True:
			# Display the menu and prompt the user for a choice
			self.clear_menu()
			self.display_menu()
			choice = input(" > ")
			choice = choice.lower()
			
			match choice:
				# if user wants to show teams
				case "1":
					teams_ui = TeamsUI(self.logic_wrapper, self.os)
					teams_ui.prompt_option()

				# if user wants to show unplayed matches
				case "2":
					unplayed_matches = UnplayedMatchesUI(self.logic_wrapper, self.os)
					unplayed_matches.prompt_option()
					#unplayed_matches.prompt_option()

				# if user wants to show game results
				case "3":
					matches = MatchesUI(self.logic_wrapper, self.os)
					matches.prompt_option()

				# if user wants to show division table
				case "4":
					division_ui = DivisionsTableUI(self.logic_wrapper, self.os)
					division_ui.prompt_option()

				# if user wants to quit session
				case "q":
					break

				# undocumented inputs get disregarded
				case _:
					input("Invalid Input!")

from ui.guest.guest_divisions_table_ui import DivisionsTableUI
from ui.guest.guest_matches_table_ui import MatchesTableUI
from ui.guest.guest_teams_table_ui import TeamsTableUI

from ui.captain.captain_match_table_ui import CaptainMatchesTableUI

from ui.menu_frame import MenuFrame

class CaptainMenuUI(MenuFrame):
	def __init__(self, logic_wrapper, os):
		super().__init__(logic_wrapper, os)
		self.status = "Captain"
		
	
	def display_menu(self):
		"""Displays the menu for the captain"""
		
		print(f"Logged in as {self.status}")
		print("┌─────────────────────────┐")
		print("│1) Show Teams            │")
		print("│2) All Unplayed Matches  │")
		print("│3) All Match Results     │")
		print("│4) Divisions Stats       │")
		print("│5) Edit Matches          │")
		print("│                         │")
		print("│q) Log out               │")
		print("└─────────────────────────┘")


	def prompt_option(self):
		"""Prompts the user to choose option from a list of options"""

		while True:
			# Display the menu and prompt the user for a choice
			self.clear_menu()
			self.display_menu()
	
			choice = input(" > ")
			choice = choice.strip().lower()
			match choice:
				# if user wants to show teams
				case "1":
					teams_table_ui = TeamsTableUI(self.logic_wrapper, self.os)
					teams_table_ui.prompt_option()

				# if user wants to show unplayed matches
				case "2":
					unplayed_matches = MatchesTableUI(self.logic_wrapper, self.os, False)
					unplayed_matches.prompt_option()

				# if user wants to show game results
				case "3":
					matches_table_ui = MatchesTableUI(self.logic_wrapper, self.os, True)
					matches_table_ui.prompt_option()

				# if user wants to show division table
				case "4":
					division_table_ui = DivisionsTableUI(self.logic_wrapper, self.os)
					division_table_ui.prompt_option()

				# if the user wants view table of matches to edit
				case "5":
					matches_table_ui = CaptainMatchesTableUI(self.logic_wrapper, self.os, False)
					matches_table_ui.prompt_option()

				# if user wants to quit session
				case "q":
					break
				
				# undocumented inputs get disregarded
				case _:
					input("Invalid Input!")

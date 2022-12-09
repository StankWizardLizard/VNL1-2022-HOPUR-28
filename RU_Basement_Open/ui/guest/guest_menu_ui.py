from ui.guest.guest_divisions_table_ui import DivisionsTableUI
from ui.guest.guest_matches_table_ui import MatchesTableUI
from ui.guest.guest_players_table_ui import PlayersTableUI
from ui.guest.guest_teams_table_ui import TeamsTableUI
from ui.guest.guest_division_stats_ui import DivisionStatsUI

from ui.menu_frame import MenuFrame

class GuestMenuUI(MenuFrame):
	def __init__(self,logic_wrapper, os):
		super().__init__(logic_wrapper, os)
		self.status = "Guest"


	def display_menu(self):
		"""Displays the menu screen for the guest"""
	
		print(f"Logged in as {self.status}")
		print("┌─────────────────────┐")
		print("│1) Show Teams        │")
		print("│2) Unplayed Matches  │")
		print("│3) Match Results     │")
		print("│4) Division Stats    │")
		print("│                     │")
		print("│q) Log out           │")
		print("└─────────────────────┘")


	def prompt_option(self):
		"""Prompts the user to choose an option from a list of options"""
	
		while True:
			# Display the menu and prompt the user for a choice
			self.clear_menu()
			self.clear_menu()
			self.display_menu()
			choice = input(" > ")
			choice = choice.lower()
			
			match choice:
				# if user wants to show teams
				case "1":
					team_table_ui = TeamsTableUI(self.logic_wrapper, self.os)
					team_table_ui.prompt_option()

				# if user wants to show unplayed matches
				case "2":
					match_table_ui = MatchesTableUI(self.logic_wrapper, self.os, False)
					match_table_ui.prompt_option()

				# if user wants to show game results
				case "3":
					match_table_ui = MatchesTableUI(self.logic_wrapper, self.os)
					match_table_ui.prompt_option()

				# if user wants to show division table
				case "4":
					division_table_ui = DivisionsTableUI(self.logic_wrapper, self.os)
					division_table_ui.prompt_option()

				case "5":
					players_table_ui = PlayersTableUI(self.logic_wrapper, self.os)
					players_table_ui.prompt_option()

				# if user wants to quit session
				case "q":
					break

				# undocumented inputs get disregarded
				case _:
					input("Invalid Input!")


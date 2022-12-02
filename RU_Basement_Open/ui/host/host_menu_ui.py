from ui.guest.guest_division_table_ui import DivisionsTableUI
from ui.guest.guest_matches_table_ui import MatchesTableUI
from ui.guest.guest_teams_table_ui import TeamsTableUI

from ui.host.host_divisions_ui import DivisionsUI
from ui.host.host_players_ui import PlayersUI
from ui.host.host_clubs_ui import ClubsUI
from ui.host.host_teams_ui import TeamsUI

from ui.menu_frame import MenuFrame

class HostMenuUI(MenuFrame):
	def __init__(self, logic_wrapper, os):
		super().__init__(logic_wrapper, os)
		self.status = "Host"
		

	def display_menu(self):
		"""Displays the menu for the host"""
		
		print(f"Logged in as {self.status}")
		print("┌──────────────────────┐")
		print("│1) Show Teams         │")
		print("│2) Unplayed Matches   │")
		print("│3) Match Results      │")
		print("│4) Divisions Table    │")
		print("│5) Players            │")
		print("│6) Teams              │")
		print("│7) Clubs              │")
		print("│8) Divisions          │")
		print("│                      │")
		print("│q) Log out            │")
		print("└──────────────────────┘")


	def prompt_option(self):
		"""Prompts the user to choose an option from list of options"""

		while True:
			# Display the menu and prompt the user for a choice
			self.clear_menu()
			self.display_menu()
			choice = input(" > ")
			choice = choice.lower()

			match choice:
				# if user wants to show teams
				case "1":
					teams_ui = TeamsTableUI(self.logic_wrapper, self.os)
					teams_ui.prompt_option()

				# if user wants to show unplayed matches
				case "2":
					unplayed_matches = MatchesTableUI(self.logic_wrapper, self.os, False)
					unplayed_matches.prompt_option()

				# if user wants to show game results
				case "3":
					matches = MatchesTableUI(self.logic_wrapper, self.os)
					matches.prompt_option()

				# if user wants to show division table
				case "4":
					division_ui = DivisionsTableUI(self.logic_wrapper, self.os)
					division_ui.prompt_option()

				# if user wants to create / edit Players
				case "5":
					players_ui = PlayersUI(self.logic_wrapper, self.os)
					players_ui.prompt_option()

				# if user wants to create / edit Teams
				case "6":
					teams_ui = TeamsUI(self.logic_wrapper, self.os)
					teams_ui.prompt_option()
						
				# if user wants to create / edit Clubs
				case "7":
					clubs_ui = ClubsUI(self.logic_wrapper, self.os)
					clubs_ui.prompt_option()
						
				# if user wants to create / edit Divisions
				case "8":
					divisions_ui = DivisionsUI(self.logic_wrapper, self.os)
					divisions_ui.prompt_option()

				# if user wants to quit session
				case "q":
					break

				# undocumented inputs get disregarded
				case _:
					input("Invalid Input!")


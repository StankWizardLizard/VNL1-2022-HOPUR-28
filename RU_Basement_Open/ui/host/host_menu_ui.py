from ui.guest.guest_matches_unplayed_ui import UnplayedMatchesUI 
from ui.guest.guest_division_ui import DivisionsTableUI
from ui.guest.guest_menu_ui import GuestMenuUI
from ui.guest.guest_matches import MatchesUI
from ui.guest.guest_teams_ui import TeamsUI

from ui.host.host_divisions_ui import DivisionsUI
from ui.host.host_clubs_ui import ClubsUI

class HostMenuUI(GuestMenuUI):
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
		print("│5) Clubs              │")
		print("│6) Divisions          │")
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
					teams_ui = TeamsUI(self.logic_wrapper, self.os)
					teams_ui.prompt_option()

				# if user wants to show unplayed matches
				case "2":
					unplayed_matches = UnplayedMatchesUI(self.logic_wrapper, self.os)
					unplayed_matches.prompt_option()

				# if user wants to show game results
				case "3":
					matches = MatchesUI(self.logic_wrapper, self.os)
					matches.prompt_option()

				# if user wants to show division table
				case "4":
					division_ui = DivisionsTableUI(self.logic_wrapper, self.os)
					division_ui.prompt_option()
	
				# if user wants to create / edit Clubs
				case "5":
					clubs = ClubsUI(self.logic_wrapper, self.os)
					clubs.prompt_option()
						
				# if user wants to create / edit Divisions
				case "6":
					divisions = DivisionsUI(self.logic_wrapper, self.os)
					divisions.prompt_option()

				# if user wants to quit session
				case "q":
					break

				# undocumented inputs get disregarded
				case _:
					input("Invalid Input!")


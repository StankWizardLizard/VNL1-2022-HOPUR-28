from ui.guest.guest_divisions_table_ui import DivisionsTableUI
from ui.guest.guest_matches_table_ui import MatchesTableUI
from ui.guest.guest_teams_table_ui import TeamsTableUI
from ui.host.host_clubs_create_ui import CreateClubUI

from ui.host.host_divisions_ui import DivisionsUI
from ui.host.host_players_create_ui import CreatePlayerUI
from ui.host.host_teams_create_ui import CreateTeamUI


from ui.captain.captain_match_table_ui import CaptainMatchesTableUI

from ui.menu_frame import MenuFrame

class HostMenuUI(MenuFrame):
	def __init__(self, logic_wrapper, os):
		super().__init__(logic_wrapper, os)
		self.status = "Host"
		

	def display_menu(self):
		"""Displays the menu for the host"""
		
		print(f"Logged in as {self.status}")
		print("┌──────────────────────────┐")
		print("│1) Show Teams             │")
		print("│2) All Unplayed Matches   │")
		print("│3) All Match Results      │")
		print("│4) Divisions Stats        │")
		print("│5) Create Players         │")
		print("│6) Create Teams           │")
		print("│7) Create Clubs           │")
		print("│8) Edit Divisions         │")
		print("│9) Edit Matches           │")
		print("│                          │")
		print("│q) Log out                │")
		print("└──────────────────────────┘")


	def prompt_option(self):
		"""Prompts the user to choose an option from list of options"""

		while True:
			# Display the menu and prompt the user for a choice
			self.clear_menu()
			self.display_menu()
			choice = input(" > ")
			choice = choice.strip().lower()

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
					create_club_ui = CreatePlayerUI(self.logic_wrapper, self.os)
					create_club_ui.prompt_option()

				# if user wants to create / edit Teams
				case "6":
					create_team_ui = CreateTeamUI(self.logic_wrapper, self.os)
					create_team_ui.prompt_option()
						
				# if user wants to create / edit Clubs
				case "7":
					create_club_ui = CreateClubUI(self.logic_wrapper, self.os)
					create_club_ui.prompt_option()
						
				# if user wants to create / edit Divisions
				case "8":
					divisions_ui = DivisionsUI(self.logic_wrapper, self.os)
					divisions_ui.prompt_option()

				case "9":
					match_table_ui = CaptainMatchesTableUI(self.logic_wrapper, self.os, True)
					match_table_ui.prompt_option()

				# if user wants to quit session
				case "q":
					break

				# undocumented inputs get disregarded
				case _:
					input("Invalid Input!")


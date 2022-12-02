from ui.host.host_teams_create_ui import CreateTeamUI
from ui.host.host_teams_edit_ui import EditTeamUI

from ui.menu_frame import MenuFrame

class TeamsUI(MenuFrame):
	def __init__(self, logic_wrapper, os):
		super().__init__(logic_wrapper, os)


	def display_menu(self):
		"""Display the the menu screen onto the terminal"""
		print("Teams")
		print("┌──────────────────────────────────┐")
		print("│  1) Create New Team              │")
		print("│  2) Edit Team                    │")
		print("│                                  │")
		print("│  q) Quit                         │")
		print("└──────────────────────────────────┘")


	def prompt_option(self):
		"""Prompts the user to choose an option from a list of options for the match table"""
		while True:
			self.clear_menu()
			self.display_menu()
			choice = input(" > ")
			choice = choice.lower()

			match choice:
				# if user wants to create a new club
				case "1":
					create_team_ui = CreateTeamUI(self.logic_wrapper, self.os)
					create_team_ui.prompt_option()

				# if user wants to edit clubs
				case "2":
					edit_team_ui = EditTeamUI(self.logic_wrapper, self.os)
					edit_team_ui.prompt_option()
					
				# if user wants to quit
				case "q":
					break

				# undocumented inputs get disregarded
				case _:
					input("Invalid Input!")

from ui.host.host_players_create_ui import CreatePlayerUI
from ui.host.host_players_edit import EditPlayerUI

from ui.menu_frame import MenuFrame

class PlayersUI(MenuFrame):
	def __init__(self, logic_wrapper, os):
		super().__init__(logic_wrapper, os)


	def display_menu(self):
		"""Display the the menu screen onto the terminal"""
		print("Players")
		print("┌──────────────────────────────────┐")
		print("│  1) Create New Player            │")
		print("│  2) Edit Player                  │")
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
					create_club_ui = CreatePlayerUI(self.logic_wrapper, self.os)
					create_club_ui.prompt_option()

				# if user wants to edit clubs
				case "2":
					edit_club_ui = EditPlayerUI(self.logic_wrapper, self.os)
					edit_club_ui.prompt_option()
					
				# if user wants to quit
				case "q":
					break

				# undocumented inputs get disregarded
				case _:
					input("Invalid Input!")

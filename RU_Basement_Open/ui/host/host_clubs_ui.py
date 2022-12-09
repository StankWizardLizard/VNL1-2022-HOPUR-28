from ui.host.host_clubs_create_ui import CreateClubUI
from ui.host.host_clubs_edit_ui import EditClubUI

from ui.menu_frame import MenuFrame

class ClubsUI(MenuFrame):
	def __init__(self, logic_wrapper, os):
		super().__init__(logic_wrapper, os)


	def display_menu(self):
		"""Display the the menu screen onto the terminal"""
		print("Clubs")
		print("┌──────────────────────────────────┐")
		print("│  1) Create New Club              │")
		print("│  2) Edit Club                    │")
		print("│                                  │")
		print("│  q) Quit                         │")
		print("└──────────────────────────────────┘")


	def prompt_option(self):
		"""Prompts the user to choose an option from a list of options for the match table"""
		while True:
			self.clear_menu()
			self.display_menu()
			choice = input(" > ")
			choice = choice.strip().lower()

			match choice:
				# if user wants to create a new club
				case "1":
					create_club_ui = CreateClubUI(self.logic_wrapper, self.os)
					create_club_ui.prompt_option()

				# if user wants to edit clubs
				case "2":
					edit_club_ui = EditClubUI(self.logic_wrapper, self.os)
					edit_club_ui.prompt_option()
					
				# if user wants to quit
				case "q":
					break

				# undocumented inputs get disregarded
				case _:
					input("Invalid Input!")

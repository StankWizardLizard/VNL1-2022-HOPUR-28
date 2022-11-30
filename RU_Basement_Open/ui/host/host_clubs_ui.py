from ui.host.host_create_club_ui import CreateClubUI
from ui.host.host_edit_club_ui import EditClubUI

class ClubsUI:
	def __init__(self, logic_wrapper, os):
		self.logic_wrapper = logic_wrapper
		self.os = os


	def clear_menu(self):
		"""Clears the menu screen"""
		if(self.os.name == "nt"):
			self.os.system("cls")
		else:
			self.os.system("clear")


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
			choice = choice.lower()

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

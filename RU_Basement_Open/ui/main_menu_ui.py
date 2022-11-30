from logic.logic_wrapper import LogicWrapper

from ui.captain.captain_menu_ui import CaptainMenuUI
from ui.host.host_menu_ui import HostMenuUI
from ui.guest.guest_menu_ui import GuestMenuUI 

import os

class MainMenuUI:
	def __init__(self):
		self.logic_wrapper = LogicWrapper()


	def clear_menu(self):
		"""Clears the menu screen """
		if(os.name == "nt"):
			os.system("cls")
		else:
			os.system("clear")


	def display_menu(self):
		"""Displays the menu screen upon starting the program"""

		print("Login as")
		print("┌────────────┐")
		print("│1) Host     │")
		print("│2) Captain  │")
		print("│3) Guest    │")
		print("│            │")
		print("│q) Quit     │")
		print("└────────────┘")


	def prompt_login(self):
		"""Prompts the user to choose a login option"""

		while True:
			# Display the menu and prompt the user for a choice
			self.clear_menu()
			self.display_menu()		
			choice = input(" > ")
			choice = choice.lower()

			match choice:

				# If user picks host
				case "1":
					host = HostMenuUI(self.logic_wrapper, os)
					host.prompt_option()
				
				# if user picks captain
				case "2":
					captain = CaptainMenuUI(self.logic_wrapper, os)
					captain.prompt_option()
				
				# if user picks guest
				case "3":
					guest = GuestMenuUI(self.logic_wrapper, os)
					guest.prompt_option()
	
	
				# if user wants to quit session
				case "q":
					break

				# undocumented inputs get disregarded
				case _:
					input("Invalid Input!")

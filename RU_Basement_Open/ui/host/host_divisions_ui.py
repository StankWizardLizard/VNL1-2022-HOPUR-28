from ui.host.host_create_divisions_ui import CreateDivisionsUI
from ui.host.host_edit_divisions_ui import EditDivisionsUI

class DivisionsUI:
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
		print("Divisions")
		print("┌──────────────────────────────────┐")
		print("│  1) Create Division              │")
		print("│  2) Edit Division                │")
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
				# if user wants to see the next 10 items
				case "1":
					create_divisions_ui = CreateDivisionsUI(self.logic_wrapper, self.os)
					create_divisions_ui.prompt_option()
					
				# if user wants to see the last 10 items
				case "2":
					edit_divisions_ui = EditDivisionsUI(self.logic_wrapper, self.os)
					edit_divisions_ui.prompt_option()

				# if user wnats to quit
				case "q":
					break

				# undocumented inputs get disregarded
				case _:
					input("Invalid Input!")

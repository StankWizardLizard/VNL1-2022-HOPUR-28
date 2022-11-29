from ui.guest_menu_ui import GuestMenuUI

class HostMenuUI(GuestMenuUI):
	def __init__(self, logic_wrapper, os):
		self.status = "Host"
		self.logic_wrapper = logic_wrapper
		self.os = os

	def display_user_menu(self):
		"""Displays the menu for the host"""

		print(f"Logged in as {self.status}")
		print("┌──────────────────────┐")
		print("│1) Show Teams         │")
		print("│2) Unplayed Matches   │")
		print("│3) Results            │")
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
			self.clear_user_menu()
			self.display_user_menu()
			choice = input(" > ")
			choice = choice.lower()

			match choice:
				# if user wants to show teams
				case "1":
					pass

				# if user wants to show unplayed matches
				case "2":
					pass

				# if user wants to show game results
				case "3":
					pass

				# if user wants to show division table
				case "4":
					pass

				# if user wants to create / edit Clubs
				case "5":
					pass			
	
				# if user wants to create / edit Divisions
				case "6":
					pass

				# if user wants to quit session
				case "q":
					break

				# undocumented inputs get disregarded
				case _:
					pass


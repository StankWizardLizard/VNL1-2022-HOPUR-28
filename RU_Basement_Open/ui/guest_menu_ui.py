from ui.unplayed_matches_ui import UnplayedMatchesUI 
from ui.divisions_table_ui import DivisionsTableUI
from ui.matches_ui import MatchesUI
from ui.teams_ui import TeamsUI

class GuestMenuUI:
	def __init__(self, logic_wrapper, os):
		self.status = "Guest"
		self.logic_wrapper = logic_wrapper
		self.os = os


	def clear_menu(self):
		"""Clears the menu screen"""
		if(self.os.name == "nt"):
			self.os.system("cls")
		else:
			self.os.system("clear")


	def display_menu(self):
		"""Displays the menu screen for the guest"""
	
		print(f"Logged in as {self.status}")
		print("┌─────────────────────┐")
		print("│1) Show Teams        │")
		print("│2) Unplayed Matches  │")
		print("│3) Results           │")
		print("│4) Division Table    │")
		print("│                     │")
		print("│q) Log out           │")
		print("└─────────────────────┘")


	def prompt_option(self):
		"""Prompts the user to choose an option from a list of options"""
	
		while True:
			# Display the menu and prompt the user for a choice
			self.clear_menu()
			self.display_menu()
			choice = input(" > ")
			choice = choice.lower()
			
			match choice:
				# if user wants to show teams
				case "1":
<<<<<<< HEAD
					teams_ui = TeamsUI(self.logic_wrapper, self.os)
					teams_ui.prompt_option()

				# if user wants to show unplayed matches
				case "2":
					unplayed_matches = UnplayedMatchesUI(self.logic_wrapper, self.os)
					unplayed_matches.prompt_option()
					#unplayed_matches.prompt_option()

				# if user wants to show game results
				case "3":
					matches = MatchesUI(self.logic_wrapper, self.os)
					matches.prompt_option()

				# if user wants to show division table
				case "4":
					division_ui = DivisionsTableUI(self.logic_wrapper, self.os)
					division_ui.prompt_option()
=======
					self.prompt_team_table_options()

				# if user wants to show unplayed matches
				case "2":
					self.prompt_unplayed_match_table_options()			

				# if user wants to show game results
				case "3":
					self.prompt_played_match_table_options()

				# if user wants to show division table
				case "4":
					self.prompt_division_table()			
>>>>>>> main

				# if user wants to quit session
				case "q":
					break

				# undocumented inputs get disregarded
				case _:
<<<<<<< HEAD
					input("Invalid Input!")
=======
					pass			


	def display_team_table(self):
		"""
		Displays the team table from a given list from a specific range
		expected to get a list of teams from logic layer
		"""
		
		print("Showing {} of {} teams")
		print("┌────┬────────────────┐")
		print("│100)│                │")
		print("├────┼────────────────┤")
		print("│99) │                │")
		print("├────┼────────────────┤")
		print("│98) │                │")
		print("├────┼────────────────┤")
		print("│97) │                │")
		print("├────┼────────────────┤")
		print("│96) │                │")
		print("├────┼────────────────┤")
		print("│95) │                │")
		print("├────┼────────────────┤")
		print("│94) │                │")
		print("├────┼────────────────┤")
		print("│93) │                │")
		print("├────┼────────────────┤")
		print("│92) │                │")
		print("├────┼────────────────┤")
		print("│91) │                │")
		print("└────┴────────────────┘")
		print("(N)ext page, (B)ack Page, (Q)uit")


	def prompt_team_table_options(self):
		while True:
			self.clear_user_menu()
			self.display_team_table()
			choice = input(" > ")
			choice = choice.lower()		

			match choice:
				# if user wants to see the next 10 items
				case "n":
					pass

				# if user wants to see the last 10 items
				case "b":
					pass

				# if user wants to quit
				case "q":
					break

				# undocumented inputs get disregarded
				case _:
					pass


	def display_unplayed_match_table(self):
		"""Displays the unfinished matches from a given list of matches"""
		print("Unfinished Matches")
		print("┌────┬──────────────────────────────────────┬────────────────────┐")
		print("│100)│ HR Basement Match nr 1               │ Date:              │")
		print("├────┼──────────────────────────────────────┼────────────────────┤")
		print("│99) │ HR Basement Match nr 1               │ Date:              │")
		print("├────┼──────────────────────────────────────┼────────────────────┤")
		print("│98) │ HR Basement Match nr 1               │ Date:              │")
		print("├────┼──────────────────────────────────────┼────────────────────┤")
		print("│97) │ HR Basement Match nr 1               │ Date:              │")
		print("├────┼──────────────────────────────────────┼────────────────────┤")
		print("│96) │ HR Basement Match nr 1               │ Date:              │")
		print("├────┼──────────────────────────────────────┼────────────────────┤")
		print("│95) │ HR Basement Match nr 1               │ Date:              │")
		print("├────┼──────────────────────────────────────┼────────────────────┤")
		print("│94) │ HR Basement Match nr 1               │ Date:              │")
		print("├────┼──────────────────────────────────────┼────────────────────┤")
		print("│93) │ HR Basement Match nr 1               │ Date:              │")
		print("├────┼──────────────────────────────────────┼────────────────────┤")
		print("│92) │ HR Basement Match nr 1               │ Date:              │")
		print("├────┼──────────────────────────────────────┼────────────────────┤")
		print("│91) │ HR Basement Match nr 1               │ Date:              │")
		print("└────┴──────────────────────────────────────┴────────────────────┘")
		print("(N)ext page, (B)ack Page, (Q)uit or Match number")

	def prompt_unplayed_match_table_options(self):
		"""Prompts the user to choose an option from list of options for the unplayed matches"""
		while True:
			self.clear_user_menu()
			self.display_unplayed_match_table()
			choice = input(" > ")
			choice = choice.lower()

			match choice:
				# if user wants to see the next 10 items
				case "n":
					pass

				# if user wants to see the last 10 items
				case "b":
					pass

				# if user wants to quit
				case "q":
					break

				# undocumented inputs get disregarded
				case _:
					pass

	def display_results_table(self):
		print("Match Results")
		print("┌────┬──────────────────────────────────────┬────────────────────┐")
		print("│100)│ HR Basement Match nr 1               │ Date:              │")
		print("├────┼──────────────────────────────────────┼────────────────────┤")
		print("│99) │ HR Basement Match nr 1               │ Date:              │")
		print("├────┼──────────────────────────────────────┼────────────────────┤")
		print("│98) │ HR Basement Match nr 1               │ Date:              │")
		print("├────┼──────────────────────────────────────┼────────────────────┤")
		print("│97) │ HR Basement Match nr 1               │ Date:              │")
		print("├────┼──────────────────────────────────────┼────────────────────┤")
		print("│96) │ HR Basement Match nr 1               │ Date:              │")
		print("├────┼──────────────────────────────────────┼────────────────────┤")
		print("│95) │ HR Basement Match nr 1               │ Date:              │")
		print("├────┼──────────────────────────────────────┼────────────────────┤")
		print("│94) │ HR Basement Match nr 1               │ Date:              │")
		print("├────┼──────────────────────────────────────┼────────────────────┤")
		print("│93) │ HR Basement Match nr 1               │ Date:              │")
		print("├────┼──────────────────────────────────────┼────────────────────┤")
		print("│92) │ HR Basement Match nr 1               │ Date:              │")
		print("├────┼──────────────────────────────────────┼────────────────────┤")
		print("│91) │ HR Basement Match nr 1               │ Date:              │")
		print("└────┴──────────────────────────────────────┴────────────────────┘")
		print("(N)ext page, (B)ack Page, (Q)uit or Match Number")


	def prompt_played_match_table_options(self):
		"""Prompts the user to choose an option from a list of options for the match table"""
		while True:
			self.clear_user_menu()
			self.display_results_table()
			choice = input(" > ")
			choice = choice.lower()

			match choice:
				# if user wants to see the next 10 items
				case "n":
					pass

				# if user wants to see the last 10 items
				case "b":
					pass

				# if user wnats to quit
				case "q":
					break

				# undocumented inputs get disregarded
				case _:
					pass

	def display_division_table(self):
		print("Divisions")


	def prompt_division_table(self):
		while True:
			self.clear_user_menu()
			self.display_division_table()
			choice = input(" > ")
			choice = choice.lower()

			match choice:
				# if user wants to see the next 10 items
				case "n":
					pass

				# if user wants to see the last 10 items
				case "b":
					pass

				# if user wants to quit
				case "q":
					break

				# undocumented inputs get disregarded
				case _:
					pass


>>>>>>> main

class GuestMenuUI:
	def __init__(self, logic_wrapper, os):
		self.status = "Guest"
		self.logic_wrapper = logic_wrapper
		self.os = os


	def clear_user_menu(self):
		"""Clears the menu screen"""
		if(self.os.name == "nt"):
			self.os.system("cls")
		else:
			self.os.system("clear")


	def display_user_menu(self):
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
			self.clear_user_menu()
			self.display_user_menu()
			choice = input(" > ")
			choice.lower()
			
			match choice:
				# if user wants to show teams
				case "1":
					self.prompt_team_table_option()

				# if user wants to show unplayed matches
				case "2":
					pass			

				# if user wants to show game results
				case "3":
					pass			

				# if user wants to show division table
				case "4":
					pass			

				# if user wants to quit session
				case "q":
					break

				# undocumented inputs get disregarded
				case _:
					pass			


	def display_team_table(self):
		"""
		Displays the team table from a given list from a specific range

		example of expected team list : [{name:"foo", },{},{}]
		"""
		
		print("Showing {} of {}")
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

	def prompt_team_table_option(self):
		while True:
			self.clear_user_menu()
			self.display_team_table()
			choice = input(" > ")
			choice.lower()		

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
		pass


	def display_results_table(self):
		pass


	def display_division_table(self):
		pass



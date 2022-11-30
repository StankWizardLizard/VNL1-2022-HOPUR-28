class TemplateUI:

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
		print("TEMPLATE")
		print("┌────┬──────────────────────────────────────┬────────────────────┐")
		print("│    │                                      │                    │")
		print("├────┼──────────────────────────────────────┼────────────────────┤")
		print("│    │                                      │                    │")
		print("└────┴──────────────────────────────────────┴────────────────────┘")
		print("(N)ext page, (B)ack Page, (Q)uit or Match Number")


	def prompt_option(self):
		"""Prompts the user to choose an option from a list of options for the match table"""
		while True:
			self.clear_menu()
			self.display_menu()
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
					input("Invalid Input!")


	def display_edit_matches_table(self):
		"""
		Displays edit matches window
		"""

		print("")
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

	def prompt_edit_matches(self):
		""""Prompts the captain to select which Match to edit"""
		while True:
			self.clear_user_menu()
			self.display_edit_matches_table()
			choice = input(" > ")
			choice = choice.lower()

			match choice:
				# if user wants to see match nr 1
				case "1":
					pass

				# if user wants to see match nr 2
				case "2":
					pass

				# if user wants to see match nr 3
				case "3":
					pass

				# if user wants to see match nr 4
				case "4":
					pass

				# if user wants to see match nr 5
				case "5":
					pass

				# if user wants to see match nr 6
				case "6":
					pass
				
				# if user wants to see match nr 7
				case "7":
					pass

				# if user wants to see match nr 8
				case "8":
					pass

				# if user wants to see match nr 9
				case "9":
					pass

				# if user wants to see match nr 10
				case "10":
					pass

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

	def display_table_for_matches(self):
		"""
		Displays match table for a specific match
		"""
		print("┌─────────────────────┬───────┬───────┬───────┬───────┬───────┬─────────────────────┐")
		print("│      Home Team      │ Leg 1 │ Leg 2 │ Games │ Leg 2 │ Leg 1 │      Away Team      │")
		print("├─────────────────────┼───────┼───────┼───────┼───────┼───────┼─────────────────────┤")
		print("│    Home Player 1    │       │       │  501  │       │       │    Away Player 1    │")
		print("├─────────────────────┼───────┼───────┼───────┼───────┼───────┼─────────────────────┤")
		print("│    Home Player 2    │       │       │  501  │       │       │    Away Player 2    │")
		print("├─────────────────────┼───────┼───────┼───────┼───────┼───────┼─────────────────────┤")
		print("│    Home Player 3    │       │       │  501  │       │       │    Away Player 3    │")
		print("├─────────────────────┼───────┼───────┼───────┼───────┼───────┼─────────────────────┤")
		print("│    Home Player 4    │       │       │  501  │       │       │    Away Player 4    │")
		print("╞═════════════════════╪═══════╪═══════╪═══════╪═══════╪═══════╪═════════════════════╡")
		print("│    Home Player 1    │       │       │       │       │       │    Away Player 3    │")
		print("├─────────────────────┤       │       │  301  │       │       ├─────────────────────┤")
		print("│    Home Player 2    │       │       │       │       │       │    Away Player 4    │")
		print("├─────────────────────┼───────┼───────┼───────┼───────┼───────┼─────────────────────┤")
		print("│    Home Player 3    │       │       │       │       │       │    Away Player 1    │")
		print("├─────────────────────┤       │       │   C   │       │       ├─────────────────────┤")
		print("│    Home Player 4    │       │       │       │       │       │    Away Player 2    │")
		print("╞═════════════════════╪═══════╪═══════╪═══════╪═══════╪═══════╪═════════════════════╡")
		print("│    Home Player 1    │       │       │       │       │       │    Away Player 1    │")
		print("├─────────────────────┤       │       │       │       │       ├─────────────────────┤")
		print("│    Home Player 2    │       │       │       │       │       │    Away Player 2    │")
		print("├─────────────────────┤       │       │  501  │       │       ├─────────────────────┤")
		print("│    Home Player 3    │       │       │       │       │       │    Away Player 3    │")
		print("├─────────────────────┤       │       │       │       │       ├─────────────────────┤")
		print("│    Home Player 4    │       │       │       │       │       │    Away Player 4    │")
		print("├─────────────────────┴───────┴───────┼───────┼───────┴───────┴─────────────────────┤")
		print("│                                     │ Score │                                     │")
		print("└─────────────────────────────────────┴───────┴─────────────────────────────────────┘")

	def prompt_input_match_data(self):
		""""Prompts Captain to input match data"""
		while True:
			self.clear_user_menu()
			self.display_table_for_matches()
			choice = input(" > ")
			choice = choice.lower()

			match choice:
				case _:
					break



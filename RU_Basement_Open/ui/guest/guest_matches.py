from ui.menu_frame import MenuFrame

class MatchesUI(MenuFrame):
	def __init__(self,logic_wrapper, os):
			super().__init__(logic_wrapper, os)


	def display_menu(self):
		print("Match Results")
		print("┌────┬──────────────────────────────────────┬────────────────────┐")
		print("│ NR │ Match Name                           │ Date               │")
		print("├────┼──────────────────────────────────────┼────────────────────┤")
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

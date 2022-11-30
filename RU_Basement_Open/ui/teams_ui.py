class TeamsUI:
	def __init__(self, logic_wrapper, os):
		self.logic_wrapper = logic_wrapper
		self.os = os

	def clear_menu(self):
		"""Clears the console screen"""
		if(self.os.name == "nt"):
			self.os.system("cls")
		else:
			self.os.system("clear")

	def display_menu(self):
		"""Display the menu screen for the teams table"""
		print("Showing {} of {} teams")
		print("┌────┬────────────────┐")
		print("│ NR │ Team Name      │")
		print("├────┼────────────────┤")
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

	def prompt_option(self):
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

				# if user wants to quit
				case "q":
					break

				# undocumented inputs get disregarded
				case _:
					input("Invalid Input!")

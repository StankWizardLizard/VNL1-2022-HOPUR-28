class MenuFrame:
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
		print("Menu Template")
		print("┌────┬────┬────┐")
		print("│    │    │    │")
		print("├────┼────┼────┤")
		print("│    │    │    │")
		print("└────┴────┴────┘")
		print("(N)ext page, (B)ack Page, (Q)uit or Match Number")


	def prompt_option(self):
		"""Prompts the user to choose an option from a list of options for the match table"""
		while True:
			self.clear_menu()
			self.display_menu()
			choice = input(" > ")
			choice = choice.strip().lower()

			match choice:
				# if user wants to pick option 1
				case "1":
					pass

				# if user wants to pick option 2
				case "2":
					pass

				# if user wnats to quit
				case "q":
					break

				# undocumented inputs get disregarded
				case _:
					input("Invalid Input!")

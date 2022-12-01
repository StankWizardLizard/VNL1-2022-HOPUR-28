from ui.menu_frame import MenuFrame

class EditTeamUI(MenuFrame):
	def __init__(self, logic_wrapper, os):
		super().__init__(logic_wrapper, os)


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

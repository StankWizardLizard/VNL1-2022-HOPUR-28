from ui.menu_frame import MenuFrame

class EditPlayerUI(MenuFrame):
	def __init__(self, logic_wrapper, os):
		super().__init__(logic_wrapper, os)


	def display_menu(self):
		"""Display the the menu screen onto the terminal"""
		print("Players")
		print("┌────┬──────────────────────────────────────┐")
		print("│ nr │ Player                               │")
		print("├────┼──────────────────────────────────────┤")
		print("│100)│ Player #1                            │")
		print("├────┼──────────────────────────────────────┤")
		print("│99) │ Player #2                            │")
		print("├────┼──────────────────────────────────────┤")
		print("│98) │ Player #3                            │")
		print("├────┼──────────────────────────────────────┤")
		print("│97) │ Player #4                            │")
		print("├────┼──────────────────────────────────────┤")
		print("│96) │ Player #5                            │")
		print("├────┼──────────────────────────────────────┤")
		print("│95) │ Player #6                            │")
		print("├────┼──────────────────────────────────────┤")
		print("│94) │ Player #7                            │")
		print("├────┼──────────────────────────────────────┤")
		print("│93) │ Player #8                            │")
		print("├────┼──────────────────────────────────────┤")
		print("│92) │ Player #9                            │")
		print("├────┼──────────────────────────────────────┤")
		print("│91) │ Player #10                            │")
		print("└────┴──────────────────────────────────────┘")
		print("(N)ext page, (B)ack Page, (Q)uit or Match Number")


	def prompt_option(self):
		"""Prompts the user to choose an option from a list of options for the match table"""
		while True:
			self.clear_menu()
			self.display_menu()
			choice = input(" > ")
			choice = choice.strip().lower()

			match choice:
				# if user wants to edit the first club
				case "1":
					pass

				# if user wants to edit the second club
				case "2":
					pass

				# if user wants to edit the ... club
				
				

				# if user wants to view the next 10 items
				case "n":
					pass

				# if user wants to view the last 10 items
				case "b":
					pass

				# if user wnats to quit
				case "q":
					break

				# undocumented inputs get disregarded
				case _:
					input("Invalid Input!")

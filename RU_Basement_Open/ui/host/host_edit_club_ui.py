

class EditClubUI:
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
		print("Clubs")
		print("┌────┬──────────────────────────────────────┐")
		print("│ nr │ Club Name                            │")
		print("├────┼──────────────────────────────────────┤")
		print("│100)│ Club Name #1                         │")
		print("├────┼──────────────────────────────────────┤")
		print("│99) │ Club Name #2                         │")
		print("├────┼──────────────────────────────────────┤")
		print("│98) │ Club Name #3                         │")
		print("├────┼──────────────────────────────────────┤")
		print("│97) │ Club Name #4                         │")
		print("├────┼──────────────────────────────────────┤")
		print("│96) │ Club Name #5                         │")
		print("├────┼──────────────────────────────────────┤")
		print("│95) │ Club Name #6                         │")
		print("├────┼──────────────────────────────────────┤")
		print("│94) │ Club Name #7                         │")
		print("├────┼──────────────────────────────────────┤")
		print("│93) │ Club Name #8                         │")
		print("├────┼──────────────────────────────────────┤")
		print("│92) │ Club Name #9                         │")
		print("├────┼──────────────────────────────────────┤")
		print("│91) │ Club Name #10                        │")
		print("└────┴──────────────────────────────────────┘")
		print("(N)ext page, (B)ack Page, (Q)uit or Match Number")


	def prompt_option(self):
		"""Prompts the user to choose an option from a list of options for the match table"""
		while True:
			self.clear_menu()
			self.display_menu()
			choice = input(" > ")
			choice = choice.lower()

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

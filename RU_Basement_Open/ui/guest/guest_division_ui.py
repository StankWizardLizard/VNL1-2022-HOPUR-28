
class DivisionsTableUI:
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
		print("Divisions")
		print("┌────┬──────────────────────────────────────┬──────┬──────┬──────────┐")
		print("│ NR │ Division Name                        │ Wins │ Loss │ Legs won │")
		print("├────┼──────────────────────────────────────┼──────┼──────┼──────────┤")
		print("│100)│ Division Name 1                      │ 1    │ 2    │ 2        │")
		print("├────┼──────────────────────────────────────┼──────┼──────┼──────────┤")
		print("│100)│ Division Name 1                      │ 1    │ 2    │ 2        │")
		print("├────┼──────────────────────────────────────┼──────┼──────┼──────────┤")
		print("│100)│ Division Name 1                      │ 1    │ 2    │ 2        │")
		print("├────┼──────────────────────────────────────┼──────┼──────┼──────────┤")
		print("│100)│ Division Name 1                      │ 1    │ 2    │ 2        │")
		print("├────┼──────────────────────────────────────┼──────┼──────┼──────────┤")
		print("│100)│ Division Name 1                      │ 1    │ 2    │ 2        │")
		print("├────┼──────────────────────────────────────┼──────┼──────┼──────────┤")
		print("│100)│ Division Name 1                      │ 1    │ 2    │ 2        │")
		print("├────┼──────────────────────────────────────┼──────┼──────┼──────────┤")
		print("│100)│ Division Name 1                      │ 1    │ 2    │ 2        │")
		print("├────┼──────────────────────────────────────┼──────┼──────┼──────────┤")
		print("│100)│ Division Name 1                      │ 1    │ 2    │ 2        │")
		print("├────┼──────────────────────────────────────┼──────┼──────┼──────────┤")
		print("│100)│ Division Name 1                      │ 1    │ 2    │ 2        │")
		print("├────┼──────────────────────────────────────┼──────┼──────┼──────────┤")
		print("│100)│ Division Name 1                      │ 1    │ 2    │ 2        │")
		print("└────┴──────────────────────────────────────┴──────┴──────┴──────────┘")
		print("(N)ext page, (B)ack Page, (Q)uit or Division Number")

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


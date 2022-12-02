from ui.menu_frame import MenuFrame

class DivisionsTableUI(MenuFrame):
	def __init__(self,logic_wrapper, os):
			super().__init__(logic_wrapper, os)

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

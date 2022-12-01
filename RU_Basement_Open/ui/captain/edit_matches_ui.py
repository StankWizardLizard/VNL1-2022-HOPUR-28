from ui.captain.display_table_for_matches import DisplayTableForMatchesUI

from ui.menu_frame import MenuFrame

class EditMatchesUI(MenuFrame):
	def __init__(self, logic_wrapper, os):
		super.__init__(logic_wrapper, os)


	def display_menu(self):
		"""
		Displays edit matches window
		"""

		print("Match List")
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


	def prompt_option(self):
		""""Prompts the captain to select which Match to edit"""
		while True:
			self.clear_menu()
			self.display_menu()
			choice = input(" > ")
			choice = choice.lower()

			match choice:
				# if user wants to see match nr 1
				case "1":
					# Remember to add a paramater for the match itself inside DisplayMatch
					# Also to make it work for every case from 1 to 10
					edit_match = DisplayTableForMatchesUI(self.logic_wrapper,self.os)
					edit_match.prompt_option()
					

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
					print("Invalid Input!")
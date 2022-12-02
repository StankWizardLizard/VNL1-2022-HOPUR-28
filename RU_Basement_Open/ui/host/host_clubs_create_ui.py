from ui.menu_frame import MenuFrame

class CreateClubUI(MenuFrame):
	def __init__(self, logic_wrapper, os):
		super().__init__(logic_wrapper, os)


	def display_menu(self):
		"""Display the the menu screen onto the terminal"""
		print("Registering New Club")


	def prompt_option(self):
		"""Prompts the user to choose an option from a list of options for the match table"""
		while True:
			self.clear_menu()
			self.display_menu()

			name = input("Enter Name of new club: ")
			address = input("Address of new club: ")
			phone = input("Phone number of club: ")

			choice = input("Would you like to save? (y)es, (q)uit and any for no: ")
			choice = choice.lower()

			match choice:
				# if user wants to save the the club info
				case "y":
					# save info
					pass

				# if user doesnt want to save info
				case "n":
					# dont save info
					pass

				# if user wnats to quit
				case "q":
					break

				# undocumented inputs get disregarded
				case _:
					input("Invalid Input!")

			choice = input("Would you like to create another club? (y for yes, any for no): ")
			choice = choice.lower()

			match choice:
					# if user wants to add another club
					case "y":
							pass
					
					# Undocumented inputs regarded as quit
					case _:
							break


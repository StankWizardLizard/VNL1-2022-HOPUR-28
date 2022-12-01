from ui.menu_frame import MenuFrame

class CreateDivisionsUI(MenuFrame):
	def __init__(self, logic_wrapper, os):
		super().__init__(logic_wrapper, os)


	def display_menu(self):
		"""Display the the menu screen onto the terminal"""
		print("Registering a new Division")


	def prompt_option(self):
		"""Prompts the user to choose an option from a list of options for the match table"""
		while True:
			self.clear_menu()
			self.display_menu()

			name = input("Enter name of the new divisions: ")
			host = input("Enter name of the host: ")
			phone = input("Enter phone number: ")
			rounds = input("Enter ammount of rounds: ")

			choice = input("Would you like to save? (y)es, (q)uit and any for no: ")
			choice = choice.lower()

			match choice:
				# if user wants to see the next 10 items
				case "y":
					# Save info
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

			choice = input("Would you like to create another Division? (y for yes, any for no): ")
			choice = choice.lower()

			match choice:
					# if user wants to add another club
					case "y":
							pass
					
					# Undocumented inputs regarded as quit
					case _:
							break

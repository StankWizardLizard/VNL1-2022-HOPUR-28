from ui.menu_frame import MenuFrame
from ui.functions import *

class EditTeamUI(MenuFrame):
	def __init__(self, logic_wrapper, os):
		super().__init__(logic_wrapper, os)


	def display_menu(self, teams:list=[], showing_page:int=0):
		# """Display the the menu screen onto the terminal"""
		# print("TEMPLATE")
		# print("┌────┬──────────────────────────────────────┬────────────────────┐")
		# print("│    │                                      │                    │")
		# print("├────┼──────────────────────────────────────┼────────────────────┤")
		# print("│    │                                      │                    │")
		# print("└────┴──────────────────────────────────────┴────────────────────┘")
		# print("(N)ext page, (B)ack Page, (Q)uit or Match Number")
		"""Display the menu screen for the  matches"""
		NUMBER = "NR"
		TEAM_NAME = "Team Name"
		NR = 4 #Length of number box
		DN = 40 #Length of team name box
		print("Teams")

		#Format of table with a list of lists [row name, row width]
		table_format = [[NUMBER, NR], [TEAM_NAME, DN]]
		try:
			#Fills in data for table
			table_data = []
			for i in range(showing_page*10, showing_page*10+len(teams[showing_page*10:showing_page*10+10])):
				team_nr = str(i+1) + ")"
				team =f"{teams[i].name}"
				table_data.append([team_nr, team])
			#Generates a table with the correct format and data
			generate_table(table_format, table_data)
		except IndexError:
			generate_table(table_format, [])


	def prompt_option(self, showing_page = 0):
		"""Prompts the user to choose an option from a list of options for the match table"""
		teams = self.logic_wrapper.get_all_teams()
		pages_number = len(teams)//10
		while True:
			self.clear_menu()
			self.display_menu(teams, showing_page=showing_page)
			print(display_menu_options(how_many_pages=pages_number, showing_page=showing_page))
			choice = input(" > ")
			choice = choice.lower()


			match choice:
				# if user wants to see the next 10 items
				case "n":
					showing_page += 1

				# if user wants to see the last 10 items
				case "b":
					showing_page -= 1

				# if user wnats to quit
				case "q":
					break

				# checks for numeric input and disregards undocumented inputs.
				case _:
					if choice .isnumeric:
						try:
							if teams[int(choice) -1]:
								pass
						except IndexError: 
							input("Invalid Input!")
					# undocumented inputs get disregarded
					else:
						input("Invalid Input!")


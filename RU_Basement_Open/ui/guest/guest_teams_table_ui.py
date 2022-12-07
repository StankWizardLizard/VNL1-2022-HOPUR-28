from ui.functions import *
from ui.menu_frame import MenuFrame

class TeamsTableUI(MenuFrame):
	def __init__(self,logic_wrapper, os):
		super().__init__(logic_wrapper, os)
		self.NR_OF_ENTRIES = 15


	def _get_team_display_menu_sizes(self, list_of_all_teams:list=[], showing_page:int=0):
		'''returns all the size caluclations for "Showing x-y of z teams" in display_menu'''

		# The z number for the "Showing x-y of z teams"
		all_team_size = len(list_of_all_teams) 

		# The x number for the "Showing x-y of z teams"
		showing_teams_size_start = 1 + showing_page * self.NR_OF_ENTRIES

		# The y number for the "Showing x-y of z teams" 
		showing_teams_size_end = showing_teams_size_start + len(list_of_all_teams[showing_teams_size_start: (showing_page+1) * self.NR_OF_ENTRIES+1])

		return all_team_size, showing_teams_size_end, showing_teams_size_start


	def display_menu(self, showing_page:int = 0, list_of_all_teams: list= []):
		"""Display the menu screen for the teams table"""
		"""Creates the format for the teams table then fills in data from list_of_all_teams 
		and feeds it to generate_table function to print a table for the teams"""

		NUMBER = "NR" # Header for the "NR" column
		TEAM_NAME = "Team Name" # Header for the "Team Name" column
		TN = 27 # Width of "Team Name" column
		NR = 4 # Width of "NR" column

		# Prints "Showing "x-y of z teams"
		all_team_size, showing_teams_size_end, showing_teams_size_start = self._get_team_display_menu_sizes(list_of_all_teams=list_of_all_teams, showing_page=showing_page)
		print(f"Showing {showing_teams_size_start}-{showing_teams_size_end} of {all_team_size} teams")

		# Format of table with a list of lists containing strings for each column ex. [[column name, column width], [column name, column width]]
		table_format = [[NUMBER, NR], [TEAM_NAME, TN]]
		try:
		
			# Fills in the list data for table with lists containing data for every row (make sure every row has data for all columns)
			table_data = []
			# Range starts from which page you are viewing times how many entries per page,
			# to which page you are viewing times how many entries per page plus how many entries there are in that page.
			for i in range(showing_page*self.NR_OF_ENTRIES, showing_page*self.NR_OF_ENTRIES+len(list_of_all_teams[showing_page*self.NR_OF_ENTRIES:showing_page*self.NR_OF_ENTRIES+self.NR_OF_ENTRIES])):
				team_nr = str(i+1) + ")"
				team_name = list_of_all_teams[i].name
				table_data.append([team_nr, team_name])

			# Generates a table with the correct format and data
            # example:
            # table_format = [[column1 name, column1 width], [column2 name, column2 width]]
			# table_data = [["column1 info", "column2 info"], ["column1 info", "column2 info"]...]
            # generate_table(table_format, table_data)
			generate_table(table_format, table_data)
		except IndexError:
			# Generates an empty table if list_of_all_teams gives wrong data
			generate_table(table_format, [])


	def prompt_option(self, showing_page:int = 0):
		'''Calls the a method to print a table of all teams then a method to print menu options, 
		then takes input from the user to choose an option from the list of options printed for the teams table'''
		list_of_all_teams = self.logic_wrapper.get_all_teams()
		page_numbers = len(list_of_all_teams)//self.NR_OF_ENTRIES

		while True:

			self.clear_menu()
			self.display_menu(showing_page=showing_page, list_of_all_teams=list_of_all_teams)
			print(display_menu_options(showing_page=showing_page, how_many_pages=page_numbers))
			choice = input(" > ")
			choice = choice.lower()

			match choice:
				#  if user wants to see the next self.NR_Of_ENTRIES items
				case "n":
					if showing_page == page_numbers:
						input("Invalid Input!")
					else:
						showing_page += 1

				#  if user wants to see the last self.NR_OF_ENTRIES items
				case "b":
					if showing_page == 0:
						input("Invalid Input!")
					else:
						showing_page -= 1

				#  if user wants to quit and return to the last page
				case "q":
					break

				#  undocumented inputs get disregarded
				case _:
					input("Invalid Input!")


'''
Display the menu screen for the teams table
print("Showing {} of {} teams")
print("┌────┬────────────────┐")
print("│ NR │ Team Name      │")
print("├────┼────────────────┤")
print("│100)│                │")
print("├────┼────────────────┤")
print("│99) │                │")
print("├────┼────────────────┤")
print("│98) │                │")
print("├────┼────────────────┤")
print("│97) │                │")
print("├────┼────────────────┤")
print("│96) │                │")
print("├────┼────────────────┤")
print("│95) │                │")
print("├────┼────────────────┤")
print("│94) │                │")
print("├────┼────────────────┤")
print("│93) │                │")
print("├────┼────────────────┤")
print("│92) │                │")
print("├────┼────────────────┤")
print("│91) │                │")
print("└────┴────────────────┘")
print("(N)ext page, (B)ack Page, (Q)uit")
'''

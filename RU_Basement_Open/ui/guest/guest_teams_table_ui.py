from ui.functions import *
from ui.menu_frame import MenuFrame

class TeamsTableUI(MenuFrame):
	def __init__(self,logic_wrapper, os):
		super().__init__(logic_wrapper, os)


	def _get_all_teams_in_correct_format(self):
		'''gets all teams from the logic layer and converts it into a correct format (for printing) of a list with team names'''
		teams = get_all_teams(self.logic_wrapper)
		new_teams = []

		for x in teams:
			new_teams.append(x.name)
		return new_teams


	def _get_team_display_menu_sizes(self, list_of_all_teams:list=[], showing_page:int=0):
		'''returns all the size caluclations for display_menu'''

		#The z number for the "Showing x-y of z teams" in the teams display menu
		all_team_size = len(list_of_all_teams) 

		#The x number for the "Showing x-y of z teams" in the teams display menu
		showing_teams_size_start = 1 + showing_page * 10

		#The y number for the "Showing x-y of z teams" in the teams display menu
		if showing_page*10+10 > len(list_of_all_teams):
			if showing_page:
				showing_teams_size = (showing_page*10+10)- ((len(list_of_all_teams) % (showing_page*10)))
			else:
				showing_teams_size = len(list_of_all_teams)
		else:
			showing_teams_size = showing_page * 10 + 10

		return all_team_size, showing_teams_size, showing_teams_size_start


	def display_menu(self, showing_page:int = 0, list_of_all_teams: list= []):
		"""Display the menu screen for the teams table"""

		NUMBER = "NR"
		TEAM_NAME = "Team Name"
		TN = 27 #Length of team name box
		NR = 4 #Length of number box

		all_team_size, showing_teams_size, showing_teams_size_start = self._get_team_display_menu_sizes(list_of_all_teams=list_of_all_teams, showing_page=showing_page)
		
		print(f"Showing {showing_teams_size_start}-{showing_teams_size} of {all_team_size} teams")
		#Format of table with a list of lists [row name, row width] #Generates a table with the correct format and data
		table_format = [[NUMBER, NR], [TEAM_NAME, TN]]
		try:
		
			#Fills in data for table
			table_data = []
			for i in range(showing_page*10, showing_page*10+len(list_of_all_teams[showing_page*10:showing_page*10+10])):
				team_nr = str(i+1) + ")"
				team_name = list_of_all_teams[i]
				table_data.append([team_nr, team_name])

			#Generates a table with the correct format and data
			generate_table(table_format, table_data)
		except IndexError:
			generate_table(table_format, [])


	def prompt_option(self, showing_page:int = 0):
		'''Calls the display_menu method to print the show teams menu and then executes based on the input from the user'''
		list_of_all_teams = self._get_all_teams_in_correct_format()
		page_numbers = len(list_of_all_teams)//10

		while True:

			self.clear_menu()
			self.display_menu(showing_page=showing_page, list_of_all_teams=list_of_all_teams)
			print(display_menu_options(showing_page=showing_page, how_many_pages=page_numbers))
			choice = input(" > ")
			choice = choice.lower()

			match choice:
				# if user wants to see the next 10 items
				case "n":
					if showing_page == page_numbers:
						input("Invalid Input!")
					else:
						showing_page += 1

				# if user wants to see the last 10 items
				case "b":
					if showing_page == 0:
						input("Invalid Input!")
					else:
						showing_page -= 1

				# if user wants to quit
				case "q":
					break

				# undocumented inputs get disregarded
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

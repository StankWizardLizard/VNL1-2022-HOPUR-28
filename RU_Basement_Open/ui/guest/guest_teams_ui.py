from ui.functions import *
from ui.menu_frame import MenuFrame

class TeamsUI(MenuFrame):
	def __init__(self,logic_wrapper, os):
		super().__init__(logic_wrapper, os)


	def _get_all_teams_in_correct_format(self):
		'''gets all teams from the logic layer and converts it into a format of a list with a list of teams inside
		with <= 10 teams per list [[10 teams][10 teams]...[remaining teams]]'''
		teams = get_all_teams(self.logic_wrapper)
		new_teams = []

		if len(teams) > 10:
			for i in range(0, len(teams)//10):
				team_page = []
				for e in range(i*10, i*10+10):
					team_page.append(teams[e].name)
				new_teams.append(team_page)
				
			if len(teams) % 10 != 0:
				team_page = []
				for x in teams[len(teams)-len(teams) % 10:]:
					team_page.append(x.name)
			new_teams.append(team_page)
		else:
			team_page = []
			for x in teams:
				team_page.append(x.name)
			new_teams.append(team_page)
		return new_teams


	def _get_team_display_menu_sizes(self, list_of_all_teams:list=[], showing_page:int=0):
		'''returns all the size caluclations for display_menu'''

		#The z number for the "Showing x-y of z teams" in the teams display menu
		#All the teams equal the length of all lists in list_of_all_teams except the last times 10, plus the length of the last list in list_of_all_teams
		all_team_size = (len(list_of_all_teams)-1) * 10 + len(list_of_all_teams[-1])  

		#The x number for the "Showing x-y of z teams" in the teams display menu
		#The first number represents the lowest number in a range of 10 numbers that the page is currently showing. Which equals 1 plus the page number times 10
		showing_teams_size_start = 1 + showing_page * 10

		#The y number for the "Showing x-y of z teams" in the teams display menu
		#The second number represents the highest number in a range of 10 numbers that the page is currently showing. 
		# hich equals 10 times the page number + length of the list curently showing
		showing_teams_size = showing_page * 10 + len(list_of_all_teams[showing_page])

		return all_team_size, showing_teams_size, showing_teams_size_start


	def display_menu(self, showing_page:int = 0, list_of_all_teams: list= []):
		"""Display the menu screen for the teams table"""

		LINE = "─"
		TEAM_NAME = "Team Name"
		LM = 40 #Length of match box

		all_team_size, showing_teams_size, showing_teams_size_start = self._get_team_display_menu_sizes(list_of_all_teams=list_of_all_teams, showing_page=showing_page)
		
		print(f"Showing {showing_teams_size_start}-{showing_teams_size} of {all_team_size} teams")
		print(f"┌────┬{LINE:─^{LM}}┐")
		print(f"│ NR │{TEAM_NAME:^{LM}}│")
		print(f"├────┼{LINE:─^{LM}}┤")
		for i in range(len(list_of_all_teams[showing_page])):
			team_nr = str(i + showing_page * 10) + ")"
			print(f"│{team_nr:^4}│{list_of_all_teams[showing_page][i]:^{LM}}│")
		print(f"└────┴{LINE:─^{LM}}┘")
		print(self._display_menu_options(list_of_all_teams,showing_page))


	def _display_menu_options(self, list_of_all_teams:list=[], showing_page:int=0):
		'''returns a string listing the available options of the menu'''

		if showing_page == 0:
			if len(list_of_all_teams) > 1:
				return "(N)ext page, (Q)uit"
			else:
				return "(Q)uit"

		elif showing_page+1 == len(list_of_all_teams):
			return "(B)ack Page, (Q)uit"

		else:
			return"(N)ext page, (B)ack Page, (Q)uit"

	def prompt_option(self, showing_page:int = 0):
		'''Calls the display_menu method to print the show teams menu and then executes based on the input from the user'''
		
		while True:
			list_of_all_teams = self._get_all_teams_in_correct_format()

			self.clear_menu()
			self.display_menu(showing_page=showing_page, list_of_all_teams=list_of_all_teams)
			choice = input(" > ")
			choice = choice.lower()

			match choice:
				# if user wants to see the next 10 items
				case "n":
					if showing_page+1 == len(list_of_all_teams):
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


'''	def display_menu(self):
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
'''

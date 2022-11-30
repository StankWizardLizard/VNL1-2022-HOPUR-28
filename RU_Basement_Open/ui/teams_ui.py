from ui.functions import *

class TeamsUI:
	def __init__(self, logic_wrapper, os):
		self.logic_wrapper = logic_wrapper
		self.os = os

	def clear_menu(self):
		"""Clears the console screen"""
		if(self.os.name == "nt"):
			self.os.system("cls")
		else:
			self.os.system("clear")

	def _get_all_teams_in_correct_format(self):
		'''gets all teams from the logic layer and converts it into a format of a list with a list of matches inside
		with <= 10 matches per list'''
		teams = get_all_teams(self.logic_wrapper)
		new_teams = []
		if len(teams) > 10:
			for i in range(0, (len(teams)//10)):
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

	def display_menu(self, showing_teams:int = 0, list_of_all_teams: list= []):
		"""Display the menu screen for the teams table"""
		all_team_size = (len(list_of_all_teams)-1) * 10 + len(list_of_all_teams[-1])
		print(all_team_size)
		showing_teams_size_start = 1 + showing_teams * 10
		showing_teams_size = showing_teams * 10 + len(list_of_all_teams[showing_teams])
		line = "─"
		team_name = "Team Name"
		print(f"Showing {showing_teams_size_start}-{showing_teams_size} of {all_team_size} teams")
		print(f"┌────┬{line:─^40}┐")
		print(f"│ NR │{team_name:^40}│")
		print(f"├────┼{line:─^40}┤")
		for i in range(len(list_of_all_teams[showing_teams])):
			team_nr = str(i + showing_teams * 10) + ")"
			print(f"│{team_nr:^4}│{list_of_all_teams[showing_teams][i]:^40}│")
		print(f"└────┴{line:─^40}┘")
		if showing_teams == 0:
			if len(list_of_all_teams) > 1:
				print("(N)ext page, (Q)uit")
			else:
				print("(Q)uit")
		elif showing_teams+1 == len(list_of_all_teams):
			print("(B)ack Page, (Q)uit")
		else:
			print("(N)ext page, (B)ack Page, (Q)uit")

	def prompt_option(self, showing_teams = 0):
		while True:
			list_of_all_teams = self._get_all_teams_in_correct_format()
			self.clear_menu()
			self.display_menu(showing_teams=showing_teams, list_of_all_teams=list_of_all_teams)
			choice = input(" > ")
			choice = choice.lower()		

			match choice:
				# if user wants to see the next 10 items
				case "n":
					if showing_teams+1 == len(list_of_all_teams):
						input("Invalid Input!")
					else:
						showing_teams += 1

				# if user wants to see the last 10 items
				case "b":
					if showing_teams == 0:
						input("Invalid Input!")
					else:
						showing_teams -= 1

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

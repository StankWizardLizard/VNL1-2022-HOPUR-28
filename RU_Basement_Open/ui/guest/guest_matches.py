from ui.functions import *

class MatchesUI:

	def __init__(self, logic_wrapper, os):
		self.logic_wrapper = logic_wrapper
		self.os = os


	def clear_menu(self):
		"""Clears the menu screen"""
		if(self.os.name == "nt"):
			self.os.system("cls")
		else:
			self.os.system("clear")

	def _get_all_concluded_matches_in_correct_format(self):
		matches = get_all_concluded_matches(self.logic_wrapper)
		new_matches = []
		if len(matches) > 10:
			for i in range(0, (len(matches)//10)):
				match_page = []
				for e in range(i*10, i*10+10):
					match_page.append([matches[e].home_team, matches[e].away_team, matches[e].date])
				if len(matches) % 10 != 0:
					match_page = []
					for x in matches[len(matches)-len(matches) % 10:]:
						match_page.append(x.home_team, x.away_team, x.date)
				new_matches.append(match_page)
		else:
			match_page = []
			for x in matches:
				match_page.append([x.home_team, x.away_team, x.date])
			new_matches.append(match_page)
		return new_matches



	def display_menu(self, showing_page:int=0, list_of_all_match_results:list=[]):
		LINE = "─"
		MATCH_NAME = "Match Name"
		DATE = "Date"
		LM = 40 #Length of match box
		LD = 20 #Length of date box 

		print("Match Results")
		print(f"┌────┬{LINE:─^{LM}}┬{LINE:─^{LD}}┐")
		print(f"│ NR │{MATCH_NAME:^{LM}}│{DATE:^{LD}}│")
		print(f"├────┼{LINE:─^{LM}}┼{LINE:─^{LD}}┤")
		for i in range(len(list_of_all_match_results[showing_page])):
			team_nr = str(i + showing_page * 10) + ")"
			teams_playing =f"{list_of_all_match_results[showing_page][i][0]} vs {list_of_all_match_results[showing_page][i][1]}"
			date = str(list_of_all_match_results[showing_page][i][2])
			print(f"│{team_nr:^4}│{teams_playing:^{LM}}│{date:^{LD}}│")
		print(f"└────┴{LINE:─^{LM}}┴{LINE:─^{LD}}┘")
		

	def _display_menu_options(self, list_of_all_match_results:list=[], showing_page:int=0):
		'''returns a string listing the available options of the menu'''

		if showing_page == 0:
			if len(list_of_all_match_results) > 1:
				return "(N)ext page, (Q)uit"
			else:
				return "(Q)uit"
		elif showing_page+1 == len(list_of_all_match_results):
			return "(B)ack Page, (Q)uit"
		else:
			return"(N)ext page, (B)ack Page, (Q)uit"


	def prompt_option(self, showing_page:int = 0):
		"""Prompts the user to choose an option from a list of options for the match table"""
		while True:
			list_of_all_match_results = self._get_all_concluded_matches_in_correct_format()
			self.clear_menu()
			self.display_menu(showing_page=showing_page, list_of_all_match_results=list_of_all_match_results)
			print(self._display_menu_options(showing_page=showing_page, list_of_all_match_results=list_of_all_match_results))
			choice = input(" > ")
			choice = choice.lower()
			match choice:
				# if user wants to see the next 10 items
				case "n":
					if showing_page+1 == len(list_of_all_match_results):
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

'''def display_menu(self):
		print("Match Results")
		print("┌────┬──────────────────────────────────────┬────────────────────┐")
		print("│ NR │ Match Name                           │ Date               │")
		print("├────┼──────────────────────────────────────┼────────────────────┤")
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
		print("(N)ext page, (B)ack Page, (Q)uit or Match Number")


def prompt_option(self):
	"""Prompts the user to choose an option from a list of options for the match table"""
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

			# if user wnats to quit
			case "q":
				break

			# undocumented inputs get disregarded
			case _:
				input("Invalid Input!")'''
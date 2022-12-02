from ui.functions import *
from ui.menu_frame import MenuFrame

class MatchesTableUI(MenuFrame):
	def __init__(self,logic_wrapper, os, is_finished = True):
			super().__init__(logic_wrapper, os)
			self.is_finished = is_finished

	def _get_all_matches_in_correct_format(self):
		'''
		gets all  matches from the logic layer and converts it into a format of a list
		with lists of lists containing information about the matches with <= 10 matches per list and
		in a format of home team, then away team, then date  [[[match], [match]..]...[remaining matches]]
		'''
		if self.is_finished:
			matches = get_all_concluded_matches(self.logic_wrapper)
		else: 
			matches = get_all_unplayed_matches(self.logic_wrapper)
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
		"""Display the menu screen for the  matches"""
		EMPTY = "" 
		NUMBER = "NR"
		MATCH_NAME = "Match Name"
		DATE = "Date"
		NR = 4 #Length of number box
		LM = 40 #Length of match box
		LD = 20 #Length of date box

		print("Match Results")
		print(f"┌{EMPTY:─^{NR}}┬{EMPTY:─^{LM}}┬{EMPTY:─^{LD}}┐")
		print(f"│{NUMBER:^{NR}}│{MATCH_NAME:^{LM}}│{DATE:^{LD}}│")
		print(f"├{EMPTY:─^{NR}}┼{EMPTY:─^{LM}}┼{EMPTY:─^{LD}}┤")
		try:
			for i in range(len(list_of_all_match_results[showing_page])):
				match_nr = str(i + showing_page * 10) + ")"
				teams_playing =f"{list_of_all_match_results[showing_page][i][0]} vs {list_of_all_match_results[showing_page][i][1]}"
				date = str(list_of_all_match_results[showing_page][i][2])
				print(f"│{match_nr:^4}│{teams_playing:^{LM}}│{date:^{LD}}│")
		except IndexError:
			print(f"│{EMPTY:^4}│{EMPTY:^{LM}}│{EMPTY:^{LD}}│")
		print(f"└{EMPTY:─^{NR}}┴{EMPTY:─^{LM}}┴{EMPTY:─^{LD}}┘")
		


	def prompt_option(self, showing_page:int = 0):
		"""Prompts the user to choose an option from a list of options for the match table"""
		list_of_all_match_results = self._get_all_matches_in_correct_format()
		while True:
			self.clear_menu()
			self.display_menu(showing_page=showing_page, list_of_all_match_results=list_of_all_match_results)
			print(display_menu_options(showing_page=showing_page, list_of_displays=list_of_all_match_results))
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

'''
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
'''
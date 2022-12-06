from ui.functions import *
from ui.menu_frame import MenuFrame
from ui.guest.guest_match_table_ui import MatchTableUI

class MatchesTableUI(MenuFrame):
	def __init__(self,logic_wrapper, os, is_finished = True):
		super().__init__(logic_wrapper, os)
		self.is_finished = is_finished
		self.NR_OF_ENTRIES = 10

	def display_menu(self, showing_page:int=0, matches:list=[]):
		"""Display the menu screen for the  table_data"""
		NUMBER = "NR"
		MATCH_NAME = "Match Name"
		DATE = "Date"
		NR = 4 #Length of number box
		LM = 40 #Length of match box
		LD = 20 #Length of date box

		print("Match Results")
		#Format of table with a list of lists [row name, row width] #Generates a table with the correct format and data
		table_format = [[NUMBER, NR], [MATCH_NAME, LM], [DATE, LD]]
		try:

			#Fills in data for table 
			table_data = []
			for i in range(showing_page*self.NR_OF_ENTRIES, showing_page*self.NR_OF_ENTRIES+len(matches[showing_page*self.NR_OF_ENTRIES:showing_page*self.NR_OF_ENTRIES+self.NR_OF_ENTRIES])):
				match_nr = str(i+1) + ")"
				teams_playing =f"{matches[i].home_team} vs {matches[i].away_team}"
				date = str(matches[i].date)
				table_data.append([match_nr, teams_playing, date])

			#Generates a table with the correct format and data
			generate_table(table_format, table_data)
		except IndexError:
			generate_table(table_format, [])

	def prompt_option(self, showing_page:int = 0):
		"""Prompts the user to choose an option from a list of options for the match table"""
		if self.is_finished:
			matches = get_all_concluded_matches(self.logic_wrapper)
		else: 
			matches = get_all_unplayed_matches(self.logic_wrapper)
		page_numbers = len(matches) // self.NR_OF_ENTRIES
		while True:
			self.clear_menu()
			self.display_menu(showing_page=showing_page, matches=matches)
			print(display_menu_options(showing_page=showing_page, how_many_pages=page_numbers))
			choice = input(" > ")
			choice = choice.lower()
			match choice:
				# if user wants to see the next NR_OF_ENTRIES items
				case "n":
					if showing_page == page_numbers:
						input("Invalid Input!")
					else:
						showing_page += 1

				# if user wants to see the last NR_OF_ENTRIES items
				case "b":
					if showing_page == 0:
						input("Invalid Input!")
					else:
						showing_page -= 1

				# if user wants to quit
				case "q":
					break

				# checks if user inputed number of a match and opens MatchTableUI if they did
				case _:
					if choice.isnumeric():
						try:
							if matches[int(choice)-1]:
								match = matches[int(choice)-1]
								match_table_ui = MatchTableUI(self.logic_wrapper, self.os, match)
								match_table_ui.prompt_option()
						except IndexError:
							input("Invalid Input!")
				# undocumented inputs get disregarded
					else:
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
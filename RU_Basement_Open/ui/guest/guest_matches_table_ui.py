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
		"""Creates the format for the matches table then fills in data from matches 
		and feeds it to generate_table function to print a table for either unplayed matches or finished matches"""
		NUMBER = "NR" # Header of "NR" column
		MATCH_NAME = "Match Name" # Header of "Match Name" column
		DATE = "Date" # Header of "Date" column
		NR = 4 # Width of "NR" column
		LM = 40 # Width of "Match Name" column
		LD = 20 # Width of "Date" column

		if self.is_finished:
			print("Match Results")
		else:
			print("Unplayed Matches")

		# Format of table with a list of lists containing strings for each column ex. [[column name, column width], [column name, column width]]
		table_format = [[NUMBER, NR], [MATCH_NAME, LM], [DATE, LD]]
		try:

			# Fills in the list data for table with lists containing data for every row (make sure every row has data for all columns)
			table_data = []
			# Range starts from which page you are viewing times how many entries per page,
			# to which page you are viewing times how many entries per page plus how many entries there are in that page.
			for i in range(showing_page*self.NR_OF_ENTRIES, showing_page*self.NR_OF_ENTRIES+len(matches[showing_page*self.NR_OF_ENTRIES:showing_page*self.NR_OF_ENTRIES+self.NR_OF_ENTRIES])):
				match_nr = str(i+1) + ")"
				home_team = self.logic_wrapper.get_team(matches[i].home_team)
				away_team = self.logic_wrapper.get_team(matches[i].away_team)
				teams_playing =f"{home_team.name} vs {away_team.name}"
				date = str(matches[i].date)
				table_data.append([match_nr, teams_playing, date])

			# Generates a table with the correct format and data
            # example:
            # table_format = [[column1 name, column1 width], [column2 name, column2 width]]
			# table_data = [["column1 info", "column2 info"], ["column1 info", "column2 info"]...]
            # generate_table(table_format, table_data)
			generate_table(table_format, table_data)
		except IndexError:
			# Generates an empty table if matches gives wrong data
			pass
			generate_table(table_format, [])

	def prompt_option(self, showing_page:int = 0):
		'''Checks if user wants matches that are finished or unplayed, 
		then calls the a method to print a table of all teams then a method to print menu options, 
		then takes input from the user to choose an option from the list of options printed for the teams table'''
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
				#  if user wants to see the next NR_OF_ENTRIES items
				case "n":
					if showing_page == page_numbers:
						input("Invalid Input!")
					else:
						showing_page += 1

				#  if user wants to see the last NR_OF_ENTRIES items
				case "b":
					if showing_page == 0:
						input("Invalid Input!")
					else:
						showing_page -= 1

				#  if user wants to quit and and return to the last page
				case "q":
					break

				#  checks if user inputed number of a match and opens MatchTableUI if it is correct, otherwise prints invalid input
				case _:
					if choice.isnumeric():
						if matches[int(choice)-1]:
							match = matches[int(choice)-1]
							match_table_ui = MatchTableUI(self.logic_wrapper, self.os, match)
							match_table_ui.prompt_option()
					
				#  undocumented inputs get disregarded
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
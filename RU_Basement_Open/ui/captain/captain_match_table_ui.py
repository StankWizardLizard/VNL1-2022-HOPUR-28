from ui.captain.captain_match_edit_ui import MatchEditUI

from ui.menu_frame import MenuFrame

from ui.functions import get_all_concluded_matches
from ui.functions import get_all_unplayed_matches
from ui.functions import get_all_matches

from math import ceil

class CaptainMatchesTableUI(MenuFrame):
	def __init__(self, logic_wrapper, os, match_finished_status = True):
		super().__init__(logic_wrapper, os)
		self.match_finished_status = match_finished_status
		self.current_page_number = 0
		self.page_number = 0
		self.match_list = []


	def get_match_list(self):
		"""Gets a list of either unplayed or completed matches based on self.match_finished_status variable"""

		return get_all_unplayed_matches(self.logic_wrapper)

		if(self.match_finished_status):
			return get_all_concluded_matches(self.logic_wrapper)
		else:
			return get_all_unplayed_matches(self.logic_wrapper)


	def format_match_list(self, match_list):
		"""Given a list of matches, formats its so that each 'page' should contain 10 items and/or last page contains 10 items or less"""

		formatted_list = []

		# Split list into list of sublists that contain every 10 items
		for i in range(ceil(len(match_list)/10)):
			formatted_list.append(match_list[i*10:i*10+10])

		return formatted_list


	def display_menu(self):
		"""Displays the match table window and the options"""

		# Print the menu
		print(f"Showing page {self.current_page_number+1}-{self.max_page_number} of Matches")
		print("┌────┬────────────────────────────────────────────────────────┬──────────────────┐")
		print("│ NR │                          Match                         │       Date       │")

		try:
			for i in range(0,len(self.match_list[self.current_page_number])):
				current_match_number = str(i+1) + ')'
				current_match = self.match_list[self.current_page_number][i]
				print("├────┼────────────────────────────────────────────────────────┼──────────────────┤")
				print(f"│{current_match_number:^4}│{current_match.home_team:^27}vs{current_match.away_team:^27}│ Date:{current_match.date:^12}│")
		except IndexError:
			pass

		print("└────┴────────────────────────────────────────────────────────┴──────────────────┘")
		print("(N)ext page, (B)ack Page, (Q)uit or Match Number")


	def prompt_option(self):
		""""Prompts the captain to select which option to pick, gives error when selected option doesnt exits"""

		self.match_list = self.get_match_list()
		self.match_list = self.format_match_list(self.match_list)
		self.max_page_number = len(self.match_list)

		while True:
			self.clear_menu()
			self.display_menu()

			choice = input(" > ")
			choice = choice.lower()

			match choice:
				# if user wants to see the next 10 items
				case "n":
					if(self.current_page_number+1 == self.max_page_number):
						input("Invalid Input!")
					else:
						self.current_page_number += 1

				# if user wants to see the last 10 items
				case "b":
					if(self.current_page_number == 0):
						input("Invalid Input")
					else:
						self.current_page_number -= 1

				# if user wants to quit
				case "q":
					break

				# undocumented input
				case _:
					# check if choice is a decimal
					if(choice.isdecimal()):
						# check if item exists in current page of lists						
						if(len(self.match_list[self.current_page_number]) > (int(choice)-1)):
							# Check out the match
							choice = int(choice) - 1
							match_edit_ui = MatchEditUI(self.logic_wrapper, self.os, self.match_list[self.current_page_number][choice])
							match_edit_ui.prompt_option()

						else:
							# not in options
							input("Invalid Input!")

					else:
						# not in options
						input("Invalid Input!")

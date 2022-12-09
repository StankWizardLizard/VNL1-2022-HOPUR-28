from ui.menu_frame import MenuFrame
from ui.functions import *

class EditClubUI(MenuFrame):
	def __init__(self, logic_wrapper, os):
		super().__init__(logic_wrapper, os)

	def display_menu(self, clubs:list=[], showing_page:int=0):
		"""Display the menu screen for the  matches"""
		NUMBER = "NR"
		CLUB_NAME = "Club Name"
		NR = 4 #Length of number box
		DN = 40 #Length of team name box
		print("Clubs")

		#Format of table with a list of lists [row name, row width]
		table_format = [[NUMBER, NR], [CLUB_NAME, DN]]
		try:
			#Fills in data for table
			table_data = []
			for i in range(showing_page*10, showing_page*10+len(clubs[showing_page*10:showing_page*10+10])):
				club_nr = str(i+1) + ")"
				club =f"{clubs[i].name}"
				table_data.append([club_nr, club])
			#Generates a table with the correct format and data
			generate_table(table_format, table_data)
		except IndexError:
			generate_table(table_format, [])

	def prompt_option(self, showing_page = 0):
		"""Prompts the user to choose an option from a list of options for the match table"""
		clubs = self.logic_wrapper.get_all_clubs()
		pages_number = len(clubs)//10
		while True:
			self.clear_menu()
			self.display_menu(clubs, showing_page=showing_page)
			print(display_menu_options(how_many_pages=pages_number, showing_page=showing_page))
			choice = input(" > ")
			choice = choice.strip().lower()
			match choice:
				# if user wants to edit the first club
				case "1":
					pass

				# if user wants to edit the second club
				case "2":
					pass

				# if user wants to edit the ... club
				
				

				# if user wants to view the next 10 items
				case "n":
					showing_page += 1


				# if user wants to view the last 10 items
				case "b":
					showing_page -= 1

				# if user wnats to quit
				case "q":
					break

				# undocumented inputs get disregarded
				case _:
					input("Invalid Input!")

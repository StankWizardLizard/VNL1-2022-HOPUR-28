from ui.menu_frame import MenuFrame
from ui.functions import *

class MatchTableUI(MenuFrame):
	def __init__(self, logic_wrapper, os, match):
		super().__init__(logic_wrapper, os)
		self.match = match
		self.points_list = [["","","",""],["","","",""],["","","",""],["","","",""],["","","",""],["","","",""],["","","",""]]
		
		self.home_team_list = self.match.home_team_players
		self.home_team_name = self.match.home_team
		self.away_team_list = self.match.away_team_players
		self.away_team_name = self.match.away_team

		self.match_number = self.match.id
		division = self.logic_wrapper.get_division(self.match.division_id)
		self.leage_name = division.name

	def display_menu(self):
		"""Displays match table for a specific match"""

		MATCH_NAME = f"{self.leage_name} Match nr. {self.match_number}"
		HOME_TEAM = "Home Team"
		AWAY_TEAM = "Away Team"
		LEG_1 = "Leg 1"
		LEG_2 = "Leg 2"
		GAMES = "Games"
		HT = 22 #"Home" and "Away Team" column width
		LEGS = 7 #Legs column width
		GM = 7 # Games column width

		LEG_1_FORMAT = [LEG_1, LEGS]
		LEG_2_FORMAT = [LEG_2, LEGS]
		table_format = [
			[HOME_TEAM, HT], LEG_1_FORMAT,LEG_2_FORMAT, [GAMES, GM], LEG_2_FORMAT, LEG_1_FORMAT, [AWAY_TEAM, HT]
			]

		print(f"{MATCH_NAME}")
		table_data = []
		
		for i in range(0, 7):
			column = [
			f"{i}", self.points_list[i][0], self.points_list[i][1], "Game",  
			self.points_list[i][2], self.points_list[i][3], f"{i}"
			]
			table_data.append(column)
		generate_table(table_format, table_data)

		home_team = "Home: " + self.home_team_name
		away_team = "Away: " + self.away_team_name
		teams_table_format = [[home_team, HT], [away_team, HT]]
		teams_table_data = []
		for i in range(4):
			column = [self.home_team_list[i], self.away_team_list[i]]
			teams_table_data.append(column)
		generate_table(teams_table_format, teams_table_data)


	def prompt_option(self):
		'''Prompts the user to choose an option from a list of options for the match table'''
		while True:

			self.clear_menu()
			self.display_menu()

			print(display_menu_options(how_many_pages=0, showing_page=0))

			choice = input(" > ")
			choice = choice.lower()

			match choice:
				case "q":
					break

				case _:
					input("Invalid Input!")

'''print(f"┌─────────────────────┬───────┬───────┬───────┬───────┬───────┬─────────────────────┐")
print(f"│      Home Team      │ Leg 1 │ Leg 2 │ Games │ Leg 2 │ Leg 1 │      Away Team      │")
print(f"├─────────────────────┼───────┼───────┼───────┼───────┼───────┼─────────────────────┤")
print(f"│    Home Player 1    │{self.points_list[0][0]:^7}│{self.points_list[0][1]:^7}│  501  │{self.points_list[0][2]:^7}│{self.points_list[0][3]:^7}│    Away Player 1    │")
print(f"├─────────────────────┼───────┼───────┼───────┼───────┼───────┼─────────────────────┤")
print(f"│    Home Player 2    │{self.points_list[1][0]:^7}│{self.points_list[1][1]:^7}│  501  │{self.points_list[1][2]:^7}│{self.points_list[1][3]:^7}│    Away Player 2    │")
print(f"├─────────────────────┼───────┼───────┼───────┼───────┼───────┼─────────────────────┤")
print(f"│    Home Player 3    │{self.points_list[2][0]:^7}│{self.points_list[2][1]:^7}│  501  │{self.points_list[2][2]:^7}│{self.points_list[2][3]:^7}│    Away Player 3    │")
print(f"├─────────────────────┼───────┼───────┼───────┼───────┼───────┼─────────────────────┤")
print(f"│    Home Player 4    │{self.points_list[3][0]:^7}│{self.points_list[3][1]:^7}│  501  │{self.points_list[3][2]:^7}│{self.points_list[3][3]:^7}│    Away Player 4    │")
print(f"╞═════════════════════╪═══════╪═══════╪═══════╪═══════╪═══════╪═════════════════════╡")
print(f"│    Home Player 1    │       │       │       │       │       │    Away Player 3    │")
print(f"├─────────────────────┤{self.points_list[4][0]:^7}│{self.points_list[4][1]:^7}│  301  │{self.points_list[4][2]:^7}│{self.points_list[4][3]:^7}├─────────────────────┤")
print(f"│    Home Player 2    │       │       │       │       │       │    Away Player 4    │")
print(f"├─────────────────────┼───────┼───────┼───────┼───────┼───────┼─────────────────────┤")
print(f"│    Home Player 3    │       │       │       │       │       │    Away Player 1    │")
print(f"├─────────────────────┤{self.points_list[5][0]:^7}│{self.points_list[5][1]:^7}│   C   │{self.points_list[5][2]:^7}│{self.points_list[5][3]:^7}├─────────────────────┤")
print(f"│    Home Player 4    │       │       │       │       │       │    Away Player 2    │")
print(f"╞═════════════════════╪═══════╪═══════╪═══════╪═══════╪═══════╪═════════════════════╡")
print(f"│    Home Player 1    │       │       │       │       │       │    Away Player 1    │")
print(f"├─────────────────────┤       │       │       │       │       ├─────────────────────┤")
print(f"│    Home Player 2    │       │       │       │       │       │    Away Player 2    │")
print(f"├─────────────────────┤{self.points_list[6][0]:^7}│{self.points_list[6][1]:^7}│  501  │{self.points_list[6][2]:^7}│{self.points_list[6][3]:^7}├─────────────────────┤")
print(f"│    Home Player 3    │       │       │       │       │       │    Away Player 3    │")
print(f"├─────────────────────┤       │       │       │       │       ├─────────────────────┤")
print(f"│    Home Player 4    │       │       │       │       │       │    Away Player 4    │")
print(f"├─────────────────────┴───────┴───────┼───────┼───────┴───────┴─────────────────────┤")
print(f"│                                     │ Score │                                     │")
print(f"└─────────────────────────────────────┴───────┴─────────────────────────────────────┘")'''
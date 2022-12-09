from ui.menu_frame import MenuFrame
from ui.functions import *

class MatchTableUI(MenuFrame):
	def __init__(self, logic_wrapper, os, match):
		super().__init__(logic_wrapper, os)
		self.match = match
		self.points_list = self.match.results
		
		self.home_team_list = self.match.home_team_players
		self.home_team_name = self.logic_wrapper.get_team(self.match.home_team).name
		self.away_team_list = self.match.away_team_players
		self.away_team_name = self.logic_wrapper.get_team(self.match.away_team).name

		self.match_number = self.match.id
		division = self.logic_wrapper.get_division(self.match.division_id)
		self.league_name = division.name

	def display_menu(self):
		"""Displays match table for a specific match"""

		HOME_TEAM = "Home Team" # Header of "Home Team" column 
		AWAY_TEAM = "Away Team" # Header of "Away Team" column 
		SCORE = "Score" # Header of "Score" column 
		GAME = "Game" # Header of "Games" column 
		HT = 22 # Width of "Home Team" and "Away Team" column
		SC = 7 # Width of "Legs" column
		GM = 7 # Width of "Games" column 

		ts = HT*2+SC*2+GM+4 # Width of match_name title header
		team_names = f"{self.home_team_name} vs {self.away_team_name}"

		table_format = [
			[HOME_TEAM, HT], [SCORE, SC], [GAME, GM], [SCORE, SC], [AWAY_TEAM, HT]
			]
		

		generate_table([[self.league_name, ts]],[[team_names]])

		table_data = []
		
		games = ["501", "501", "501", "501", "301", "C", "501"]

		for i in range(0, len(games)):
			try:
				player_home = self.points_list[i][2]
			except IndexError:
				player_home = ""
			try:
				player_away = self.points_list[i][3]
			except IndexError:
				player_away = ""
			try:
				points_home = f"{self.points_list[i][0]}"
			except IndexError:
				points_home = ""
			try:
				points_away = f"{self.points_list[i][1]}"
			except IndexError:
				points_away = ""
			game = games[i]
			column = [
			player_home, points_home, game, points_away, player_away
			]
			table_data.append(column)
		try:
			points_away = 0
			points_home = 0
			for j in range(0,7):
				if self.points_list[i][0] == "2":
					points_home += 1
				elif self.points_list[i][1] == "2":
					points_away += 1
			points_away = str(points_away)
			points_home = str(points_home)
		except IndexError:
			points_home = ""
			points_away = ""
		game = "Total"
		column = [
		self.home_team_name, points_home, game, points_away, self.away_team_name
		]
		table_data.append(column)
		generate_table(table_format, table_data)

		home_team = self.home_team_name
		away_team = self.away_team_name
		teams_table_format = [[home_team, HT], ["Quality Points", 15], [away_team, HT], ["Quality Points", 15]]
		teams_table_data = []
		for i in range(4):
			if self.home_team_list and self.away_team_list:
				column = [self.home_team_list[i], "", self.away_team_list[i], ""]
			else:
				column = ["", "", "", ""]
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
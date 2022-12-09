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

		self.quality_points = self.match.quality_points
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
				if len(self.points_list[i]['home_plr']) == 1:
					player_home = self.logic_wrapper.get_player(self.points_list[i]['home_plr'][0])
					player_home_name = player_home.name
				else:
					player_home_name = []
					for j in range(len(self.points_list[i]['home_plr'])):
						player_home_temp = self.logic_wrapper.get_player(self.points_list[i]['home_plr'][j])
						player_home = player_home_temp.name
						player_home_name.append(player_home)
			except IndexError:
				player_home_name = ""
			try:
				if len(self.points_list[i]['away_plr']) == 1:
					player_away = self.logic_wrapper.get_player(self.points_list[i]['away_plr'][0])
					player_away_name = player_away.name
				else:
					player_away_name = []
					for j in range(len(self.points_list[i]['away_plr'])):
						player_away_temp = self.logic_wrapper.get_player(self.points_list[i]['away_plr'][j])
						player_away = player_away_temp.name
						player_away_name.append(player_away)
			except IndexError:
				player_away_name = ""
			try:
				points_home = f"{self.points_list[i]['result'][0]}"
			except IndexError:
				points_home = ""
			try:
				points_away = f"{self.points_list[i]['result'][1]}"
			except IndexError:
				points_away = ""
			game = games[i]
			column = [
			player_home_name, points_home, game, points_away, player_away_name
			]
			table_data.append(column)
		try:
			points_away = 0
			points_home = 0
			for j in range(0,7):
				if self.points_list[i]['result'][0] == 2:
					points_home += 1
				elif self.points_list[i]['result'][1] == 2:
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
		teams_table_format = [[home_team, HT], ["Quality Points", 16], [away_team, HT], ["Quality Points", 16]]
		teams_table_data = []
		for i in range(4):
			if self.home_team_list and self.away_team_list:
				home_team_player = self.logic_wrapper.get_player(self.home_team_list[i])
				home_team_player_name = home_team_player.name
				away_team_player = self.logic_wrapper.get_player(self.away_team_list[i])
				away_team_player_name = away_team_player.name
				try:
					home_team_player_qp = self.quality_points[self.home_team_list[i]]
				except KeyError:
					home_team_player_qp = ""
				try:
					away_team_player_qp = self.quality_points[self.away_team_list[i]]
				except KeyError:
					away_team_player_qp = ""
				column = [home_team_player_name, home_team_player_qp, away_team_player_name, away_team_player_qp]
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
			choice = choice.strip().lower()

			match choice:
				case "q":
					break

				case _:
					input("Invalid Input!")
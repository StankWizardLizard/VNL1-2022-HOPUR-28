from ui.menu_frame import MenuFrame
from models.team_mdl import TeamMdl
from ui.functions import *

class CreateTeamUI(MenuFrame):
	def __init__(self, logic_wrapper, os):
		super().__init__(logic_wrapper, os)


	def display_clubs_menu(self,clubs:list=[], showing_page:int=0):
# 		"""Display the the menu screen onto the terminal"""
# 		print("Select club to start")
# 		print("""
# ┌────┬─────────────────────────────────┐
# │ Nr │ Club Names                      │""")

# 		for i, club in enumerate(clubs):
# 			print(f"""├────┼─────────────────────────────────┤\n│ {i:^5}) │{club.name:^33}│""")

# 		print("""└────┴─────────────────────────────────┘""")
# 		print("Select (N)ext or club")
		"""Display the menu screen for the  clubs"""
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


	def _number_of_team_members(self):
			print("How many team members (must atleast be 4)?")
			number_of_team_members = int(input("> "))
			while number_of_team_members <4:
				number_of_team_members = input("invalid number of team members. Try again \n >")
			return number_of_team_members

	def _display_player_menu(self,players_list):
			
		self.clear_menu()
		print("Select players of team")
		print("""
┌────┬─────────────────────────────────┐
│ Nr │ Player Names                      │""")

		for i, player in enumerate(players_list):
			print(f"""├────┼─────────────────────────────────┤\n│ {i}) │{player.name:^33}│""")

		print("""└────┴─────────────────────────────────┘""")
		print("Select (N)ext or player")
	
	def _write_new_team_to_storage(self,team_name):
		"""Sends new team to logic layer for writing to storage"""
		return self.logic_wrapper.create_team(TeamMdl(name=team_name))

	def _sanitize_inputs(self,input,isInt = False, isStr = False,):
		pass


	def prompt_option(self, showing_page=0):
		"""Prompts the user to choose an option from a list of options for the match table"""
		while True:
			#select club
			self.clear_menu()
			clubs = self.logic_wrapper.get_all_clubs()
			self.display_clubs_menu(clubs, showing_page=showing_page)
			print(display_menu_options(len(clubs)//10, showing_page=showing_page))
			select_club_choice = input(">")
			match select_club_choice:
				case "q":
					break
				case "n":
					showing_page += 1
					continue
				case "b":
					showing_page -= 1
					continue
			if select_club_choice.isnumeric():
				club_selected = clubs[int(select_club_choice)-1]
			team_id = self._write_new_team_to_storage(input("Enter Team Name: "))
			#create team
			players_of_club = self.logic_wrapper.get_players_by_club(club_selected)
			for i in range(self._number_of_team_members()):
				self._display_player_menu(players_of_club)
				teammember_index = i+1
				if i == 0:
					i = int(get_input(f"Enter Captains TeamMember #{teammember_index} Index",number=True))
					player_id = players_of_club[i-1].id
					self.logic_wrapper.add_player_to_team(player_id,team_id)
					self.logic_wrapper.promote_player(player_id,team_id)	
				else:
					i = int(get_input(f"Enter TeamMember #{teammember_index} Index",number=True))
					player_id = players_of_club[i-1].id
					self.logic_wrapper.add_player_to_team(player_id,team_id)
			choice = input("Make another team with the same club or go back?")
			
			match choice:
				case "1":
					pass
				case "2":
					break

'''from ui.menu_frame import MenuFrame
from models.team_mdl import TeamMdl
from ui.functions import *

class CreateTeamUI(MenuFrame):
	def __init__(self, logic_wrapper, os):
		super().__init__(logic_wrapper, os)


	def display_clubs_menu(self,clubs:list=[], showing_page:int=0):
# 		"""Display the the menu screen onto the terminal"""
# 		print("Select club to start")
# 		print("""
# ┌────┬─────────────────────────────────┐
# │ Nr │ Club Names                      │""")

# 		for i, club in enumerate(clubs):
# 			print(f"""├────┼─────────────────────────────────┤\n│ {i:^5}) │{club.name:^33}│""")

# 		print("""└────┴─────────────────────────────────┘""")
# 		print("Select (N)ext or club")
		"""Display the menu screen for the  clubs"""
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


	def _number_of_team_members(self):
			print("How many team members (must atleast be 4)?")
			number_of_team_members = int(input("> "))
			while number_of_team_members <4:
				number_of_team_members = input("invalid number of team members. Try again \n >")
			return number_of_team_members

	def _display_player_menu(self,players_list, showing_page = 0):
			
		self.clear_menu()
		print("Select players of team")
		table_format = [["NR", 4], ["Player Names", 40]]

		table_data = []
		for i, player in enumerate(players_list[showing_page*10:showing_page*10+10]):
			table_data.append([str(i+1), player.name])
		generate_table(table_format=table_format, table_data=table_data)
	
	def _write_new_team_to_storage(self,team_name):
		"""Sends new team to logic layer for writing to storage"""
		return self.logic_wrapper.create_team(TeamMdl(name=team_name))

	def _sanitize_inputs(self,input,isInt = False, isStr = False,):
		pass


	def prompt_option(self, showing_page=0):
		"""Prompts the user to choose an option from a list of options for the match table"""
		while True:
			#select club
			self.clear_menu()
			clubs = self.logic_wrapper.get_all_clubs()
			self.display_clubs_menu(clubs, showing_page=showing_page)
			print(display_menu_options(len(clubs)//10, showing_page=showing_page), "or select club by number")
			select_club_choice = input(">")
			match select_club_choice:
				case "q":
					break
				case "n":
					showing_page += 1
					continue
				case "b":
					showing_page -= 1
					continue
			if select_club_choice.isnumeric():
				club_selected = clubs[int(select_club_choice)-1]
			team_id = self._write_new_team_to_storage(input("Enter Team Name: "))
			#create team
			players_of_club = self.logic_wrapper.get_players_by_club(club_selected)
			for i in range(self._number_of_team_members()):
				self._display_player_menu(players_of_club, showing_page)
				teammember_index = i+1
				if i == 0:
					choice = int(get_input(f"Select Captain: ",number=True))
					player_id = players_of_club[choice-1].id
					self.logic_wrapper.add_player_to_team(player_id,team_id)
					self.logic_wrapper.promote_player(player_id,team_id)
					del players_of_club[choice-1]
				else:
					choice = int(get_input(f"Select TeamMember #{teammember_index}: ",number=True))
					player_id = players_of_club[choice-1].id
					self.logic_wrapper.add_player_to_team(player_id,team_id)
					del players_of_club[choice-1]
			choice = input("Make another team with the same club or go back? y for yes anything else for no: ")
			match choice:
				case "y":
					pass
				case _:
					input("Invalid input!")'''
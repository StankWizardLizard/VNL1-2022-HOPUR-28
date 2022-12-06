from ui.menu_frame import MenuFrame
from models.team_mdl import TeamMdl
class CreateTeamUI(MenuFrame):
	def __init__(self, logic_wrapper, os):
		super().__init__(logic_wrapper, os)


	def display_clubs_menu(self,clubs):
		"""Display the the menu screen onto the terminal"""
		print("Select club to start")
		print("""
┌────┬─────────────────────────────────┐
│ Nr │ Club Names                      │""")

		for i, club in enumerate(clubs):
			print(f"""├────┼─────────────────────────────────┤\n│ {i}) │{club.name:^33}│""")

		print("""└────┴─────────────────────────────────┘""")
		print("Select (N)ext or club")


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


	def prompt_option(self):
		"""Prompts the user to choose an option from a list of options for the match table"""
		while True:
			#select club
			self.clear_menu()
			clubs = self.logic_wrapper.get_all_clubs()
			self.display_clubs_menu(clubs)
			club_selected = clubs[int(input(">"))]
			team_id = self._write_new_team_to_storage(input("Enter Team Name: "))
			#create team
			players_of_club = self.logic_wrapper.get_players_by_club(club_selected)
			for i in range(self._number_of_team_members()):
				self._display_player_menu(players_of_club)
				teammember_index = i+1
				if i == 0:
					print(f"Enter Captains TeamMember #{teammember_index} Name")
					player_id = players_of_club[int(input(">"))].id
					self.logic_wrapper.add_player_to_team(player_id,team_id)
					self.logic_wrapper.promote_player(player_id,team_id)	
				else:
					print(f"Enter TeamMember #{teammember_index} Name")
					player_id = players_of_club[int(input(">"))].id
					self.logic_wrapper.add_player_to_team(player_id,team_id)
			choice = input("Make another team with the same club or go back?")
			
			match choice:
				case "1":
					pass
				case "2":
					break


			



			
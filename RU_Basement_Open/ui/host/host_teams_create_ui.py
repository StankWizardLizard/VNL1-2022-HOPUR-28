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



	def prompt_option(self):
		"""Prompts the user to choose an option from a list of options for the match table"""
		while True:
			#select club
			self.clear_menu()
			clubs = self.logic_wrapper.get_all_clubs()
			self.display_clubs_menu(clubs)
			club_selected = clubs[int(input(">"))]
			print(club_selected)
			team_name = input("Enter Team Name: ")
			#create team
			players_of_club = self.logic_wrapper.get_players_by_club(club_selected)
			team_members = []
			for i in range(self._number_of_team_members()):
				teammember_index = i+1
				if i == 0:
					self._display_player_menu(players_of_club)
					print(f"Enter Captains TeamMember #{teammember_index} Name")
					players_of_club[int(input(">"))].captain=True	
					team_members.append(players_of_club[int(input(">"))])	
				else:
					print(f"Enter TeamMember #{teammember_index} Name")
					team_members.append(players_of_club[int(input(">"))])	

			print("selected team members", team_name," ",team_members)

			choice = input("Make another team with the same club or go back?")
			
			match choice:
				case "1":
					pass
				case "2":
					break


			



			
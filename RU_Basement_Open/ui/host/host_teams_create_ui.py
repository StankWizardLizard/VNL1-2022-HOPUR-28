from ui.menu_frame import MenuFrame
from models.team_mdl import TeamMdl
from ui.functions import get_input


class CreateTeamUI(MenuFrame):
    def __init__(self, logic_wrapper, os):
        super().__init__(logic_wrapper, os)

    def display_clubs_menu(self, clubs):
        """Display the the menu screen onto the terminal"""
        print("Select club to start")
        print("""
┌────┬─────────────────────────────────┐
│ Nr │ Club Names                      │""")

        for i, club in enumerate(clubs):
            print(
                f"""├────┼─────────────────────────────────┤\n│ {i+1}) │{club.name:^33}│""")

        print("""└────┴─────────────────────────────────┘""")
        print("Select (N)ext, (Q)uit or club")


    def _display_player_menu(self, players_list):
        print("""
┌────┬─────────────────────────────────┐
│ Nr │ Player Names                    │""")

        for i, player in enumerate(players_list):
            print(
                f"""├────┼─────────────────────────────────┤\n│ {i+1}) │{player.name:^33}│""")

        print("""└────┴─────────────────────────────────┘""")

    def _write_new_team_to_storage(self, team_name):
        """Sends new team to logic layer for writing to storage"""
        return self.logic_wrapper.create_team(TeamMdl(name=team_name))

    def _sanitize_inputs(self, input, isInt=False, isStr=False,):
        pass

    def prompt_option(self):
        """Prompts the user to choose an option from a list of options for the match table"""
        while True:
            # select club
            self.clear_menu()
            clubs = self.logic_wrapper.get_all_clubs()
            self.display_clubs_menu(clubs)
            back = False
            
            while True:
                choice = get_input(" > ")
                if choice.lower() == "q":
                    back = True
                    break
                
                try:
                    club_selected = clubs[int(choice) - 1]
                    players_of_club = self.logic_wrapper.get_players_by_club(club_selected)
                    if len(players_of_club) >= 4:
                        break
                    print("Selected club does not have enough players, select a club with atleast 4 players")
                        
                except IndexError:
                    print("Invalid id, try again...")
                except ValueError:
                    print(f"{choice} is not a number")
            # If user chose quit, xit team creation menu
            if back:
                break
            
            self.clear_menu()
            print(f"Club selected: {club_selected.name}\n")

            while True:
                team_name = get_input("Enter Team Name: ")
                a = self.logic_wrapper.team_name_exists_on_club(team_name, club_selected.id)
                if not a:
                    break
                print(f"A team with name {team_name} already exists on {club_selected.name}, try again...")
            team_id = self._write_new_team_to_storage(team_name)
            self.logic_wrapper.add_team_to_club(team_id, club_selected.id)
                
            #create team
            added_players = []
            player_counter = 0
            while True:
                #Print avalable
                print(f"Select players to participate in {team_name}")
                self._display_player_menu(players_of_club)
                print("Added players: ")
                self._display_player_menu(added_players)
                
                try:
                    if player_counter == 0:
                        string = f"Choose player {player_counter+1}. This player will be the team captain"
                    else: 
                        string = f"Choose player {player_counter+1}, press 'q' when done" 
                    
                    print(string)
                    choice = get_input(" > ")
                    if choice.lower() == "q":
                        # User cannot quit unless atleast two teams are selected
                        if player_counter < 4:
                            print("Please choose atleast 4 players")
                            continue
                        break
                    i = int(choice)-1
                    player_id = players_of_club[i].id
                    added_players.append(players_of_club.pop(i))
                    self.logic_wrapper.add_player_to_team(player_id,team_id)
                    if player_counter == 0:
                        self.logic_wrapper.promote_player(player_id,team_id)
                    player_counter += 1
                    self.clear_menu()
                except IndexError:
                    print(f"index {choice} is out of range, try again...")
                except ValueError:
                    print(f"{choice} is not a number") 
            
            print("Make another team with the same club? y for yes and any for no ")
            choice = input(" > ")
            
            match choice.strip().lower():
                case "y":
                    pass
                case _:
                    break


            



			
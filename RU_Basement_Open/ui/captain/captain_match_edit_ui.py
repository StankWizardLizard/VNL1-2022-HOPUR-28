from ui.menu_frame import MenuFrame

# --------- TODO ---------- #
# Finish the Singles function
# Finish the Duos function
# Finish the Quads functions
# Function to save Data to file
# Function to read Data from file

class MatchEditUI(MenuFrame):
    def __init__(self, logic_wrapper, os, match):
        super().__init__(logic_wrapper, os)
        self.match = match

        self.points_list = [["","","",""],["","","",""],["","","",""],["","","",""],["","","",""],["","","",""],["","","",""]]
        self.player_list = [("",""),("",""),("",""),("",""),("",""),("",""),("",""),("",""),("",""),("",""),("",""),("","")]


    def display_menu(self):
        """Displays match table for a specific match"""

        Table = f"""
┌──────────────────────────────────────────┬───────┬───────┬───────┬───────┬───────┬──────────────────────────────────────────┐
│{self.match.home_team:^42}│ Leg 1 │ Leg 2 │ Games │ Leg 2 │ Leg 1 │{self.match.away_team:^42}│
├──────────────────────────────────────────┼───────┼───────┼───────┼───────┼───────┼──────────────────────────────────────────┤
│{self.player_list[0][0]:^42}│{self.points_list[0][0]:^7}│{self.points_list[0][1]:^7}│  501  │{self.points_list[0][2]:^7}│{self.points_list[0][3]:^7}│{self.player_list[0][1]:^42}│
├──────────────────────────────────────────┼───────┼───────┼───────┼───────┼───────┼──────────────────────────────────────────┤
│{self.player_list[1][0]:^42}│{self.points_list[1][0]:^7}│{self.points_list[1][1]:^7}│  501  │{self.points_list[1][2]:^7}│{self.points_list[1][3]:^7}│{self.player_list[1][1]:^42}│
├──────────────────────────────────────────┼───────┼───────┼───────┼───────┼───────┼──────────────────────────────────────────┤
│{self.player_list[2][0]:^42}│{self.points_list[2][0]:^7}│{self.points_list[2][1]:^7}│  501  │{self.points_list[2][2]:^7}│{self.points_list[2][3]:^7}│{self.player_list[2][1]:^42}│
├──────────────────────────────────────────┼───────┼───────┼───────┼───────┼───────┼──────────────────────────────────────────┤
│{self.player_list[3][0]:^42}│{self.points_list[3][0]:^7}│{self.points_list[3][1]:^7}│  501  │{self.points_list[3][2]:^7}│{self.points_list[3][3]:^7}│{self.player_list[3][1]:^42}│
╞══════════════════════════════════════════╪═══════╪═══════╪═══════╪═══════╪═══════╪══════════════════════════════════════════╡
│{self.player_list[4][0]:^42}│       │       │       │       │       │{self.player_list[4][1]:^42}│
├──────────────────────────────────────────┤{self.points_list[4][0]:^7}│{self.points_list[4][1]:^7}│  301  │{self.points_list[4][2]:^7}│{self.points_list[4][3]:^7}├──────────────────────────────────────────┤
│{self.player_list[5][0]:^42}│       │       │       │       │       │{self.player_list[5][1]:^42}│
├──────────────────────────────────────────┼───────┼───────┼───────┼───────┼───────┼──────────────────────────────────────────┤
│{self.player_list[6][0]:^42}│       │       │       │       │       │{self.player_list[6][1]:^42}│
├──────────────────────────────────────────┤{self.points_list[5][0]:^7}│{self.points_list[5][1]:^7}│   C   │{self.points_list[5][2]:^7}│{self.points_list[5][3]:^7}├──────────────────────────────────────────┤
│{self.player_list[7][0]:^42}│       │       │       │       │       │{self.player_list[7][1]:^42}│
╞══════════════════════════════════════════╪═══════╪═══════╪═══════╪═══════╪═══════╪══════════════════════════════════════════╡
│{self.player_list[8][0]:^42}│       │       │       │       │       │{self.player_list[8][1]:^42}│
├──────────────────────────────────────────┤       │       │       │       │       ├──────────────────────────────────────────┤
│{self.player_list[9][0]:^42}│       │       │       │       │       │{self.player_list[9][1]:^42}│
├──────────────────────────────────────────┤{self.points_list[6][0]:^7}│{self.points_list[6][1]:^7}│  501  │{self.points_list[6][2]:^7}│{self.points_list[6][3]:^7}├──────────────────────────────────────────┤
│{self.player_list[10][0]:^42}│       │       │       │       │       │{self.player_list[10][1]:^42}│
├──────────────────────────────────────────┤       │       │       │       │       ├──────────────────────────────────────────┤
│{self.player_list[11][0]:^42}│       │       │       │       │       │{self.player_list[11][1]:^42}│
├──────────────────────────────────────────┴───────┴───────┼───────┼───────┴───────┴──────────────────────────────────────────┤
│                                                          │ Score │                                                          │
└──────────────────────────────────────────────────────────┴───────┴──────────────────────────────────────────────────────────┘
"""
        print(Table)



    def get_points(self):
        """Get points from the user"""
        while True:
            # get points from user
            for game in self.points_list:
                for point in range(0,4):

                    game[point] = input(f"Input Leg point: ")

                    self.clear_menu()
                    self.display_menu()

            choice = input("would you like to save the table? (y for yes and any for no): ")
            choice = choice.lower()

            match choice:
                case "y":
                    # Save info about the match and quit the window
                    break

                case "n":
                    # Dont save info about the match
                    points = [(2,1),(1,2),(2,2),(0,0)]
                    self.points_list = [["","","",""],["","","",""],["","","",""],["","","",""],["","","",""],["","","",""],["","","",""]]

                case _:
                    break



    def display_player_table(self, player_list):
        """Displays a table of a given player list"""

        print("┌────┬──────────────────────────────────────────┐")
        print("│ NR │                   Name                   │")

        try:
            for current_player_number in range(0, len(player_list)):
                print("├────┼──────────────────────────────────────────┤")
                print(f"│{current_player_number+1:^4}│{player_list[current_player_number]:^42}│")
        except IndexError:
            pass

        print("└────┴──────────────────────────────────────────┘")



    def pick_players_from_list(self,team_list):
        """Given a list of players, let user choose one and return it"""
        # Get Matchup for Home team
        while True:
            
            # Clear Menu and display match table and team table
            self.clear_menu()
            self.display_menu()
            self.display_player_table(team_list)

            # Let user choose a player to add
            player_choice = input(" > ")

            if(player_choice.isdecimal()):
                
                player_choice = int(player_choice) - 1
                
                if(player_choice >= 0 and len(team_list)-1 >= player_choice):
                
                    # Picked player gets saved
                    player = team_list[player_choice]

                    # remove the player from the list of available players
                    team_list.remove(team_list[player_choice])        

                    break

                else:
                    input("Invalid Input!")
            else:
                input("Invalid Input!")
        
        return player



    def get_matchup(self):
        """Get the player matchup from the user and update the table"""
        while True:

            # Create copies of Home and Away team list
            home_team = [x for x in self.match.home_team_players]
            away_team = [x for x in self.match.away_team_players]

            # Singles Matchup
            for match_number in range(0,4):

                # Pick from Home
                home_player = self.pick_players_from_list(home_team)

                # Save player
                self.player_list[match_number] = (home_player, "")

                # Pick from Away
                away_player = self.pick_players_from_list(away_team)

                # Save player
                self.player_list[match_number] = (home_player, away_player)

            # Create copies of Home and Away team list
            home_team = [x for x in self.match.home_team_players]
            away_team = [x for x in self.match.away_team_players]

            # Duos Matchup 
            for match_number in range(4,8):
                # Pick from Home
                home_player = self.pick_players_from_list(home_team)

                # Save player
                self.player_list[match_number] = (home_player, "")

                # Pick from Away
                away_player = self.pick_players_from_list(away_team)

                # Save player
                self.player_list[match_number] = (home_player, away_player)                

            # Quads Matchup
            self.player_list[8:12] = self.player_list[0:4]

            self.clear_menu()
            self.display_menu()

            choice = input("would you like to save the table? (y for yes and any for no): ")
            choice = choice.lower()

            match choice:
                case "y":
                    # Save info about the match
                    break

                case _:
                    # Dont save info about the match
                    self.player_list = [("",""),("",""),("",""),("",""),("",""),("",""),("",""),("",""),("",""),("",""),("",""),("","")]



    def prompt_option(self):
        """"Prompts Captain to input match data"""
        while True:

            self.clear_menu()
            self.display_menu()
            self.get_matchup()
            self.get_points()
            
            input()
            break

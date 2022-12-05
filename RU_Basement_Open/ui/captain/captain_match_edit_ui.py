from ui.menu_frame import MenuFrame

class MatchEditUI(MenuFrame):
    def __init__(self, logic_wrapper, os, match):
        super().__init__(logic_wrapper, os)
        self.match = match
        self.points_list = [["","","",""],["","","",""],["","","",""],["","","",""],["","","",""],["","","",""],["","","",""]]
        
        self.home_team_list = self.match.home_team_players
        self.home_team_name = self.match.home_team
        self.away_team_list = self.match.away_team_players
        self.away_team_name = self.match.away_team

    def display_menu(self):
        """Displays match table for a specific match"""

        match_name = "HR Basement Match nr 1"

        print(f"{match_name}")
        print(f"┌─────────────────────┬───────┬───────┬───────┬───────┬───────┬─────────────────────┐")
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
        print(f"└─────────────────────────────────────┴───────┴─────────────────────────────────────┘")

        print(dir(self.match))
        print("HOME")
        print(self.match.home_team)
        print(self.match.home_team_players)
        print("AWAY")
        print(self.match.away_team)
        print(self.match.away_team_players)


    def prompt_option(self):
        """"Prompts Captain to input match data"""
        while True:

            self.clear_menu()
            self.display_menu()

            # collect info of match
            for game in self.points_list:
            
                for i in range(0,4):

                    game[i] = input(f"Results for Leg{i+1}: ")

                    self.clear_menu()
                    self.display_menu()


            choice = input("would you like to save the table? (y for yes and any for no): ")
            choice = choice.lower()

            match choice:
                case "y":
                    # Save and break
                    pass

                case "n":
                    pass

                case _:
                    break
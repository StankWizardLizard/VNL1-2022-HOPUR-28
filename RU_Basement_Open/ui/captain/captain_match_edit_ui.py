from ui.menu_frame import MenuFrame

class MatchEditUI(MenuFrame):
    def __init__(self, logic_wrapper, os):
        super().__init__(logic_wrapper, os)

    def display_menu(self, points_list):
        """Displays match table for a specific match"""

        # This is how the points list would look like
        points_list = [
            [2,2,5,5], # represents the first game
            [5,2,2,5], # represents the second game
            [5,5,2,2], # ...
            [2,5,5,2],
            [2,2,2,2],
            [5,5,5,5],
            [4,1,0,3]  # represents the last game
            ]
        
        match_name = "HR Basement Match nr 1"

        print(f"{match_name}")
        print(f"┌─────────────────────┬───────┬───────┬───────┬───────┬───────┬─────────────────────┐")
        print(f"│      Home Team      │ Leg 1 │ Leg 2 │ Games │ Leg 2 │ Leg 1 │      Away Team      │")
        print(f"├─────────────────────┼───────┼───────┼───────┼───────┼───────┼─────────────────────┤")
        print(f"│    Home Player 1    │{points_list[0][0]:^7}│{points_list[0][1]:^7}│  501  │{points_list[0][2]:^7}│{points_list[0][3]:^7}│    Away Player 1    │")
        print(f"├─────────────────────┼───────┼───────┼───────┼───────┼───────┼─────────────────────┤")
        print(f"│    Home Player 2    │{points_list[1][0]:^7}│{points_list[1][1]:^7}│  501  │{points_list[1][2]:^7}│{points_list[1][3]:^7}│    Away Player 2    │")
        print(f"├─────────────────────┼───────┼───────┼───────┼───────┼───────┼─────────────────────┤")
        print(f"│    Home Player 3    │{points_list[2][0]:^7}│{points_list[2][1]:^7}│  501  │{points_list[2][2]:^7}│{points_list[2][3]:^7}│    Away Player 3    │")
        print(f"├─────────────────────┼───────┼───────┼───────┼───────┼───────┼─────────────────────┤")
        print(f"│    Home Player 4    │{points_list[3][0]:^7}│{points_list[3][1]:^7}│  501  │{points_list[3][2]:^7}│{points_list[3][3]:^7}│    Away Player 4    │")
        print(f"╞═════════════════════╪═══════╪═══════╪═══════╪═══════╪═══════╪═════════════════════╡")
        print(f"│    Home Player 1    │       │       │       │       │       │    Away Player 3    │")
        print(f"├─────────────────────┤{points_list[4][0]:^7}│{points_list[4][1]:^7}│  301  │{points_list[4][2]:^7}│{points_list[4][3]:^7}├─────────────────────┤")
        print(f"│    Home Player 2    │       │       │       │       │       │    Away Player 4    │")
        print(f"├─────────────────────┼───────┼───────┼───────┼───────┼───────┼─────────────────────┤")
        print(f"│    Home Player 3    │       │       │       │       │       │    Away Player 1    │")
        print(f"├─────────────────────┤{points_list[5][0]:^7}│{points_list[5][1]:^7}│   C   │{points_list[5][2]:^7}│{points_list[5][3]:^7}├─────────────────────┤")
        print(f"│    Home Player 4    │       │       │       │       │       │    Away Player 2    │")
        print(f"╞═════════════════════╪═══════╪═══════╪═══════╪═══════╪═══════╪═════════════════════╡")
        print(f"│    Home Player 1    │       │       │       │       │       │    Away Player 1    │")
        print(f"├─────────────────────┤       │       │       │       │       ├─────────────────────┤")
        print(f"│    Home Player 2    │       │       │       │       │       │    Away Player 2    │")
        print(f"├─────────────────────┤{points_list[6][0]:^7}│{points_list[6][1]:^7}│  501  │{points_list[6][2]:^7}│{points_list[6][3]:^7}├─────────────────────┤")
        print(f"│    Home Player 3    │       │       │       │       │       │    Away Player 3    │")
        print(f"├─────────────────────┤       │       │       │       │       ├─────────────────────┤")
        print(f"│    Home Player 4    │       │       │       │       │       │    Away Player 4    │")
        print(f"├─────────────────────┴───────┴───────┼───────┼───────┴───────┴─────────────────────┤")
        print(f"│                                     │ Score │                                     │")
        print(f"└─────────────────────────────────────┴───────┴─────────────────────────────────────┘")


    def prompt_option(self):
        """"Prompts Captain to input match data"""
        while True:
            self.clear_menu()
            self.display_menu([])

            choice = input("would you like to save the table? (y for yes and any for no): ")
            choice = choice.lower()

            match choice:
                case "y":
                    pass

                case "n":
                    pass

                case _:
                    break
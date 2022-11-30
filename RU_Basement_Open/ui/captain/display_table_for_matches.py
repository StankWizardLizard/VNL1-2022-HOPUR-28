class DisplayTableForMatchesUI:
    def __init__(self, logic_wrapper, os):
        self.logic_wrapper = logic_wrapper
        self.os = os


    def clear_menu(self):
        """Clears the menu screen"""
        if(self.os.name == "nt"):
            self.os.system("cls")
        else:
            self.os.system("clear")


    def display_menu(self):
        """
        Displays match table for a specific match
        """
        print("HR Basement Match nr 1")
        print("┌─────────────────────┬───────┬───────┬───────┬───────┬───────┬─────────────────────┐")
        print("│      Home Team      │ Leg 1 │ Leg 2 │ Games │ Leg 2 │ Leg 1 │      Away Team      │")
        print("├─────────────────────┼───────┼───────┼───────┼───────┼───────┼─────────────────────┤")
        print("│    Home Player 1    │       │       │  501  │       │       │    Away Player 1    │")
        print("├─────────────────────┼───────┼───────┼───────┼───────┼───────┼─────────────────────┤")
        print("│    Home Player 2    │       │       │  501  │       │       │    Away Player 2    │")
        print("├─────────────────────┼───────┼───────┼───────┼───────┼───────┼─────────────────────┤")
        print("│    Home Player 3    │       │       │  501  │       │       │    Away Player 3    │")
        print("├─────────────────────┼───────┼───────┼───────┼───────┼───────┼─────────────────────┤")
        print("│    Home Player 4    │       │       │  501  │       │       │    Away Player 4    │")
        print("╞═════════════════════╪═══════╪═══════╪═══════╪═══════╪═══════╪═════════════════════╡")
        print("│    Home Player 1    │       │       │       │       │       │    Away Player 3    │")
        print("├─────────────────────┤       │       │  301  │       │       ├─────────────────────┤")
        print("│    Home Player 2    │       │       │       │       │       │    Away Player 4    │")
        print("├─────────────────────┼───────┼───────┼───────┼───────┼───────┼─────────────────────┤")
        print("│    Home Player 3    │       │       │       │       │       │    Away Player 1    │")
        print("├─────────────────────┤       │       │   C   │       │       ├─────────────────────┤")
        print("│    Home Player 4    │       │       │       │       │       │    Away Player 2    │")
        print("╞═════════════════════╪═══════╪═══════╪═══════╪═══════╪═══════╪═════════════════════╡")
        print("│    Home Player 1    │       │       │       │       │       │    Away Player 1    │")
        print("├─────────────────────┤       │       │       │       │       ├─────────────────────┤")
        print("│    Home Player 2    │       │       │       │       │       │    Away Player 2    │")
        print("├─────────────────────┤       │       │  501  │       │       ├─────────────────────┤")
        print("│    Home Player 3    │       │       │       │       │       │    Away Player 3    │")
        print("├─────────────────────┤       │       │       │       │       ├─────────────────────┤")
        print("│    Home Player 4    │       │       │       │       │       │    Away Player 4    │")
        print("├─────────────────────┴───────┴───────┼───────┼───────┴───────┴─────────────────────┤")
        print("│                                     │ Score │                                     │")
        print("└─────────────────────────────────────┴───────┴─────────────────────────────────────┘")


    def prompt_option(self):
        """"Prompts Captain to input match data"""
        while True:
            self.clear_menu()
            self.display_menu()
            choice = input(" > ")
            choice = choice.lower()
            
            match choice:
                case _:
                    break
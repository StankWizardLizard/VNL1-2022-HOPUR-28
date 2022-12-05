from ui.menu_frame import MenuFrame
from models.player_mdl import PlayerMdl
import re
import string

def remove_punctuation(input_str):
    """Removes all punctuation and whitespaces from a string"""
    input_str = input_str.translate(str.maketrans('', '', string.punctuation)) # Remove punctuation
    input_str = ''.join(input_str.split()) # Remove whitespaces
    return input_str

def get_input(display_string: str, number: bool = False, email: bool = False):
    """Takes a string to display, asks for user input and does basic validation,
    returns input once it's valid"""
    while True:
        valid = True
        choice = input(display_string).strip()
        # Remove filler characters and check if the user'sm choice is numeric
        if number:
            choice = remove_punctuation(choice)
            if not choice.isnumeric():
                valid = False
        # Check whether the user's choice is a valid email
        if email:
            # Email validating regular expression
            regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            if not (re.fullmatch(regex, choice)):
                valid = False
        # Check whether the user's choice is empty
        if choice == "":
            valid = False
        # Return user's choice if all checks succeded
        if valid:
            return choice
        print(f"{choice}, is an invalid input...")


class CreatePlayerUI(MenuFrame):
    def __init__(self, logic_wrapper, os):
        super().__init__(logic_wrapper, os)

    def display_menu(self):
        """Display the the menu screen onto the terminal"""
        print("Registering New Player")

    def prompt_option(self):
        """Prompts the user to choose an option from a list of options for the match table"""
        while True:
            self.clear_menu()
            self.display_menu()

            print("Select an existing team!")
            teams = self.logic_wrapper.get_all_teams()
            for team in teams:
                print(team.name)

            while True:
                try:
                    team_name = get_input("Team Name: ")
                    team_id = self.logic_wrapper.get_team_id_by_name(team_name)
                    break

                except IndexError:
                    print("Team does not exist")

            name = get_input("Enter Name of new player: ")
            address = get_input("Address of new player: ")
            mobile_nr = get_input("Mobile phone number of player: ", number=True)
            home_nr = get_input("Home phone number of player: ", number= True)
            ssn = get_input("Input national id number of player: ", number=True)
            email = get_input("email address of player: ", email=True)

            choice = input(
                "Would you like to save? (y)es, (q)uit and any for no: ")
            choice = choice.lower()

            match choice:
                # if user wants to save the the club info
                case "y":
                    # save info
                    player_id = PlayerMdl(name=name, ssn=ssn, mobile_nr=mobile_nr,
                                          home_nr=home_nr, address=address, email=email, team_id=team_id)
                    self.logic_wrapper.create_player(player_id)

                # if user doesnt want to save info
                case "n":
                    # dont save info
                    pass

                # if user wnats to quit
                case "q":
                    break

                # undocumented inputs get disregarded
                case _:
                    input("Invalid Input!")

            choice = input(
                "Would you like to create another player? (y for yes, any for no): ")
            choice = choice.lower()

            match choice:
                # if user wants to add another player
                case "y":
                    pass

                # Undocumented inputs regarded as quit
                case _:
                    break

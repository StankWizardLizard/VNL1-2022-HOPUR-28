from ui.menu_frame import MenuFrame
from models.division_mdl import DivisionMdl
from ui.functions import get_input, get_date_input


class CreateDivisionsUI(MenuFrame):
    def __init__(self, logic_wrapper, os):
        super().__init__(logic_wrapper, os)

    def display_menu(self):
        """Display the the menu screen onto the terminal"""
        print("Registering a new Division")

    def prompt_option(self):
        """Prompts the user to choose an option from a list of options for the match table"""
        while True:
            self.clear_menu()
            self.display_menu()
            # Asks user for all information neccesary to create a new division
            # While True loops ensure that the user can try again if he types an invalid input
            while True:
                name = get_input("Enter name of the new divisions: ")
                if not self.logic_wrapper.division_name_exists(name):
                    break
                print(
                    f"A division with name {name} already exists, try again...")

            host = get_input("Enter name of the host: ")
            phone = get_input("Enter phone number: ", number=True)
            rounds = get_input("Enter ammount of rounds: ", number=True)
            start_date = get_date_input("Enter division start date: ")
            days_between_matchdays = get_input(
                "Enter amount of rest days between match days: ", number=True)
            # User can choose to save or disregard the information he just wrote
            choice = input(
                "Would you like to save? (y)es, (q)uit and any for no: ")
            match choice.lower():
                # if user wants to see the next 10 items
                case "y":
                    # Save info
                    division = DivisionMdl(
                        name=name, host_name=host, phone_nr=phone, rounds=rounds)
                    division_id = self.logic_wrapper.create_division(division)
                    self.clear_menu()
                # if user doesnt want to save info
                case "n":
                    # dont save info
                    continue

                # if user wnats to quit
                case "q":
                    break

                # undocumented inputs get disregarded
                case _:
                    input("Invalid Input!")

            # User chooses which teams he wants to compete
            # List of all avalable teams
            teams = self.logic_wrapper.get_all_teams()
            team_counter = 0
            added_teams = []
            while True:
                # Print avalable teams
                print(f"Select which teams to compete in {name}")
                print("Teams:")  # TODO: gera fallega töflu
                for i, team in enumerate(teams):
                    print(i+1, team.name)
                # Print teams already added
                print("------added teams------")
                for i, team in enumerate(added_teams):
                    print(i+1, team.name)

                try:
                    choice = get_input(
                        "Choose a teams to add to division, press 'q' when done: ")
                    if choice.lower() == "q":
                        # User cannot quit unless atleast two teams are selected
                        if team_counter < 2:
                            print("Please choose atleast 2 teams")
                            continue
                        break
                    i = int(choice)-1
                    team_id = teams[i].id
                    # Moves selected team to a seperate list for added teams
                    added_teams.append(teams.pop(i))
                    self.logic_wrapper.add_team_to_division(
                        team_id, division_id)
                    team_counter += 1
                    self.clear_menu()
                except IndexError:
                    print(f"index {choice} is out of range, try again...")
                except ValueError:
                    print(f"{choice} is not a number")
            # Call to logic layer to automatically generate matches
            self.logic_wrapper.master_logic.generate_division_matches(
                division_id, start_date, int(days_between_matchdays), int(rounds))

            choice = input(
                "Would you like to create another Division? (y for yes, any for no): ")
            match choice.lower():
                # if user wants to add another club
                case "y":
                    pass

                # Undocumented inputs regarded as quit
                case _:
                    break

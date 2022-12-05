from ui.menu_frame import MenuFrame
from models.division_mdl import DivisionMdl
from ui.functions import get_input


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

            while True:
                name = get_input("Enter name of the new divisions: ")
                if not self.logic_wrapper.division_name_exists(name):
                    break
                print(
                    f"A division with name {name} already exists, try again...")

            host = get_input("Enter name of the host: ")
            phone = get_input("Enter phone number: ", number=True)
            rounds = get_input("Enter ammount of rounds: ", number=True)

            choice = input(
                "Would you like to save? (y)es, (q)uit and any for no: ")
            choice = choice.lower()

            match choice:
                # if user wants to see the next 10 items
                case "y":
                    # Save info
                    division = DivisionMdl(
                        name=name, host_name=host, phone_nr=phone, rounds=rounds)
                    division_id = self.logic_wrapper.create_division(division)
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

            # Add teams to division
            teams = self.logic_wrapper.get_all_teams()
            print(f"Select which teams to compete in {name}")
            print("Teams:") # TODO: geta fallega töflu
            for i ,team in enumerate(teams):
                print(i+1, team.name)
            while True:    
                choice = get_input("Choose a team to add to division: ")
                if choice.lower() == "q":
                    break
                i = int(choice)
                team_id = teams[i].id
                self.logic_wrapper.add_team_to_division(team_id, division_id)



            choice = input(
                "Would you like to create another Division? (y for yes, any for no): ")
            choice = choice.lower()

            match choice:
                # if user wants to add another club
                case "y":
                    pass

                # Undocumented inputs regarded as quit
                case _:
                    break

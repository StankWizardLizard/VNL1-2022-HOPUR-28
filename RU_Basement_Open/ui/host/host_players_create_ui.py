from ui.menu_frame import MenuFrame
from models.player_mdl import PlayerMdl


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
            
            while True:
                try:
                    team_name = input("Team Name: ")
                    team_id = self.logic_wrapper.get_team_id_by_name(team_name)
                    
                except IndexError:
                    print("Team does not exist")
                
   
            name = input("Enter Name of new player: ")
            address = input("Address of new player: ")
            mobile_nr = input("Mobile phone number of player: ")
            home_nr = input("Home phone number of player: ")
            ssn = input("Input national id number of player: ")
            email = input("email address of player: ")

            # player_id = PlayerMdl(name=name, ssn=ssn, mobile_nr=mobile_nr,
            #                    home_nr=home_nr, address=address, email=email)
            # self.logic_wrapper.create_player(player_id)
   
            choice = input(
                "Would you like to save? (y)es, (q)uit and any for no: ")
            choice = choice.lower()

            match choice:
                # if user wants to save the the club info
                case "y":
                    # save info
                    pass

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
                # if user wants to add another club
                case "y":
                    pass

                # Undocumented inputs regarded as quit
                case _:
                    break

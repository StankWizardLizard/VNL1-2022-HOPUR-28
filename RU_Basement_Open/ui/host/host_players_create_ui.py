from ui.menu_frame import MenuFrame
from models.player_mdl import PlayerMdl
from ui.functions import get_input
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
            clubs = self.logic_wrapper.get_all_clubs()
            back = False
            
            print("Select a club from the list to register a new player or press 'q' to abort")
            for i, club in enumerate(clubs):
                print(i+1, club.name)

            while True:
                try:
                    choice =  get_input("Club Id: ")
                    if choice.strip().lower() == "q":
                        back = True
                        break
                    
                    club_id = clubs[int(choice)-1].id
                    break
                    
                except IndexError:
                    print("Invalid id, try again...")
                except ValueError:
                    print(f"{choice} is not a number")
            # Exit player creation
            if back:
                break
            self.clear_menu()
            print(f"Registering new player to club: {clubs[int(choice)-1].name}")
            name = get_input("Enter Name of new player: ")
            address = get_input("Address of new player: ")
            mobile_nr = get_input("Mobile phone number of player: ", number=True, length=7)
            home_nr = get_input("Home phone number of player: ", number= True,length=7)
            while True: 
                ssn = get_input("Input national id number of player: ", number=True, length=10)
                if not self.logic_wrapper.player_ssn_exists(ssn):
                    break
                print(f"A player with ssn {ssn} already exists, try again...")
            
            email = get_input("email address of player: ", email=True)

            choice = input(
                "Would you like to save? (y)es, (q)uit and any for no: ")
            choice = choice.strip().lower()

            match choice:
                # if user wants to save the the club info
                case "y":
                    # save info
                    player = PlayerMdl(name=name, ssn=ssn, mobile_nr=mobile_nr,
                                          home_nr=home_nr, address=address, email=email, club_id=club_id)
                    self.logic_wrapper.create_player(player)

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
            choice = choice.strip().lower()

            match choice:
                # if user wants to add another player
                case "y":
                    pass

                # Undocumented inputs regarded as quit
                case _:
                    break

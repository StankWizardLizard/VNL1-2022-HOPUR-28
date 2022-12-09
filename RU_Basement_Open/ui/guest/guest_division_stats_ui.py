from ui.menu_frame import MenuFrame
from ui.guest.guest_division_table_ui import DivisionTableUI
from ui.guest.guest_matches_table_ui import MatchesTableUI
from ui.guest.guest_player_list import PlayerList
from ui.guest.guest_player_qps_ui import QPSTable
from ui.guest.guest_player_inshot_ui import InShotTable
from ui.guest.guest_player_outshot_ui import OutShotTable
from ui.functions import *

class DivisionStatsUI(MenuFrame):
    def __init__(self,logic_wrapper, os,division:DivisionMdl = DivisionMdl("Reykjavik Open")):
        super().__init__(logic_wrapper, os)
        self.NR_OF_ENTRIES = 10 #How many entries per page
        self.division = division

    def display_menu(self, list_of_all_divisions:list=[], showing_page:int=0):
        """Dsplays the menu screen for the guest"""    	
        print("┌─────────────────────────┐")
        print("│1) Unplayed Matches      │")
        print("│2) Played Matches        │")
        print("│3) Division Table        │")
        print("│4) Player List           │")
        print("│5) Player Quality Points │")
        print("│6) Player Inshots        │")
        print("│7) Player Outshots       │")
        print("│                         │")
        print("│                         │")
        print("│q) Back                  │")
        print("└─────────────────────────┘")
        
    def prompt_option(self, showing_page:int=0):
        '''Prompts the user to choose an option from a list of options for the divisions table'''
        list_of_divisions = self.logic_wrapper.get_all_divisions()
        pages_number = len(list_of_divisions)//self.NR_OF_ENTRIES
        while True:
            self.clear_menu()
            self.display_menu(list_of_divisions, showing_page=showing_page)
            print(display_menu_options(how_many_pages=pages_number, showing_page=showing_page))
            choice = input(" > ")
            choice = choice.lower()

            match choice:
                case "1":
                    unplayed_matches_ui = MatchesTableUI(self.logic_wrapper,self.os, False,self.division)
                    unplayed_matches_ui.prompt_option()
                case "2":
                    played_matches_ui = MatchesTableUI(self.logic_wrapper,self.os, True,self.division)
                    played_matches_ui.prompt_option()
                case "3":
                    divisions_table_ui = DivisionTableUI(self.logic_wrapper,self.os,self.division) 
                    divisions_table_ui.prompt_option()
                case "4":
                    player_list = PlayerList(self.logic_wrapper,self.os,self.division)
                    player_list.prompt_option()
                case "5":
                    player_qps = QPSTable(self.logic_wrapper,self.os,self.division)
                    player_qps.prompt_option()
                case "6":
                    player_inshot= InShotTable(self.logic_wrapper,self.os,self.division)
                    player_inshot.prompt_option()
                case "7":
                    player_outshot = OutShotTable(self.logic_wrapper,self.os,self.division)
                    player_outshot.prompt_option()
                case "q":
                   break 


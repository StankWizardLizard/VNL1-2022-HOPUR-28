from ui.menu_frame import MenuFrame
from ui.functions import *

class EditDivisionUI(MenuFrame):
    def __init__(self, logic_wrapper, os, division):
        super().__init__(logic_wrapper, os)
        self.division = division


    def display_menu(self, matches:list=[], showing_page:int=0):
        """Display the menu screen for the  division"""
        print(dir(self.division))
        print(self.division.matches)
        input()
        NUMBER = "NR"
        DIVISION_MATCHES_NAME = "Division Matches"
        NR = 4 #Length of number box
        DN = 40 #Length of team name box
        print("Divisions")

        #Format of table with a list of lists [row name, row width]
        table_format = [[NUMBER, NR], [DIVISION_MATCHES_NAME, DN]]
        try:
            #Fills in data for table
            table_data = []
            for i in range(showing_page*10, showing_page*10+len(matches[showing_page*10:showing_page*10+10])):
                matches_nr = str(i+1) + ")"
                matches =f"{matches[i]}"
                table_data.append([matches_nr, matches])
            #Generates a table with the correct format and data
            generate_table(table_format, table_data)
        except IndexError:
            generate_table(table_format, [])


    def prompt_option(self, showing_page = 0, id = 1):
        """Prompts the user to choose an option from a list of options for the match table"""
        matches = self.logic_wrapper.get_all_matches()
        pages_number = len(matches)//10
        while True:
            self.clear_menu()
            self.display_menu(matches, showing_page=showing_page)
            print(display_menu_options(how_many_pages=pages_number, showing_page=showing_page))
            choice = input(" > ")
            choice = choice.lower()

            match choice:
                # if user wants to quit
                case "q":
                    break

                # undocumented inputs get disregarded
                case _:
                    continue

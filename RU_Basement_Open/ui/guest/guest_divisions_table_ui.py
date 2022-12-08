from ui.menu_frame import MenuFrame
from ui.guest.guest_division_table_ui import DivisionTableUI
from ui.functions import *

class DivisionsTableUI(MenuFrame):
    def __init__(self,logic_wrapper, os):
        super().__init__(logic_wrapper, os)
        self.NR_OF_ENTRIES = 10 # Number of entries displayed per page 

    def display_menu(self, list_of_all_divisions:list=[], showing_page:int=0):
        """Creates the format for the divisions table then fills in data from list_of_all_divisions 
		and feeds it to generate_table function to print a table for the divsions"""

        # Constants
        NUMBER = "NR" # Header of "Number" column
        DIVISION_NAME = "Division Name" #Header of "Division Name" column
        NR = 4 # Width of "Number" column
        DN = 40 # Width of "Team Name" column

        print("Divisions")

        # Format of table with a list of lists containing strings for each column ex. [[column name, column width], [column name, column width]]
        table_format = [[NUMBER, NR], [DIVISION_NAME, DN]]
        try:
            # Fills in the list data for table with lists containing data for every row (make sure every row has data for all columns)
            table_data = []
            # Range starts from which page you are viewing times how many entries per page,
			# to which page you are viewing times how many entries per page plus how many entries there are in that page.
            for i in range(
                showing_page*self.NR_OF_ENTRIES, 
                showing_page*self.NR_OF_ENTRIES+len(list_of_all_divisions[showing_page*self.NR_OF_ENTRIES:showing_page*self.NR_OF_ENTRIES+self.NR_OF_ENTRIES])
                ):
                division_nr = str(i + 1 + showing_page * self.NR_OF_ENTRIES) + ")"
                division =f"{list_of_all_divisions[i].name}"
                table_data.append([division_nr, division])
            # Generates a table with the correct format and data
            # example:
            # table_format = [[column1 name, column1 width], [column2 name, column2 width]]
			# table_data = [["column1 info", "column2 info"], ["column1 info", "column2 info"]...]
            # generate_table(table_format, table_data)
            generate_table(table_format, table_data)
        except IndexError:
            # Generates an empty table if list_of_all_divisions gives wrong data
            generate_table(table_format, [])


    def prompt_option(self, showing_page:int=0):
        '''Calls the a method to print a table of all divisions then a method to print menu options, 
		then takes input from the user to choose an option from the list of options printed for the divisions table'''
        list_of_divisions = self.logic_wrapper.get_all_divisions()
        pages_number = len(list_of_divisions)//self.NR_OF_ENTRIES
        while True:
            self.clear_menu()
            self.display_menu(list_of_divisions, showing_page=showing_page)
            print(display_menu_options(how_many_pages=pages_number, showing_page=showing_page), "or select division by number")
            choice = input(" > ")
            choice = choice.lower()

            match choice:
                # if user wants to see the next self.NR_OF_ENTRIES items
                case "n":
                    if showing_page == pages_number:
                        input("Invalid Input!")
                    else:
                        showing_page += 1

                # if user wants to see the last self.NR_OF_ENTRIES items
                case "b":
                    if showing_page == 0:
                        input("Invalid Input!")
                    else:
                        showing_page -= 1

                # if user wants to quit to the last page
                case "q":
                    break
                
                # checks if user inputed number of a division and opens DivisionTableUI if they did,
                # otherwise prints invalid input
                case _:
                    if choice.isnumeric():
                        try:
                            if list_of_divisions[int(choice)-1]:
                                division = list_of_divisions[int(choice)-1]
                                division_table_ui = DivisionTableUI(self.logic_wrapper, self.os, division)
                                division_table_ui.prompt_option()
                        except IndexError:
                            input("Invalid Input!")
                    # undocumented inputs get disregarded
                    else:
                        input("Invalid Input!")

'''
print("Divisions")
print("┌────┬──────────────────────────────────────┐")
print("│ NR │ Division Name                        │")
print("├────┼──────────────────────────────────────┤")
print("│100)│ Division Name 1                      │")
print("├────┼──────────────────────────────────────┤")
print("│100)│ Division Name 1                      │")
print("├────┼──────────────────────────────────────┤")
print("│100)│ Division Name 1                      │")
print("├────┼──────────────────────────────────────┤")
print("│100)│ Division Name 1                      │")
print("├────┼──────────────────────────────────────┤")
print("│100)│ Division Name 1                      │")
print("├────┼──────────────────────────────────────┤")
print("│100)│ Division Name 1                      │")
print("├────┼──────────────────────────────────────┤")
print("│100)│ Division Name 1                      │")
print("├────┼──────────────────────────────────────┤")
print("│100)│ Division Name 1                      │")
print("├────┼──────────────────────────────────────┤")
print("│100)│ Division Name 1                      │")
print("├────┼──────────────────────────────────────┤")
print("│100)│ Division Name 1                      │")
print("└────┴──────────────────────────────────────┘")
print("(N)ext page, (B)ack Page, (Q)uit or Division Number")
'''
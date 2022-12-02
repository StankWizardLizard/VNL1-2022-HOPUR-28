from ui.menu_frame import MenuFrame
from ui.guest.guest_division_table_ui import DivisionTableUI
from ui.functions import *

class DivisionsTableUI(MenuFrame):
    def __init__(self,logic_wrapper, os):
        super().__init__(logic_wrapper, os)

    def display_menu(self, list_of_all_divisions:list=[], showing_page:int=0):
        """Display the menu screen for the  matches"""
        NUMBER = "NR"
        DIVISION_NAME = "Division Name"
        NR = 4 #Length of number box
        DN = 40 #Length of team name box
        print("Division")

        #Format of table with a list of lists [row name, row width]
        table_format = [[NUMBER, NR], [DIVISION_NAME, DN]]
        try:
            #Fills in data for table
            table_data = []
            for i in range(len(list_of_all_divisions[showing_page])):
                division_nr = str(i + showing_page * 10) + ")"
                division =f"{list_of_all_divisions[showing_page][i][0]}"
                table_data.append([division_nr, division])
            #Generates a table with the correct format and data
            generate_table(table_format, table_data)
        except IndexError:
            generate_table(table_format, [])


    def prompt_option(self, showing_page:int=0):
        '''list_of_divisions = get_divisions(self.logic_wrapper)'''
        list_of_divisions = [[]]
        pages_number = len(list_of_divisions)//10
        while True:
            self.clear_menu()
            self.display_menu(list_of_divisions, showing_page=showing_page)
            print(display_menu_options(how_many_pages=pages_number, showing_page=showing_page))
            choice = input(" > ")
            choice = choice.lower()

            match choice:
                case "n":
                    if showing_page == pages_number:
                        input("Invalid Input!")
                    else:
                        showing_page += 1

                # if user wants to see the last 10 items
                case "b":
                    if showing_page == 0:
                        input("Invalid Input!")
                    else:
                        showing_page -= 1

                # if user wants to quit
                case "q":
                    break
                
                case "1":
                    division_table_ui = DivisionTableUI(self.logic_wrapper, self.os)
                    division_table_ui.prompt_option(1)

                # undocumented inputs get disregarded
                case _:
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
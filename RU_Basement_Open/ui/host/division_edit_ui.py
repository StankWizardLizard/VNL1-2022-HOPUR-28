from ui.menu_frame import MenuFrame
from ui.functions import *

class EditDivisionUI(MenuFrame):
    def __init__(self, logic_wrapper, os, division):
        super().__init__(logic_wrapper, os)
        self.division = division


    def display_menu(self, team_names:list=[], showing_page:int=0):
        """Display the menu screen for the  division
            Prints Names of Team in match in table  """
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
            for i in range(showing_page*10, showing_page*10+len(team_names[showing_page*10:showing_page*10+10])):
                team_names_nr = str(i+1) + ")"
                team_name =f"{team_names[i][0]} vs {team_names[i][1]}"
                table_data.append([team_names_nr, team_name])
            #Generates a table with the correct format and data
            generate_table(table_format, table_data)
        except IndexError:
            generate_table(table_format, [])


    def prompt_option(self, showing_page = 0, id = 1):
        """Prompts the user to choose an option from a list of options for the match table"""
        team_names = self.logic_wrapper.get_team_names_by_division(self.division.id)
        match_ids = self.logic_wrapper.get_division_unplayed_match_ids(self.division.id)
        pages_number = len(team_names)//10
        while True:
            self.clear_menu()
            self.display_menu(team_names, showing_page=showing_page)
            print(display_menu_options(how_many_pages=pages_number, showing_page=showing_page))
            print("Select a match to delay")
            choice = input(" > ")
            choice = choice.strip().lower()

            match choice:
                # if user wants to quit
                case "q":
                    break

                # undocumented inputs get disregarded
                case _:
                    if choice.isnumeric():
                        try:     
                            match_id = match_ids[int(choice)-1]
                            new_date = get_date_input("Choose a new date on format YYYY-MM-DD: ")
                            self.logic_wrapper.postpone_match(new_date, self.division.id, match_id)
                            # division = divisions[int(choice) -1]
                            # divisionui = EditDivisionUI(self.logic_wrapper, self.os, division)
                            # divisionui.prompt_option()
                        except IndexError:
                            input("Invalid Input!")

from templates import all_months

class ActionSelection():
    """this class will store the user action selection (add, delete or modify) and will direct it to the necessary function to write to or delete from the file
    """
    
    def __init__(self):

        pass

    def add_event(self, something_here):
        #IN USER PAGE, NEED TO ADD ANOTHE RUSER INPUT FOR WHAT KIND OF APPOINTMENT, PASS THAT VAL AND REQUIRED DATA INTO HERE AND MAKE THE IF STATMENT TO WHICH CLASS TO RUN
        #THEN WE GOT TO MAKE ANOTHER FUNCTION IN APPOINTMENT TEMPLATE TO WRITE THE APPOINTMENT AS A STRING INTO CALENDAR TEMPLATE
        pass

    def delete_event(self, something):
        #WRITE THESE FUNCTION IN THE MONTHLY_TEMPLATE.PY AND THEN PASS IT TO ALL_MONTHS, THEN PASS IT TO THIS FUNCTION
        pass

    def modify_event(self, something):
        #IN THE USER PAGE, NEED TO ADD ANOTHER USER INPUT FOR WHAT THEY WANT TO MODIFY, LIKE DATE, DESC ETC. PASS VAL HERE AND MAKE IF STATMENT
        pass

    def print_whole_calendar(self):
        #ADD ANOTHER PRINT FUNCTION IN THE ALL_MONTHS FILE TO PRINT THE WHOLE OBJECT AND ADD IT TO THE END OF THE ALL MONTH TEMPLATE
        pass
    
    def make_calendar(self,year):
        self.year = year
        self.calendar = all_months.months_all(self.year)
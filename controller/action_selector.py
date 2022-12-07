from templates import all_months as am
from templates import monthly_template as mt
from models import appointment as aps
from models import assignment as ass
from models import birthday as bir
from models import chore as cho
from models import event as eve
from models import meeting as mee


#look in monthly_template for how the function flow up


class ActionSelection():
    """this class will store the user action selection (add, delete or modify) and will direct it to the necessary function to write to or delete from the file
    """
    
    def __init__(self):

        pass

    def add_event(self):
        #IN USER PAGE, NEED TO ADD ANOTHE RUSER INPUT FOR WHAT KIND OF APPOINTMENT, PASS THAT VAL AND REQUIRED DATA INTO HERE AND MAKE THE IF STATMENT TO WHICH CLASS TO RUN
        #THEN WE GOT TO MAKE ANOTHER FUNCTION IN APPOINTMENT TEMPLATE TO WRITE THE APPOINTMENT AS A STRING INTO CALENDAR TEMPLATE
        print("You have chosen to add an event.")
        print("What kind of event would you like to add?")
        print("Number 1: Appointment")
        print("Number 2: Assignment")
        print("Number 3: Birthday")
        print("Number 4: Chore")
        print("Number 5: Event")
        print("Number 6: Meeting")
        event_number = int(input("Please enter your selectoin: "))
        if event_number == 1:
            ...
            x = aps.Appointment()
        elif event_number == 2:
            ...
            x = ass.Assignment()
        elif event_number == 3:
            ...
            x = bir.Birthday()
        elif event_number == 4:
            ...
            x = cho.Chore()
        elif event_number == 5:
            ...
            x = eve.Event()
        elif event_number == 6:
            ...
            x = cho.Chore()
        pass

    def delete_event(self):
        #WRITE THESE FUNCTION IN THE MONTHLY_TEMPLATE.PY AND THEN PASS IT TO ALL_MONTHS, THEN PASS IT TO THIS FUNCTION
        date = input("What is the date of the event you want to delete? (MM-DD-YYY)")
        title = input("What is the title of the event, exact wording.")
        appointment_type = input("What is the type of appointment you are trying to remove?")
        am.months_all.delete_events()
        

    def modify_event(self):
        #IN THE USER PAGE, NEED TO ADD ANOTHER USER INPUT FOR WHAT THEY WANT TO MODIFY, LIKE DATE, DESC ETC. PASS VAL HERE AND MAKE IF STATMENT
        date = input("What is the date of the event you want to delete? (MM-DD-YYY)")
        title = input("What is the title of the event, exact wording.")
        pass

    def print_whole_calendar(self):
        #ADD ANOTHER PRINT FUNCTION IN THE ALL_MONTHS FILE TO PRINT THE WHOLE OBJECT AND ADD IT TO THE END OF THE ALL MONTH TEMPLATE
        #added __Str__ to all event classes parent and child and to all_months
        pass
    
    def make_calendar(self):
        start_year = int(input('Which year would you like your calendar to start from?'))
        self.calendar = am.months_all(start_year)

    def import_calendar(self, pathway):
        #open the final and import the object to self.calendar
        pass

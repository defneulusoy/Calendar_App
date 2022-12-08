import all_months as am
import monthly_template as mt
import appointment as aps
import assignment as ass
import birthday as bir
import chore as cho
import event as eve
import meeting as mee


#look in monthly_template for how the function flow up


class ActionSelection():
    """this class will store the user action selection (add, delete or modify) and will direct it to the necessary function to write to or delete from the file
    """
    
    def __init__(self,start_year):
        self.list_of_appointments = []
        if isinstance(start_year, int):
            self.start_year = start_year
            self.calendar = am.months_all(start_year)
        elif isinstance(start_year, str):
            self.pathway = start_year
            #read file and import year and appointments
        

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
        event_number = int(input("Please enter your selection: "))
        if event_number == 1:
            title = input("What is the title of the appointment? ")
            month = int(input("What is the month of the appointment (month number)? "))
            day = int(input("What is the day of the appointment? "))
            appt_time = input("What is the time of the appointment? ")
            self.list_of_appointments.append(aps.Appointment(day,month,title,appt_time))
            self.calendar.add_events(month,self.list_of_appointments[-1])
        elif event_number == 2:
            title = input("What is the title of the assignment? ")
            month = int(input("What is the month of the assignment (month number)? "))
            day = int(input("What is the day of the assignment? "))
            ass_time = input("What is the time of the assignment? ")
            self.list_of_appointments.append(ass.Assignment(day,month,title,ass_time))
            self.calendar.add_events(month,self.list_of_appointments[-1])      
        elif event_number == 3:
            title = input("What is the name of the birthday? ")
            month = int(input("What is the month of the birthday (month number)? "))
            day = int(input("What is the day of the birthday? "))
            self.list_of_appointments.append(bir.Birthday(day,month,title))
            self.calendar.add_events(month,self.list_of_appointments[-1])  
        elif event_number == 4:
            title = input("What is the chore? ")
            month = int(input("What is the month of the chore (month number)? "))
            day = int(input("What is the day of the chore? "))
            self.list_of_appointments.append(cho.Chore(day,month,title))
            self.calendar.add_events(month,self.list_of_appointments[-1]) 
            
        elif event_number == 5:
            title = input("What is the title of the event? ")
            month = int(input("What is the month of the event (month number)? "))
            day = int(input("What is the day of the event? "))
            appt_time = input("What is the time of the event? ")
            self.list_of_appointments.append(eve.Event(day,month,title,appt_time))
            self.calendar.add_events(month,self.list_of_appointments[-1])
            
        elif event_number == 6:
            title = input("What is the title of the meeting? ")
            month = int(input("What is the month of the meeting (month number)? "))
            day = int(input("What is the day of the meeting? "))
            appt_time = input("What is the time of the meeting? ")
            self.list_of_appointments.append(mee.Meeting(day,month,title,appt_time))
            self.calendar.add_events(month,self.list_of_appointments[-1])


    def delete_event(self):
        #WRITE THESE FUNCTION IN THE MONTHLY_TEMPLATE.PY AND THEN PASS IT TO ALL_MONTHS, THEN PASS IT TO THIS FUNCTION
        month = int(input("What is the month of the event you want to delete? (Month number) "))
        day = int(input("What is the day of the event? (Number) "))
        title = input("What is the title of the event, with exact wording? ")
        appointment_type = input("What is the type of appointment you are trying to remove? ")
        self.calendar.delete_events(month,day,title,appointment_type)
        

    def modify_event(self):
        #IN THE USER PAGE, NEED TO ADD ANOTHER USER INPUT FOR WHAT THEY WANT TO MODIFY, LIKE DATE, DESC ETC. PASS VAL HERE AND MAKE IF STATMENT
        month = int(input("What is the month of the event you want to modify? (Month number) "))
        day = int(input("What is the day of the event? (Number) "))
        title = input("What is the title of the event, with exact wording? ")
        appointment_type = input("What is the type of appointment you are trying to modify? ")
        self.calendar.modify_events(month,day,title,appointment_type)

    def print_whole_calendar(self):
        #ADD ANOTHER PRINT FUNCTION IN THE ALL_MONTHS FILE TO PRINT THE WHOLE OBJECT AND ADD IT TO THE END OF THE ALL MONTH TEMPLATE
        #added __Str__ to all event classes parent and child and to all_months
        am.months_all.print_out(self.calendar)

        print("{" + str(self.start_year) + "}",end="")
        for ele in self.list_of_appointments:
            print(ele)
        with open('cal.txt', 'w') as f:
            for ele in self.list_of_appointments:
                f.write("%s\n" %ele)

        
    
    def make_calendar(self):
        start_year = int(input('Which year would you like your calendar to start from? '))
        self.calendar = am.months_all(start_year)

if __name__ == "__main__":
    a = ActionSelection(1999)
    a.add_event()
    a.print_whole_calendar()

   #I FEEL LIKE THIS IS DONE
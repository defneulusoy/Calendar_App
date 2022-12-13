import all_months as am
import monthly_template as mt
import appointment as aps
import assignment as ass
import birthday as bir
import chore as cho
import event as eve
import meeting as mee





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
            self.list_of_appointments = []
            f= open(self.pathway,"r")
            lines = f.readlines()[565:-1]
            print(lines)
            for line in lines:
                self.list_of_appointments.append(line.strip())
            self.start_year = int(self.list_of_appointments[0])
            self.calendar = am.months_all(self.start_year)

                

            #read file and import year and appointments
        

    def add_event(self):
   
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
        
        month = int(input("What is the month of the event you want to delete? (Month number) "))
        day = int(input("What is the day of the event? (Number) "))
        title = input("What is the title of the event, with exact wording? ")
        appointment_type = input("What is the type of appointment you are trying to remove? ")
        if appointment_type == "Appointment" or appointment_type == "Assignment" or appointment_type == "Event" or appointment_type == "Meeting":
            time = input("What is the time of the event")
        self.calendar.delete_events(month,day,title,appointment_type,time)
        if appointment_type == "Appointment" or appointment_type == "Assignment" or appointment_type == "Event" or appointment_type == "Meeting":
                x = "Day: %s Month: %s Title: %s Time: %s AppointmentType: %s"%(day,month,title,time,appointment_type)
        else:
                x = "Day: %s Month: %s Title: %s AppointmentType: %s"%(day,month,title,appointment_type)
        for ele in self.list_of_appointments:
            if str(ele) == x:
                self.list_of_appointments.remove(ele)
        

    def modify_event(self):
        
        month = int(input("What is the month of the event you want to modify? (Month number) "))
        day = int(input("What is the day of the event? (Number) "))
        title = input("What is the title of the event, with exact wording? ")
        appointment_type = input("What is the type of appointment you are trying to modify? ")
        if appointment_type == "Appointment" or appointment_type == "Assignment" or appointment_type == "Event" or appointment_type == "Meeting":
            time = input("What is the time of the event")
        if appointment_type == "Appointment" or appointment_type == "Assignment" or appointment_type == "Event" or appointment_type == "Meeting":
            x = "Day: %s Month: %s Title: %s Time: %s AppointmentType: %s"%(day,month,title,time,appointment_type)
        else:
            x = "Day: %s Month: %s Title: %s AppointmentType: %s"%(day,month,title,appointment_type)
        for ele in self.list_of_appointments:
            if str(ele) == x:
                self.list_of_appointments.remove(ele)


        self.calendar.delete_events(month,day,title,appointment_type,time)
        
        bb = "Y"
        time_change = "hi"
        day_change = "hi"
        title_change = "hi"
        while bb == "Y":
            if appointment_type == "Appointment" or appointment_type == "Assignment" or appointment_type == "Event" or appointment_type == "Meeting":
                print("What would you like to change?")
                print("1: Day change")
                print("2: Title change")
                print("3: Time change")
                change = int(input("What would you like to change?"))
                if change == 1:
                    day_change = int(input("What day would you like to change to?"))
                if change == 2:
                    title_change = input("What would you like to change the title to")
                if change == 3:
                    time_change = input("What would you like to change the time to?")
            else:
                print("What would you like to change?")
                print("1: Day change")
                print("2: Title change")
                change = int(input("What would you like to change?"))
                if change == 1:
                    day_change = int(input("What day would you like to change to?"))
                if change == 2:
                    title_change = input("What would you like to change the title to")
            bb = input("Do you want to change another thing? (Y/N)")



        if title_change == "hi":
            title_change = title
        if day_change == "hi":
            day_change = day
        if time_change == "hi":
            time_change = time



        if appointment_type == "Appointment":
            self.list_of_appointments.append(aps.Appointment(day_change,month,title_change,time_change))
            self.calendar.add_events(month,self.list_of_appointments[-1])
        elif appointment_type == "Assignment":
            self.list_of_appointments.append(ass.Assignment(day_change,month,title_change,time_change))
            self.calendar.add_events(month,self.list_of_appointments[-1])      
        elif appointment_type == "Birthday":
            self.list_of_appointments.append(bir.Birthday(day_change,month,title_change))
            self.calendar.add_events(month,self.list_of_appointments[-1])  
        elif appointment_type == "Chore":
            self.list_of_appointments.append(cho.Chore(day_change,month,title_change))
            self.calendar.add_events(month,self.list_of_appointments[-1]) 
        elif appointment_type == "Event":
            self.list_of_appointments.append(eve.Event(day_change,month,title_change,time_change))
            self.calendar.add_events(month,self.list_of_appointments[-1])           
        elif appointment_type == "Meeting":
            self.list_of_appointments.append(mee.Meeting(day,day_change,title_change,time_change))
            self.calendar.add_events(month,self.list_of_appointments[-1])



    def print_whole_calendar(self):
        
        #added __Str__ to all event classes parent and child and to all_months
        am.months_all.print_out(self.calendar)

        a = str(self.start_year)
        for ele in self.list_of_appointments:
            print(ele)
        with open('cal.txt', 'a') as f:
            f.write("%s\n"%a)
            for ele in self.list_of_appointments:
                f.write("%s\n" %ele)

        
    
    def make_calendar(self):
        start_year = int(input('Which year would you like your calendar to start from? '))
        self.calendar = am.months_all(start_year)

if __name__ == "__main__":
    a = ActionSelection(1999)
    a.add_event()
    a.delete_event()


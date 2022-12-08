from monthly_template import one_month
import datetime
class months_all:

    def __init__(self,year):
        # this just makes all the months together
        self.year = year
        #gets year from action selector
        self.months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        self.month_code = [1,2,3,4,5,6,7,8,9,10,11,12]
        #month code needed to calculate first day of the month
        self.month_template = []
        for x in range(len(self.months)):
                first_day = datetime.date(self.year,self.month_code[x],1)
                first_day = first_day.weekday()
                if first_day == 6:
                    self.month_template.append(one_month(self.months[x], "Sunday", self.year))
                elif first_day == 0:
                    self.month_template.append(one_month(self.months[x], "Monday", self.year))
                elif first_day == 1:
                    self.month_template.append(one_month(self.months[x], "Tuesday", self.year))
                elif first_day == 2:
                    self.month_template.append(one_month(self.months[x], "Wednesday", self.year))
                elif first_day == 3:
                    self.month_template.append(one_month(self.months[x], "Thursday", self.year))
                elif first_day == 4:
                    self.month_template.append(one_month(self.months[x], "Friday", self.year))
                elif first_day == 5:
                    self.month_template.append(one_month(self.months[x], "Saturday", self.year))
                    
            
    def add_events(self, month, apt):
        the_month = month -1
        self.month_template[the_month].add_eventss(apt)
    
    def delete_events(self,month,date,title,appointment_type):
        the_month = month - 1
        self.month_template[the_month].delete_events(date,title,appointment_type)

    def modify_events(self,month,date,title,appointment_type):
        the_month = month - 1
        self.month_template[the_month].modify_events(date,title,appointment_type)

    def print_out(self):
        for ele in self.month_template:
            one_month.print_real(ele)


if __name__ == "__main__":
    x = months_all(2008)
    x.print_out()
        

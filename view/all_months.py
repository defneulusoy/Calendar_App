from monthly_template import one_month

class months_all:

    def __init__(self,year):
        # this just makes all the months together
        self.year = year
        #gets year from action selector
        self.months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        self.month_code = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4 ]
        #month code needed to calculate first day of the month
        self.month_template = []
        for x in range(len(self.months)):
            if not self.year% 4 == 0:
                first_day = (self.year + int(self.year / 4) - int(self.year / 100) + int(self.year / 400) + self.month_code[x] + 1) % 7 #january
                if first_day == 0:
                    self.month_template.append(one_month(self.months[x], "Sunday", self.year))
                elif first_day == 1:
                    self.month_template.append(one_month(self.months[x], "Monday", self.year))
                elif first_day == 2:
                    self.month_template.append(one_month(self.months[x], "Tuesday", self.year))
                elif first_day == 3:
                    self.month_template.append(one_month(self.months[x], "Wednesday", self.year))
                elif first_day == 4:
                    self.month_template.append(one_month(self.months[x], "Thursday", self.year))
                elif first_day == 5:
                    self.month_template.append(one_month(self.months[x], "Friday", self.year))
                elif first_day == 6:
                    self.month_template.append(one_month(self.months[x], "Saturday", self.year))
            else: 
                first_day = (self.year + int(self.year / 4) - int(self.year / 100) + int(self.year / 400) + self.month_code[x]) % 7
                if first_day == 0:
                    self.month_template.append(one_month(self.months[x], "Sunday", self.year))
                elif first_day == 1:
                    self.month_template.append(one_month(self.months[x], "Monday", self.year))
                elif first_day == 2:
                    self.month_template.append(one_month(self.months[x], "Tuesday", self.year))
                elif first_day == 3:
                    self.month_template.append(one_month(self.months[x], "Wednesday", self.year))
                elif first_day == 4:
                    self.month_template.append(one_month(self.months[x], "Thursday", self.year))
                elif first_day == 5:
                    self.month_template.append(one_month(self.months[x], "Friday", self.year))
                elif first_day == 6:
                    self.month_template.append(one_month(self.months[x], "Saturday", self.year))

    def add_events(self):
        pass
    
    def delete_events(self):
        one_month.delete_events()

    def modify_events(self):
        pass



    def print_out(self):
        for ele in self.month_template:
            one_month.print_real(ele)


if __name__ == "__main__":
    x = months_all(2008)
    x.print_out()
        

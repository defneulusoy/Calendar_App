class one_month:
    def __init__(self,month,first_day,year):
        self.month = month
        self.year = year
        self.first_day = first_day
        if self.year% 4 == 0:
            self.leap_year = True
        else:
            self.leap_year = False
        if len(month) % 2 == 1:
            self.monthtitle1 = " " * ((148-len(month))//2-3)
            self.monthtitle2 = " " * (((148-len(month))//2)-3)
        else:
            self.monthtitle1 = " " * (74 - (len(month)//2)-3)
            self.monthtitle2 = " " * (74 - (len(month)//2)-4)
        row = "-"*148
        middle = "|       Sunday       |       Monday       |       Tuesday      |      Wednesday     |      Thursday      |       Friday       |      Saturday      |"
        week_header = [row, middle, row]
        # 20 character limit inside
        month = "|" + self.monthtitle2 + self.month + " " + str(self.year) + self.monthtitle1 + "|"
        month_header = [row, month]
        inside = ["                    ", "|"] #change this when we get to adding info
        middle = ["|", inside, inside, inside, inside, inside, inside, inside]
        one_section = [middle,middle,middle,middle,middle,middle,row]
        whole_body = one_section*6
        for ele in week_header:
            month_header.append(ele)
        for ele in whole_body:
            month_header.append(ele)
        self.calendar =  month_header

    def add_appointment():
        pass # work on this

    def print_real(self):
        for x in self.calendar:
            if isinstance(self.calendar, list):
                for y in x:
                    for z in y:
                        print(z,end= "")
                print("")
            else:
                print(x)

    #no __str__ for this class. cant output a list, must print through this class.

a = one_month("1234","monday",1234)
a.print_real()

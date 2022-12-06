class one_month:
    def __init__(self,month,first_day,year):
        #this is the template for one month
        self.month = month
        self.year = year
        self.first_day = first_day
        # year month and first day are needed to find what week day the month starts on
        if self.year% 4 == 0:
            self.leap_year = True
        else:
            self.leap_year = False
        #for considering leap year
        if len(month) % 2 == 1:
            self.monthtitle1 = " " * ((148-len(month))//2-3)
            self.monthtitle2 = " " * (((148-len(month))//2)-3)
        else:
            self.monthtitle1 = " " * (74 - (len(month)//2)-3)
            self.monthtitle2 = " " * (74 - (len(month)//2)-4)
        #all of the if statements are to calculate formatting of the month header
        row = "-"*148
        middle = "|       Sunday       |       Monday       |       Tuesday      |      Wednesday     |      Thursday      |       Friday       |      Saturday      |"
        week_header = [row, middle, row] # header for the week titles
        # 20 character limit inside
        month = "|" + self.monthtitle2 + self.month + " " + str(self.year) + self.monthtitle1 + "|"
        month_header = [row, month] # header for the month title
        inside = ["                    ", "|"] #change this when we get to adding info
        middle = ["|", inside, inside, inside, inside, inside, inside, inside]
        one_section = [middle,middle,middle,middle,middle,middle,row]
        #two loops to get to the inside, and to change the data, it will always be position 0
        whole_body = one_section*6
        #makes 6 weeks of boxes
        for ele in week_header:
            month_header.append(ele)
            #appends the week header to month header
        for ele in whole_body:
            #appends month body to header
            month_header.append(ele)
        self.calendar =  month_header

    def add_appointment():
        pass # work on this

    def print_real(self):
        #this function must be used to print out the template, cannot print as string
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

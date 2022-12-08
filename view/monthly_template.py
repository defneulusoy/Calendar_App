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
        middle = ["|", ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"]]
        one_section = [["|", ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"]],["|", ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"]],["|", ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"]],["|", ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"]],["|", ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"]],["|", ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"]],row]
        #two loops to get to the inside, and to change the data, it will always be position 0
        whole_body = [[["|", ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"]],["|", ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"]],["|", ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"]],["|", ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"]],["|", ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"]],["|", ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"]],row],[["|", ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"]],["|", ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"]],["|", ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"]],["|", ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"]],["|", ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"]],["|", ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"]],row],[["|", ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"]],["|", ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"]],["|", ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"]],["|", ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"]],["|", ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"]],["|", ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"]],row],[["|", ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"]],["|", ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"]],["|", ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"]],["|", ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"]],["|", ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"]],["|", ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"]],row],[["|", ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"]],["|", ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"]],["|", ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"]],["|", ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"]],["|", ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"]],["|", ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"]],row],[["|", ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"]],["|", ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"]],["|", ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"]],["|", ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"]],["|", ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"]],["|", ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"], ["                    ", "|"]],row]]
        #makes 6 weeks of boxes
        if self.month == "January" or self.month == "March" or self.month == "May" or self.month == "July" or self.month == "August" or self.month == "October" or self.month == "December":
            if first_day == "Sunday":
                count = 1
                for x in range(4):
                    for y in range(1,8):
                        if count < 10:
                            whole_body[x][0][y][0] = "         %s          "%count
                            count += 1
                        else:
                            whole_body[x][0][y][0] = "         %s         "%count
                            count += 1
                for y in range(1,4):
                    whole_body[4][0][y][0] = "         %s         "%count
                    count += 1
            elif first_day == "Monday":
                count = 1
                for y in range(2,8):
                    whole_body[0][0][y][0] = "         %s          "%count
                    count += 1
                for x in range(1,4):
                    for y in range(1,8):
                        if count < 10:
                            whole_body[x][0][y][0] = "         %s          "%count
                            count += 1
                        else:
                            whole_body[x][0][y][0] = "         %s         "%count
                            count += 1
                for y in range(1,5):
                    whole_body[4][0][y][0] = "         %s         "%count
                    count += 1
            elif first_day == "Tuesday":
                count = 1
                for y in range(3,8):
                    whole_body[0][0][y][0] = "         %s          "%count
                    count += 1
                for x in range(1,4):
                    for y in range(1,8):
                        if count < 10:
                            whole_body[x][0][y][0] = "         %s          "%count
                            count += 1
                        else:
                            whole_body[x][0][y][0] = "         %s         "%count
                            count += 1
                for y in range(1,6):
                    whole_body[4][0][y][0] = "         %s         "%count
                    count += 1
            elif first_day == "Wednesday":
                count = 1
                for y in range(4,8):
                    whole_body[0][0][y][0] = "         %s          "%count
                    count += 1
                for x in range(1,4):
                    for y in range(1,8):
                        if count < 10:
                            whole_body[x][0][y][0] = "         %s          "%count
                            count += 1
                        else:
                            whole_body[x][0][y][0] = "         %s         "%count
                            count += 1
                for y in range(1,7):
                    whole_body[4][0][y][0] = "         %s         "%count
                    count += 1
            elif first_day == "Thursday":
                count = 1
                for y in range(5,8):
                    whole_body[0][0][y][0] = "         %s          "%count
                    count += 1
                for x in range(1,5):
                    for y in range(1,8):
                        if count < 10:
                            whole_body[x][0][y][0] = "         %s          "%count
                            count += 1
                        else:
                            whole_body[x][0][y][0] = "         %s         "%count
                            count += 1
            elif first_day == "Friday":
                count = 1
                for y in range(6,8):
                    whole_body[0][0][y][0] = "         %s          "%count
                    count += 1
                for x in range(1,5):
                    for y in range(1,8):
                        if count < 10:
                            whole_body[x][0][y][0] = "         %s          "%count
                            count += 1
                        else:
                            whole_body[x][0][y][0] = "         %s         "%count
                            count += 1
                for y in range(1,2):
                    whole_body[5][0][y][0] = "         %s         "%count
                    count += 1
            elif first_day == "Saturday":
                count = 1
                for y in range(7,8):
                    whole_body[0][0][y][0] = "         %s          "%count
                    count += 1
                for x in range(1,5):
                    for y in range(1,8):
                        if count < 10:
                            whole_body[x][0][y][0] = "         %s          "%count
                            count += 1
                        else:
                            whole_body[x][0][y][0] = "         %s         "%count
                            count += 1
                for y in range(1,3):
                    whole_body[5][0][y][0] = "         %s         "%count
                    count += 1
        elif self.month == "April" or self.month == "June" or self.month == "September" or self.month == "November":  
            if first_day == "Sunday":
                if first_day == "Sunday":
                    count = 1
                    for x in range(4):
                        for y in range(1,8):
                            if count < 10:
                                whole_body[x][0][y][0] = "         %s          "%count
                                count += 1
                            else:
                                whole_body[x][0][y][0] = "         %s         "%count
                                count += 1
                    for x in range(1,3):
                        whole_body[4][0][x][0] = "         %s         "%count
                        count += 1
            elif first_day == "Monday":
                count = 1
                for y in range(2,8):
                    whole_body[0][0][y][0] = "         %s          "%count
                    count += 1
                for x in range(1,4):
                    for y in range(1,8):
                        if count < 10:
                            whole_body[x][0][y][0] = "         %s          "%count
                            count += 1
                        else:
                            whole_body[x][0][y][0] = "         %s         "%count
                            count += 1
                for y in range(1,4):
                    whole_body[4][0][y][0] = "         %s         "%count
                    count += 1
            elif first_day == "Tuesday":
                count = 1
                for y in range(3,8):
                    whole_body[0][0][y][0] = "         %s          "%count
                    count += 1
                for x in range(1,4):
                    for y in range(1,8):
                        if count < 10:
                            whole_body[x][0][y][0] = "         %s          "%count
                            count += 1
                        else:
                            whole_body[x][0][y][0] = "         %s         "%count
                            count += 1
                for y in range(1,5):
                    whole_body[4][0][y][0] = "         %s         "%count
                    count += 1
            elif first_day == "Wednesday":
                count = 1
                for y in range(4,8):
                    whole_body[0][0][y][0] = "         %s          "%count
                    count += 1
                for x in range(1,4):
                    for y in range(1,8):
                        if count < 10:
                            whole_body[x][0][y][0] = "         %s          "%count
                            count += 1
                        else:
                            whole_body[x][0][y][0] = "         %s         "%count
                            count += 1
                for y in range(1,6):
                    whole_body[4][0][y][0] = "         %s         "%count
                    count += 1
            elif first_day == "Thursday":
                count = 1
                for y in range(5,8):
                    whole_body[0][0][y][0] = "         %s          "%count
                    count += 1
                for x in range(1,4):
                    for y in range(1,8):
                        if count < 10:
                            whole_body[x][0][y][0] = "         %s          "%count
                            count += 1
                        else:
                            whole_body[x][0][y][0] = "         %s         "%count
                            count += 1
                for y in range(1,7):
                    whole_body[4][0][y][0] = "         %s         "%count
                    count += 1
            elif first_day == "Friday":
                count = 1
                for y in range(6,8):
                    whole_body[0][0][y][0] = "         %s          "%count
                    count += 1
                for x in range(1,5):
                    for y in range(1,8):
                        if count < 10:
                            whole_body[x][0][y][0] = "         %s          "%count
                            count += 1
                        else:
                            whole_body[x][0][y][0] = "         %s         "%count
                            count += 1
            elif first_day == "Saturday":
                count = 1
                for y in range(7,8):
                    whole_body[0][0][y][0] = "         %s          "%count
                    count += 1
                for x in range(1,5):
                    for y in range(1,8):
                        if count < 10:
                            whole_body[x][0][y][0] = "         %s          "%count
                            count += 1
                        else:
                            whole_body[x][0][y][0] = "         %s         "%count
                            count += 1
                for y in range(1,2):
                    whole_body[5][0][y][0] = "         %s         "%count
                    count += 1
        elif self.month == "February":
            if self.leap_year:
                if first_day == "Sunday":
                    count = 1
                    for x in range(4):
                        for y in range(1,8):
                            if count < 10:
                                whole_body[x][0][y][0] = "         %s          "%count
                                count += 1
                            else:
                                whole_body[x][0][y][0] = "         %s         "%count
                                count += 1
                    for y in range(1,2):
                        whole_body[4][0][y][0] = "         %s         "%count
                        count += 1               
                elif first_day == "Monday":
                    count = 1
                    for y in range(2,8):
                        whole_body[0][0][y][0] = "         %s          "%count
                        count += 1
                    for x in range(1,4):
                        for y in range(1,8):
                            if count < 10:
                                whole_body[x][0][y][0] = "         %s          "%count
                                count += 1
                            else:
                                whole_body[x][0][y][0] = "         %s         "%count
                                count += 1
                    for y in range(1,3):
                        whole_body[4][0][y][0] = "         %s         "%count
                        count += 1
                elif first_day == "Tuesday":
                    count = 1
                    for y in range(3,8):
                        whole_body[0][0][y][0] = "         %s          "%count
                        count += 1
                    for x in range(1,4):
                        for y in range(1,8):
                            if count < 10:
                                whole_body[x][0][y][0] = "         %s          "%count
                                count += 1
                            else:
                                whole_body[x][0][y][0] = "         %s         "%count
                                count += 1
                    for y in range(1,4):
                        whole_body[4][0][y][0] = "         %s         "%count
                        count += 1
                elif first_day == "Wednesday":
                    count = 1
                    for y in range(4,8):
                        whole_body[0][0][y][0] = "         %s          "%count
                        count += 1
                    for x in range(1,4):
                        for y in range(1,8):
                            if count < 10:
                                whole_body[x][0][y][0] = "         %s          "%count
                                count += 1
                            else:
                                whole_body[x][0][y][0] = "         %s         "%count
                                count += 1
                    for y in range(1,5):
                        whole_body[4][0][y][0] = "         %s         "%count
                        count += 1
                elif first_day == "Thursday":
                    count = 1
                    for y in range(5,8):
                        whole_body[0][0][y][0] = "         %s          "%count
                        count += 1
                    for x in range(1,4):
                        for y in range(1,8):
                            if count < 10:
                                whole_body[x][0][y][0] = "         %s          "%count
                                count += 1
                            else:
                                whole_body[x][0][y][0] = "         %s         "%count
                                count += 1
                    for y in range(1,6):
                        whole_body[4][0][y][0] = "         %s         "%count
                        count += 1
                elif first_day == "Friday":
                    count = 1
                    for y in range(6,8):
                        whole_body[0][0][y][0] = "         %s          "%count
                        count += 1
                    for x in range(1,4):
                        for y in range(1,8):
                            if count < 10:
                                whole_body[x][0][y][0] = "         %s          "%count
                                count += 1
                            else:
                                whole_body[x][0][y][0] = "         %s         "%count
                                count += 1
                    for y in range(1,7):
                        whole_body[4][0][y][0] = "         %s         "%count
                        count += 1
                elif first_day == "Saturday":
                    count = 1
                    for y in range(7,8):
                        whole_body[0][0][y][0] = "         %s          "%count
                        count += 1
                    for x in range(1,5):
                        for y in range(1,8):
                            if count < 10:
                                whole_body[x][0][y][0] = "         %s          "%count
                                count += 1
                            else:
                                whole_body[x][0][y][0] = "         %s         "%count
                                count += 1
            else:
                if first_day == "Sunday":
                    count = 1
                    for x in range(4):
                        for y in range(1,8):
                            if count < 10:
                                whole_body[x][0][y][0] = "         %s          "%count
                                count += 1
                            else:
                                whole_body[x][0][y][0] = "         %s         "%count
                                count += 1           
                elif first_day == "Monday":
                    count = 1
                    for y in range(2,8):
                        whole_body[0][0][y][0] = "         %s          "%count
                        count += 1
                    for x in range(1,4):
                        for y in range(1,8):
                            if count < 10:
                                whole_body[x][0][y][0] = "         %s          "%count
                                count += 1
                            else:
                                whole_body[x][0][y][0] = "         %s         "%count
                                count += 1
                    for y in range(1,2):
                        whole_body[4][0][y][0] = "         %s         "%count
                        count += 1
                elif first_day == "Tuesday":
                    count = 1
                    for y in range(3,8):
                        whole_body[0][0][y][0] = "         %s          "%count
                        count += 1
                    for x in range(1,4):
                        for y in range(1,8):
                            if count < 10:
                                whole_body[x][0][y][0] = "         %s          "%count
                                count += 1
                            else:
                                whole_body[x][0][y][0] = "         %s         "%count
                                count += 1
                    for y in range(1,3):
                        whole_body[4][0][y][0] = "         %s         "%count
                        count += 1
                elif first_day == "Wednesday":
                    count = 1
                    for y in range(4,8):
                        whole_body[0][0][y][0] = "         %s          "%count
                        count += 1
                    for x in range(1,4):
                        for y in range(1,8):
                            if count < 10:
                                whole_body[x][0][y][0] = "         %s          "%count
                                count += 1
                            else:
                                whole_body[x][0][y][0] = "         %s         "%count
                                count += 1
                    for y in range(1,4):
                        whole_body[4][0][y][0] = "         %s         "%count
                        count += 1
                elif first_day == "Thursday":
                    count = 1
                    for y in range(5,8):
                        whole_body[0][0][y][0] = "         %s          "%count
                        count += 1
                    for x in range(1,4):
                        for y in range(1,8):
                            if count < 10:
                                whole_body[x][0][y][0] = "         %s          "%count
                                count += 1
                            else:
                                whole_body[x][0][y][0] = "         %s         "%count
                                count += 1
                    for y in range(1,5):
                        whole_body[4][0][y][0] = "         %s         "%count
                        count += 1
                elif first_day == "Friday":
                    count = 1
                    for y in range(6,8):
                        whole_body[0][0][y][0] = "         %s          "%count
                        count += 1
                    for x in range(1,4):
                        for y in range(1,8):
                            if count < 10:
                                whole_body[x][0][y][0] = "         %s          "%count
                                count += 1
                            else:
                                whole_body[x][0][y][0] = "         %s         "%count
                                count += 1
                    for y in range(1,6):
                        whole_body[4][0][y][0] = "         %s         "%count
                        count += 1
                elif first_day == "Saturday":
                    count = 1
                    for y in range(7,8):
                        whole_body[0][0][y][0] = "         %s          "%count
                        count += 1
                    for x in range(1,4):
                        for y in range(1,8):
                            if count < 10:
                                whole_body[x][0][y][0] = "         %s          "%count
                                count += 1
                            else:
                                whole_body[x][0][y][0] = "         %s         "%count
                                count += 1
                    for y in range(1,7):
                        whole_body[4][0][y][0] = "         %s         "%count
                        count += 1
                



        for ele in week_header:
            month_header.append(ele)
            #appends the week header to month header
        for ele in whole_body:
            #appends month body to header
            month_header.append(ele)
        self.calendar =  month_header

    

    #add_event goes to all months, to appointment template, to action selector
    def add_events(self):
        pass
    #delete event goes to all months to action selector
    def delete_events(self, file_name, event_name):
        with open(file_name , 'r') as f:
            lines =  f.readlines()
            with open(file_name, 'w'):
                for line in lines:
                    if line.strip('\n') != event_name:
                        f.write(line)

        pass
    #modify event goes to all months to action selector
    def modify_events(self):
        pass


    def print_real(self):
        #this function must be used to print out the template, cannot print as string
        count = 0
        #this function must be used to print out the template, cannot print as string
        for x in self.calendar:
            if isinstance(self.calendar, list):
                for y in x:
                    for z in y:
                        if isinstance(z,list):
                            for a in z:
                                print(a,end="")
                                count += 1
                                if count == 14:
                                    print("")
                                    count = 0 
                                
                        else:
                            print(z,end= "")
                print("")
            else:
                print(x)

    #no __str__ for this class. cant output a list, must print through this class.

if __name__ == "__main__":
    x = one_month("February","Monday",1999)
    x.print_real()


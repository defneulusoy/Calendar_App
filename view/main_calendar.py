calendar_type = input("Please enter 'new' to add a new calendar, or the date of the calendar in the 'dd-mm-year' format if you would like to see an existing calendar: ")

if calendar_type == 'new':
    with open('New_Calendar.txt', 'w') as f:
        #initialize new calendar
        pass
else:
    date_lst = calendar_type.split('-')
    day = date_lst[0]
    month = date_lst[1]
    year = date_lst[2]

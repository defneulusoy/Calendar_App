
calendar_type = input("Please enter 'new' to add a new calendar, or the date of the calendar in the 'dd-mm-year' format if you would like to see an existing calendar: ")

if calendar_type == 'new':
    start_year = input('Which year would you like your calendar to start from?')
    with open('New_Calendar.txt', 'w') as f:
        #initialize new calendar
        pass
else:
    date_lst = calendar_type.split('-')
    day = date_lst[0]
    month = date_lst[1]
    year = date_lst[2]
    print("Welcome to your personalized calendar application")
    print("Here, you can do many tasks such as adding, deleting or modifying various types of pre_determined or new events, and save all your events to view them later")
    print("Here are some suggestions, please enter your selection number")
    print("Number 1: Add a new event")
    print("Number 2: Delete an existing event")
    print("Number 3: Modify a pre-existing event")

    action_selection = input(print("Please enter your selection: "))

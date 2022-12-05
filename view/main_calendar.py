from controller import action_selector
from templates import all_months



calendar_type = input("Please enter 'new' to add a new calendar, or the pathway to an old calendar if you would like to see an existing calendar: ")

if calendar_type == 'new':
    start_year = input('Which year would you like your calendar to start from?')
    final_cal = all_months.months_all(start_year)
else:
    pathway = calendar_type
    x = ... # read file's objects


print("Welcome to your personalized calendar application")
print("Here, you can do many tasks such as adding, deleting or modifying various types of pre_determined or new events, and save all your events to view them later")
print("Here are some suggestions, please enter your selection number")
x = "Y"
while x:
    print("Number 1: Add a new event")
    print("Number 2: Delete an existing event")
    print("Number 3: Modify a pre-existing event")
    action_selection = int(input(print("Please enter your selection: ")))
    action_selector.ActionSelection(action_selection)
    x = input("Whould you like to make more changes? (Y/N)")

print("The file will now automatically save.")

... # write the calendar into the file
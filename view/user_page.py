#THIS FILE IS DONE, NOTHING TO ADD HERE, DO ALL CODING ON OTHER FILES
#THIS FILE IS DONE, NOTHING TO ADD HERE, DO ALL CODING ON OTHER FILES 
#THIS FILE IS DONE, NOTHING TO ADD HERE, DO ALL CODING ON OTHER FILES
import action_selector
#WE NEED TO MAKE TEST CASES FOR EVERY CLASS __name__ == __main__

#try not to have any objects in this page, do everything through the action selector
calendar_type = input("Please enter 'new' to add a new calendar, or the pathway to an old calendar if you would like to see an existing calendar: ")
#this will either get new calendar or the pathway to an old calendar
final_cal = action_selector.ActionSelection 
#initializes the action selector so that things can be done

if calendar_type == 'new':
    final_cal.make_calendar()
    #if new, asks for year and makes the calendar in the action selector
else:
    pathway = calendar_type
    final_cal.import_calendar(pathway)
    #WORK THIS, add function in action selector that can open file from given file path and read the contents.
    #im thinking that at the end of the calendar template will be the object of the calendar printed in bytes
    #that way we can read and easily manipulate.

print("Welcome to your personalized calendar application")
print("Here, you can do many tasks such as adding, deleting or modifying various types of pre_determined or new events, and save all your events to view them later")
print("Here are some suggestions, please enter your selection number")
#this is where the user starts to add/modify/delete
x = "Y"
while x:
    print("Number 1: Add a new event")
    print("Number 2: Delete an existing event")
    print("Number 3: Modify a pre-existing event")
    action_selection = int(input("Please enter your selection: "))
    if action_selection == 1:
        final_cal.add_event()
    elif action_selection == 2:
        final_cal.delete_event()
    elif action_selection == 3:
        final_cal.modify_event()
        
    x = input("Whould you like to make more changes? (Y/N)")

print("The file will now automatically save.")
final_cal.print_whole_calendar() # this needs to print into a file


#THIS FILE IS DONE, NOTHING TO ADD HERE, DO ALL CODING ON OTHER FILES
#THIS FILE IS DONE, NOTHING TO ADD HERE, DO ALL CODING ON OTHER FILES
#THIS FILE IS DONE, NOTHING TO ADD HERE, DO ALL CODING ON OTHER FILES
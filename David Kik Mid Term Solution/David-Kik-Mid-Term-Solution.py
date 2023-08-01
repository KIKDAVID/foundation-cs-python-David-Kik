#Step 1: Importing necessary libraries
#########################################################################################################################

import datetime #to handle date and time related 







#Step 2: Defining Global variables to be used by all methods
#########################################################################################################################

filePath= '/home/dave55/foundation-cs-python-David-Kik/David Kik Mid Term Solution/events.txt'








#Step3: defining the function readEventsFromFile to read event data from the txt file info.
#       and return a list of events.
 
##################################################################################################################33

#https://www.codingame.com/playgrounds/58255/basic-file-manipulation-in-python
#https://hashnode.com/post/strip-and-split-method-in-python-cl2buwtjx07k8x5nv4mgcbio1
#https://www.section.io/engineering-education/files-and-exceptions-in-python/
#https://www.geeksforgeeks.org/read-list-of-dictionaries-from-file-in-python/
#https://stackoverflow.com/questions/38780764/how-to-create-a-list-from-a-text-file-in-python
#https://education.molssi.org/python_scripting_cms/02-file_parsing/index.html#:~:text=In%20order%20to%20parse%20a,your%20notebook%20and%20evaluating%20it.


def readEventsFromFile(filePath):            # defining the function with argument filPath
    events= []                               # Empty list created 
    try:                                     # a try block created to handle errors and excemptions while handeling the file 
        with open(filePath, 'r') as file:    # with statement ensures file is properly closed r for read mode 
            for line in file:                # for loop to iterate over each line 
                ticket_id, ticket_date, event_id, user_name, time_stamp, priority = line.strip().split(', ')#rparsing data from file with spilt strip and reads a line from the file using strip to eliminate white spaces and split the line into individual characters separating by , and space.asigning the charactes to variables 
                ticket = {                   # extracted characters are used to create a dictionary 
                    'ticket_id': ticket_id,  # key value pairs created 
                    'ticket_date': ticket_date,
                    'event_id': event_id,
                    'user_name': user_name,
                    'time_stamp': time_stamp,
                    'priority': int(priority)
                }
                events.append(ticket)         # the dictionary created (ticket) is added to events list using append 
        print("\n***** Events imported successfully.*****") #if read successfully this message is printed 
    except FileNotFoundError:                 # if file not found 
        print("File does not exist.")         # this message is printed 
    except Exception as errorfound:           # as keyword created to catch ecceptions and errors giving it a variable errorfound.
        print("Error occurred while reading the file:", errorfound) #if any error occurs this message will be printed along with exception errorfound 
    return events                             # after reading all lines the function returns the list of events 



#https://realpython.com/read-write-files-python/
#defining a function to save an event/ticket

def saveTicketToFile(events):                 # the function that takes an argument to be saved on 
    try:                                      # try block created to handle the file 
        with open(filePath, 'w') as file:     # with statement using write mode 
            for ticket in events:
                                              # creating a string line using f" fstring representing the file format needed 
                line = f"{ticket['ticket_id']}, {ticket['ticket_date']}, {ticket['event_id']}, {ticket['user_name']}, {ticket['time_stamp']}, {ticket['priority']}\n"
                file.write(line)              # Write the 'line' to the file
        print("\n*****Tickets saved successfully.*****")# print successful if no errors found 
    except Exception as errorfound:           # print any error found
        print("Error occurred while saving tickets:", errorfound)







#Step4: Defining the login function for normal user and admin.
###############################################################
#The login function handles the login process, where the user is prompted for a username and password (if admin) and allowed a limited number of login attempts.

def login(events):                            # difining the function giving it argument needed 
    max_attempts = 5                          # setting max number of log attempts 
    while max_attempts > 0:                   # Loop until max login reached 
        user_name = input("\nEnter your username \n(Must be alphabetic only): ").strip()#correct credential entered 
        if alphabeticalName(user_name):       # is a function to check if username is only letters 
            password = input("\nEnter your password \n(leave empty for normal user): ")

            if user_name.lower() == "admin" and password == "admin123123":# Checking if the entered username is "admin" and the password is "admin123123".
                print("\nWelcome, Admin!")
                print("\nWelcome, Admin!")
                adminMenu(events)             # Calling the adminMenu
                break                         # Exiting the login loop
            elif password == "":              # Calling the normalUserMenu function if the user is not the admin password is empty
                
                print("\nWelcome", user_name,"!!!")
                normalUserMenu(events, user_name)
                break                         # Exiting the login loop 
            else:                             # If credentials are incorrect 
                max_attempts -= 1             # Reducing the number of remaining login attempts by 1
                print("Invalid Username. Username must contain only letters. Remaining attempts:", max_attempts)
        else:                                 # Executed when the user enters an invalid username 
            max_attempts -= 1                 # Reducing the number of remaining login attempts by 1           
            print("Invalid Username. Username must contain only letters. Remaining attempts:", max_attempts)
    else:                                     # Executed when all login attempts are used up
        print("Maximum login attempts reached. Exiting the program.")


#https://www.programiz.com/python-programming/methods/string/isalpha
#https://www.shiksha.com/online-courses/articles/isalpha-method-in-python/#Return-Value-of-isalpha()
## Function to check if a username only contains letters

def alphabeticalName(user_name):      
    #return user_name.isalpha()
    for char in user_name:
        if not (char.isalpha() or char.isspace()):# Check if the character is a letter or a space
            return False
    return True




#Step 5: Implementing admin and user menus
##########################################################################################################################
#The adminMenu function displays options for an admin user, such as displaying statistics, booking a ticket, changing ticket priority, etc.
#The normalUserMenu function displays options for a regular user, such as booking a ticket and saving and exiting.

def adminMenu(events):
    while True:                                   # loop to keep displaying the menu until the admin chooses to exit the program.
        print("\nAdmin Menu Options:")
        print("1. Display Statistics")
        print("2. Book a Ticket")
        print("3. Display all Tickets")
        print("4. Change Ticket's Priority")
        print("5. Disable Ticket")
        print("6. Run Events")
        print("7. Exit ")

        choice = input("Enter your choice here!: ")# admin is prompted to enter their choice using the input function, and the entered choice is stored in the variable choice.
                                                   # uses multiple if and elif statements to check the value of choice and call the corresponding functions based on the user's input.
        if choice == '1':            
            displayStatistics(events)              # Call the displayStatistics function
        elif choice == '2':
            bookTicket(events)                      # Call the bookTicket function
        elif choice == '3':
            displayAllTickets(events)               # Call the displayAllTickets function
        elif choice == '4':
            changeTicketPriority(events)            # Call the changeTicketPriority function
        elif choice == '5':
            disableTicket(events)                   # Call the disableTicket function
        elif choice == '6':
            runEvents(events)                       # Call the runEvents function
        elif choice == '7':
            exit(events)                            # Call the exit function and exit the loop to end the program
            print("----Exiting the program.----\n")
            break
        else:                                       # If the entered choice is invalid, display an error message
            print("Invalid choice. Try again.")






#Step 6: Building and displaying menu options and event details for admin and normal user.
##########################################################################################################################

#choice 1 admin
# Calculate the event ID with the highest number of tickets

def displayStatistics(events):                   # Create an empty dictionary to store the count of tickets for each event_id
    eventIdTicketCount = {}
    for ticket in events:
        event_id = ticket['event_id']            # Increment the ticket count
        eventIdTicketCount[event_id] = eventIdTicketCount.get(event_id, 0) + 1# Using get method to handle cases when event_id is not yet present in the dictionary

    if not eventIdTicketCount:                    # Check if there are any tickets in the dictionary
        print("No tickets found.")
        return

    maxTicketCount = max(eventIdTicketCount.values()) # Find the maximum ticket count
    maxTicketEvents = [event_id for event_id, count in eventIdTicketCount.items() if count == maxTicketCount]# Create a list of event_ids that have the maximum ticket count

    print("Event IDs with the highest number of tickets:")# Print the event_ids with the highest number of tickets
    for event_id in maxTicketEvents:
        print(f"{event_id} (Number of tickets: {maxTicketCount})")
    
                                                   # Get the list of tickets associated with the event ID with the highest ticket count
    max_ticket_event_id = maxTicketEvents[0]       # Get the event_id with the highest ticket count from the list of maxTicketEvents
    max_ticket_events_list = [ticket for ticket in events if ticket['event_id'] == max_ticket_event_id]# Create a list of tickets associated with the event_id 
    return max_ticket_event_id, max_ticket_events_list # Return the event_id with the highest ticket count


#Choice 2 admin:
# Implement option 2 - Book a Ticket

def bookTicket(events):
    
    user_name = input("Enter username: ")          # Prompt the user for username, event ID, and priority for the new ticket
    event_id = input("Enter event ID: ")
    priority = int(input("Enter priority (integer value): "))

    ticket_date = getValidTicketDate()             # Prompt for a valid ticket date
    current_date = datetime.datetime.now().strftime("%Y%m%d")# Get the current date and time to set as the timestamp
    ticket_id = generateTicketId(events)           # Generate a new ticket ID for the new ticket

    new_ticket = {                                 # Create a dictionary 'new_ticket' to store the information
        "ticket_id": ticket_id,
        "ticket_date": ticket_date.strftime("%Y%m%d"),
        "event_id": event_id,
        "user_name": user_name,
        "time_stamp": current_date,
        "priority": priority
    }

    events.append(new_ticket)                      # Add the new ticket to the 'events' list
    print("\nTicket booked successfully.")
    print("***************************")
    saveTicketToFile(events)


#Choice 3 admin:
#Display all Tickets

def displayAllTickets(events):
    
    today = datetime.date.today()                   # Get the current date 
    tomorrow = today + datetime.timedelta(days=1)   # Calculate the date for tomorrow

                                                    # Filter out old tickets
    valid_tickets = [ticket for ticket in events if datetime.datetime.strptime(ticket['time_stamp'], "%Y%m%d").date() >= today]

                                                    # Sort tickets by date and event ID
    sorted_tickets = sorted(valid_tickets, key=lambda x: (datetime.datetime.strptime(x['time_stamp'], "%Y%m%d"), x['event_id']))

    if not sorted_tickets:                          # Check if there are no valid_tickets after filtering
        print("No valid tickets found.")
        return

    print("\nAll Tickets:")                         # Valid tickets, print their information
    for ticket in sorted_tickets:                   # Print ticket information using formatted strings
        print(f"Ticket ID: {ticket['ticket_id']}, Ticket Date: {ticket['ticket_date']}, Event ID: {ticket['event_id']}, "
              f"Username: {ticket['user_name']}, Timestamp: {ticket['time_stamp']}, Priority: {ticket['priority']}")


#Choice 4: admin
#Changing ticket priority as an admin 

def changeTicketPriority(events):
    while True:                                      # Prompt the user to enter the ticket ID for which they want to change the priority
        ticket_id_to_change = input("Enter the ticket ID you want to change priority for: ")

                                                     # Check if the ticket ID exists in the list
        ticket_found = False
        for ticket in events:                        # Loop tickets in the events list to find the specified ID
            if ticket['ticket_id'] == ticket_id_to_change:
                ticket_found = True
                new_priority = int(input("Enter the new priority (integer value): "))
                ticket['priority'] = new_priority
                print(f"Priority of ticket {ticket_id_to_change} changed to {new_priority}.")
                break

        if ticket_found:
            break
        else:
            print("Ticket ID not found. Please enter an existing ticket ID.")


#Choice: 5 admin 
#Disable Tickets as an admin

def disableTicket(events):
    while True:                                     # Loop until a valid ticket ID is entered
        ticket_id_to_remove = input("Enter the ticket ID you want to remove: ")

        ticket_found = False
        for ticket in events:
            if ticket['ticket_id'] == ticket_id_to_remove:
                events.remove(ticket)
                print(f"Ticket {ticket_id_to_remove} has been removed.")
                ticket_found = True
                break

        if ticket_found:
            break
        else:
            print(f"Ticket with ID {ticket_id_to_remove} not found. Please enter an existing ticket ID.")



#choice 6: admin
 # Implement option 6 - Run Events as admin

def runEvents(events):
   
    today = datetime.date.today().strftime("%Y%m%d")

    today_tickets = [ticket for ticket in events if ticket['ticket_date'] == today]
    if not today_tickets:
        print("No events found for today.")
        return

    today_tickets.sort(key=lambda x: x['priority'], reverse=True)

    print("\nToday's Events (Sorted by Highest Priority):")
    for ticket in today_tickets:
        print(f"Event ID: {ticket['event_id']}, Ticket ID: {ticket['ticket_id']},Ticket Date: {ticket['ticket_date']}  "
              f"Username: {ticket['user_name']}, Priority: {ticket['priority']}")

    # Remove today's events from the queue
    events = [ticket for ticket in events if ticket['ticket_date'] != today]
    saveRemovedTicketToFile(events)
    print(" Displayed Tickts will be removed after exiting the program")



def saveRemovedTicketToFile(events):
    try:                                                # try block created to handle the file 
        with open(filePath, 'w') as file:               # with statement using write mode 
            for ticket in events:
                                                        #creating a string line using f"=
                line = f"{ticket['ticket_id']}, {ticket['ticket_date']}, {ticket['event_id']}, {ticket['user_name']}, {ticket['time_stamp']}, {ticket['priority']}\n"
                file.write(line)
        print("\n     *****Tickets Removed successfully.*****")
        print("\n          ---Updated list is Saved---")
    except Exception as errorfound:
        print("Error occurred while saving tickets:", errorfound)



#choice 7: admin
# Exit without Saving
def exit(events):
    
    print("\n**********BYE BYE!**********")
    return








#step 7: Normal user menu
##############################################################################################################################

def normalUserMenu(events, username):                       # Displays a menu with options for a normal user.
    while True:                                             # Display the User Menu Options
        print("\nUser Menu Options:")
        print("1. Book a Ticket")
        print("2. Save and Exit")

        choice = input("Enter your choice: ")               # Prompt the user to enter their choice

        if choice == '1':                                   # Check the user's choice and call the functions based on the input
            bookTicketForUser(events, username)             # Option 1 Book a Ticket:
        elif choice == '2':
            saveTicketToFile(events)                        # Option 2 Save and Exit: save the changes to the tickets and exit the program
            print("        Exiting the program.")
            return
        else:                                               # If the entered choice is invalid, display an error message
            print("Invalid choice. Try again.")




def bookTicketForUser(events, user_name):
    print(f"\n{user_name}!,")  # welcome the user by their name
    # Implement option 1 - Book a Ticket for User
    event_id = input("Enter event ID: ")
    current_date = datetime.datetime.now().strftime("%Y%m%d")
    priority = 0

    ticket_date = getValidTicketDate() 
    ticket_id = generateTicketId(events)

    new_ticket = {
        "ticket_id": ticket_id,
        "ticket_date": ticket_date.strftime("%Y%m%d"), 
        "event_id": event_id,
        "user_name": user_name,
        "time_stamp": current_date,
        "priority": priority
    }

    events.append(new_ticket)
    print("\nTicket booked successfully.")
    print('______________________')
    print(f"\n{user_name},\nyour new ticket is:")
    #print(new_ticket)
    printTicketInfo(new_ticket)



def printTicketInfo(ticket):
    # Format the ticket info as a readable string
    ticket_info = (
        f"Ticket ID: {ticket['ticket_id']}\n"
        f"Ticket Date: {ticket['ticket_date']}\n"
        f"Event ID: {ticket['event_id']}\n"
        f"Username: {ticket['user_name']}\n"
        f"Timestamp: {ticket['time_stamp']}\n"
        f"Priority: {ticket['priority']}"
    )
    print(ticket_info)
    print('______________________')




def getValidTicketDate():
    while True:                                        # Loop until a valid ticket date is entered
        try:
            date_str = input("Enter the ticket date (YYYYMMDD): ")  # Prompt the user to enter the ticket date in the format YYYYMMDD
            ticket_date = datetime.datetime.strptime(date_str, "%Y%m%d").date()# Convert the input date string to a datetime object using strptime with the specified format "%Y%m%d"
            today = datetime.date.today()          # Get the current date as a datetime object using date.today()
            
            if ticket_date >= today:               # Check if the entered ticket_date is greater than or equal to the current date 
                return ticket_date
            else:                                   # If the entered ticket_date is not valid (in the past), print an error message
                print("Ticket date must be in the future.")
        except ValueError:
            print("Invalid date format. Please enter a date in the format YYYY-MM-DD.")




def generateTicketId(events):
    if not events:                                    # Check if the events list is empty     
        return "tick101"                              # If the events list is empty, return a default ticket ID tick101
    
    last_ticket_id = events[-1]["ticket_id"]          # If the events list is not empty, get the ticket ID of the last ticket in the list
    ticket_num = int(last_ticket_id[4:]) + 1          # Extract the numeric part of the last_ticket_id by slicing the string from the 4th character to the end
    return f"tick{ticket_num:03d}"                    # Format the new ticket number as a 3-digit zero-padded string







#Step3: Defining The main function to read events from the file and call the login function.
############################################################################################################################

def main():
    events= readEventsFromFile(filePath)
    login(events)


#Step 3: program execution, calling the main function inside a '__main__' block.
if __name__ == '__main__':
    main()


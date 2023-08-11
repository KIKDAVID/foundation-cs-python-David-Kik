                                             # Define a class named TEEMZ
class TEEMZ:
    def __init__(self):
                                             # Initialize an empty dictionary to store user information and friend connections
        self.users = {}
    
                                             # Method to add a new user to the platform
    def addUser(self):
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        email = input("Enter email: ")
        
        user_info = (first_name, last_name)  # Create a tuple containing first name and last name
        
                                             # Check if the email already exists in the users dictionary
        if email in self.users:
            print("User with this email already exists.")
        else:
                                             # Add user information to the dictionary, including an empty set for friends
            self.users[email] = {"info": user_info, "friends": set()}
            print("User added successfully.")
    
                                             # Method to remove a user from the platform
    def removeUser(self, email):
                                             # Check if the given email exists in the users dictionary
        if email in self.users:
            user_info = self.users.pop(email)# Remove user info from dictionary
                                             # Iterate through the user's friends and remove the user from their friends sets
            for friend in user_info["friends"]:
                self.users[friend]["friends"].discard(email)
            print("User removed successfully.")
        else:
            print("User not found.")
    
                                             # Method to send a friend request
    def sendFriendRequest(self, sender_email, friend_email):
                                             # Check if both sender's and friend's emails exist in the users dictionary
        if sender_email in self.users and friend_email in self.users:
                                             # Update friend sets for both users
            self.users[sender_email]["friends"].add(friend_email)
            self.users[friend_email]["friends"].add(sender_email)
            print("Friend request sent successfully.")
        else:
            print("Invalid emails. Both users should exist.")
    
                                             # Method to remove a friend connection
    def removeFriend(self, user_email, friend_email):
                                             # Check if both user's and friend's emails exist in the users dictionary
        if user_email in self.users and friend_email in self.users:
                                             # Remove friend connections by updating friends sets for both users
            self.users[user_email]["friends"].discard(friend_email)
            self.users[friend_email]["friends"].discard(user_email)
            print("Friend removed successfully.")
        else:
            print("Invalid emails. Both users should exist.")
    
                                            # Method to view a user's friends
    def viewFriends(self, email):
                                            # Check if the given email exists in the users dictionary
        if email in self.users:
                                            # Get the user's friend set
            friends = self.users[email]["friends"]
            print("Friends list:")
                                            # Iterate through the friend set and display friend names
            for friend_email in friends:
                print(f"{self.users[friend_email]['info'][0]} {self.users[friend_email]['info'][1]}")
        else:
            print("User not found.")
    
                                            # Method to view all registered users
    def viewAllUsers(self):
        print("Registered users:")
                                            # Iterate through the users dictionary and display user names and emails
        for email, user_info in self.users.items():
            print(f"{user_info['info'][0]} {user_info['info'][1]} - {email}")
    
                                            # Method to display the main menu and handle user interactions
    def menu(self):
        print("Welcome to TEEMZ")
        while True:
            print("- - - - - - - - - - - - - - -")
            print("1. Add a user")
            print("2. Remove a user")
            print("3. Send a friend request")
            print("4. Remove a friend")
            print("5. View your list of friends")
            print("6. View the list of users")
            print("7. Exit")
            choice = input("Enter a choice: ")
            
                                            # Perform actions based on user's choice
            if choice == "1":
                self.addUser()              # Call the addUser method
            elif choice == "2":
                email = input("Enter user's email to remove: ")
                self.removeUser(email)      # Call the removeUser method
            elif choice == "3":
                sender_email = input("Enter your email: ")
                friend_email = input("Enter friend's email: ")
                self.sendFriendRequest(sender_email, friend_email)  # Call the sendFriendRequest method
            elif choice == "4":
                user_email = input("Enter your email: ")
                friend_email = input("Enter friend's email to remove: ")
                self.removeFriend(user_email, friend_email)  # Call the removeFriend method
            elif choice == "5":
                email = input("Enter your email: ")
                self.viewFriends(email)      # Call the viewFriends method
            elif choice == "6":
                self.viewAllUsers()          # Call the viewAllUsers method
            elif choice == "7":
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please choose again.")

                                            # Run the program if the script is executed directly
if __name__ == "__main__":
                                            # Create an instance of the TEEMZ class
    platform = TEEMZ()
                                            # Call the menu method to start the program
    platform.menu()

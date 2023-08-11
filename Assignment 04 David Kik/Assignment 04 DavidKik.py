class TEEMZSocialMedia:
    def __init__(self):
        self.users = {}
    
    def add_user(self):
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        email = input("Enter email: ")
        
        user_info = (first_name, last_name)
        
        if email in self.users:
            print("User with this email already exists.")
        else:
            self.users[email] = {"info": user_info, "friends": set()}
            print("User added successfully.")
    
    def remove_user(self, email):
        if email in self.users:
            user_info = self.users.pop(email)
            for friend in user_info["friends"]:
                self.users[friend]["friends"].discard(email)
            print("User removed successfully.")
        else:
            print("User not found.")
    
    def send_friend_request(self, sender_email, friend_email):
        if sender_email in self.users and friend_email in self.users:
            self.users[sender_email]["friends"].add(friend_email)
            self.users[friend_email]["friends"].add(sender_email)
            print("Friend request sent successfully.")
        else:
            print("Invalid emails. Both users should exist.")
    
    def remove_friend(self, user_email, friend_email):
        if user_email in self.users and friend_email in self.users:
            self.users[user_email]["friends"].discard(friend_email)
            self.users[friend_email]["friends"].discard(user_email)
            print("Friend removed successfully.")
        else:
            print("Invalid emails. Both users should exist.")
    
    def view_friends(self, email):
        if email in self.users:
            friends = self.users[email]["friends"]
            print("Friends list:")
            for friend_email in friends:
                print(f"{self.users[friend_email]['info'][0]} {self.users[friend_email]['info'][1]}")
        else:
            print("User not found.")
    
    def view_all_users(self):
        print("Registered users:")
        for email, user_info in self.users.items():
            print(f"{user_info['info'][0]} {user_info['info'][1]} - {email}")
    
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
            
            if choice == "1":
                self.add_user()
            elif choice == "2":
                email = input("Enter user's email to remove: ")
                self.remove_user(email)
            elif choice == "3":
                sender_email = input("Enter your email: ")
                friend_email = input("Enter friend's email: ")
                self.send_friend_request(sender_email, friend_email)
            elif choice == "4":
                user_email = input("Enter your email: ")
                friend_email = input("Enter friend's email to remove: ")
                self.remove_friend(user_email, friend_email)
            elif choice == "5":
                email = input("Enter your email: ")
                self.view_friends(email)
            elif choice == "6":
                self.view_all_users()
            elif choice == "7":
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    platform = TEEMZSocialMedia()
    platform.menu()

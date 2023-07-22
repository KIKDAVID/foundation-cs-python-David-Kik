
#exercise:1
#Write a function that takes an integer from the user and calculates its factorial, (The
#less than or equal to n)


#first we define the function that uses n number 
def factorialofnumb(n):

#then we specify the conditions under which the program may work in   
  if n == 0:
    return 1
  else:
    return n * factorialofnumb(n-1)

#last we produce a place for inputing the number and printing out the solution 
n = int(input("type a number to show its factorial : "))    
print( factorialofnumb(n) )








# Exercise 2  Write a function that takes an integer as an input from the user and finds all its divisors
#and stores them in a list.

def divisorNumber(n): #defining the function 
    divisors = []    #Initialize an empty list to store the divisors

    for i in range(1, n+1): #iterate from 1 to n (inclusive)
      if n % i == 0:
        divisors.append(i) # add the divisors to the list 
    return divisors
#prompt the user for an integer input 
num= int(input("Enter an integer to show a list of its divisors: "))

#call function to find divisors 
result = divisorNumber(num)

#print the divisors 
print( result)









#Exercise 3: Write a function called reverseString that takes a string as input from the user and returns
#the string reversed. You must use a loop to implement the reversal, and you cannot use any
#built-in string or list reversal functions.

def reverseString(s):#defining the function 
    reversed_str = "" #initialising an empty string 

    for i in range(len(s)-1, -1, -1): #iterate from last character to first character of the string 
        reversed_str += s[i]
    return reversed_str

input_str = input("Enter a string: ") #prompt the user 

reversed_str = reverseString(input_str) #call the function to reverse the string 

print("Reversed  String: ", reversed_str )#print the reversed string 






#Exersice 4: Write a function that takes a list of integers as input from the user and returns a new list
#containing only the even numbers from the original list, in the same order.

def getEvenNumbers(lst):#  defining the function lst 
    even_numbers = []#initializing an empty list 

    # Iterate through the list
    for num in lst:
        if num % 2 == 0:
            even_numbers.append(num)

    return even_numbers

# Prompt the user for a list of integers
input_list = input("Enter a list of integers (space-separated): ").split()
input_list = [int(num) for num in input_list]

# Call the function to get even numbers
even_nums = getEvenNumbers(input_list)

# Print the even numbers
print("Even Numbers:", even_nums)






#Exercise 4: Write a function that takes a string as input and checks whether it meets the requirements
#for a strong password. A strong password should be at least 8 characters long, contain at
#least one uppercase letter, one lowercase letter, one digit, and one special character (a
#special character is either #, ?, !, $).

def checkPasswordStrength(password):
    # Check password length
    if len(password) < 8:
        return "Weak password"

    has_uppercase = False
    has_lowercase = False
    has_digit = False
    has_special_char = False

    # Check each character of the password
    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_digit = True
        elif char in "#?!$":
            has_special_char = True

    # Check if all requirements are met
    if has_uppercase and has_lowercase and has_digit and has_special_char:
        return "Strong password"
    else:
        return "Weak password"

# Prompt the user for a password
input_password = input("Enter a password: ")

# Call the function to check password strength
result = checkPasswordStrength(input_password)

# Print the result
print(result)







#Exercise 5: Write a function that takes a string as input and checks
#whether it is a valid IPv4 address. A valid IPv4 address is a string of four numbers
#separated by periods, where each number is between 0 and 255.


def checkIpv4Address(ip_address):
    octets = ip_address.split(".")

    # Check if there are four octets
    if len(octets) != 4:
        return False

    # Check each octet
    for octet in octets:
        # Check if the octet is a valid integer
        if not octet.isdigit():
            return False

        # Check if the octet is between 0 and 255
        value = int(octet)
        if value < 0 or value > 255:
            return False

        # Check if the octet has leading zeros
        if len(octet) > 1 and octet[0] == '0':
            return False

    return True

# Prompt the user for an IP address
input_ip = input("Enter an IPv4 address: ")

# Call the function to check if it is a valid IPv4 address
is_valid_ipv4 = checkIpv4Address(input_ip)

# Print the result
if is_valid_ipv4:
    print("Valid IPv4 address")
else:
    print("Invalid IPv4 address")






#writing a Python program that utilizes recursive  functions. The program will begin by displaying a menu with four options:  
#1. Count Digits 
#2. Find Max 
#3. Count Tags 
#4. Exit 
#- - - - - - - - - - - - - - - 
#Enter a choice: 
#The user will select one of the options by entering the corresponding number. 
#Choice 1: will prompt the user to enter an integer and then recursively count the number of  digits in that integer. 
#Example 1: Input: 64 Output: 2 
#Example 2: Input: 252 Output: 3 
#Example 3: Input: 6 Output: 1 
#Choice 2: will prompt the user to enter a list of integers and then recursively find the maximum  value in the list (you cannot use the max function). 
#Example 1: Input: [13] Output: 13 
#Example 2: Input: [1, 6, -3, 1, 14, 9, 12, 24] Output: 24 
#Example 3: Input: [] Output: 0
#Choice 3: Given a valid HTML code as a multiline string (hard code the variable or read an  actual html file that would be a plus) and a tag, recursively count the occurrences of the tag in  the HTML code (the opening and closing tags are considered as one). 
#Example: Suppose the HTML code is as follows: 
#<html> 
#<head> 
#<title>My Website</title> 
#</head> 
#<body> 
#<h1>Welcome to my website!</h1> 
#<p>Here you'll find information about me and my hobbies.</p> 
#<h2>Hobbies</h2> 
#<ul> 
#<li>Playing guitar</li> 
#<li>Reading books</li> 
#<li>Traveling</li> 
#<li>Writing cool h1 tags</li> 
#</ul> 
#</body> 
#</html> 
#If the user enters "h1" as the tag, the program should recursively count the occurrences of the  "h1" tag in the HTML code, which is 1. Similarly, if the user enters "li" as the tag, the program  should recursively count the occurrences of the "li" tag, which is 4. 
#Note that the opening and closing tags are considered as one. In the example above, there is only  one "h1" tag, even though there is both an opening and a closing tag. 
#Hint: you should get more familiar with the structure of an HTML code, and how opening tags  and closing tags work. 
#Choice 4: will terminate the program.
#Note: you can add extra parameters to the function for each choice. 






###########################################################################


#starting with the functions needed 
#CHOICE 1

# defining a recursive function to count the number of digits in an integer.
def count_digits(n):
    if n < 10:
        return 1
    else:
        return 1 + count_digits(n // 10)
#The count_digits function takes an integer n as input and returns the count of its digits.

#The base case of the recursion is when the input number n is less than 10. In this case, it means that n has only one digit, so the function returns 1

#If the input number n is greater than or equal to 10, the function moves to the recursive step. It divides the number n by 10 using the // operator. This removes the last digit from the number. Example, if n is 123, n // 10 will be 12

#The function recursively calls itself with the updated value of n // 10. This step continues until the base case is reached, n become less than 10

#After the recursive call, the function returns 1 plus the result of the recursive call. This accounts for the current digit that was removed earlier 

#The recursive calls continue to unwind, and each recursive call adds 1 to the count until the original number n becomes less than 10


##############################################################################


#CHOICE 2 
#The find_max function takes a list of integers nums as input and returns the maximum value in the list.
def find_max(nums):
  
    if len(nums) == 0:
        return 0
    elif len(nums) == 1:
        return nums[0]
    else:
        mid = len(nums) // 2
        left_max = find_max(nums[:mid])
        right_max = find_max(nums[mid:])
        return left_max if left_max > right_max else right_max

#The base case of the recursion is when the length of the input list nums is 0. In this case, since there are no elements in the list, the function returns 0.

#If the length of the input list nums is 1, it means there is only one element in the list. In this case, the function directly returns that element as the maximum value, by using [0] indexing 

#If the length of the input list nums is greater than 1, the function moves to the recursive step. It finds the middle index of the list by dividing the length of nums by 2 using the // operator.

#The function recursively calls itself with two sublists: nums[:mid] represents the left half of the list, and nums[mid:] represents the right half of the list.

#Each recursive call finds the maximum value in the respective sublist by calling find_max recursively.

#Finally, the function compares the maximum values obtained from the left and right sublists. It returns the greater value as the overall maximum value in the original list.


##############################################################################

#CHOICE 3 
# defining count tags function that takes html and tag as arguments

def count_tags(html, tag):
  # Construct the opening and closing tags
    opening_tag = "<" + tag + ">"
    closing_tag = "</" + tag + ">"
  
  # Initialize the count
    count = 0
  
  # Find the start index of the opening tag
    start = html.find(opening_tag)

  # If the opening tag is not found, return the count
    if start == -1:
        return count

  # Find the end index of the closing tag starting from the start index
    end = html.find(closing_tag, start)

  # If the closing tag is not found, return the count
    if end == -1:
        return count

  # Increment the count by 1 since an opening and closing tag pair is found
    count += 1

  # Get the remaining HTML after the current closing tag
    remaining_html = html[end + len(closing_tag):]

  # Recursively call the function with the remaining HTML to count additional occurrences of the tag
    return count + count_tags(remaining_html, tag)


  #The function count_tags takes two parameters: html (the HTML code as a string) and tag (the tag to count occurrences of).

#The opening and closing tags are constructed by concatenating the input tag with appropriate brackets and slashes.

#The count variable is initialized to 0 to keep track of the number of occurrences of the tag.

#The function finds the start index of the opening tag within the html string using the find method.

#If the opening tag is not found (start is -1), it means there are no more occurrences of the tag, so the function returns the current count.

#If the opening tag is found, the function proceeds to find the end index of the closing tag. The search for the closing tag starts from the start index using the find method.

#If the closing tag is not found (end is -1), it means the HTML is invalid or incomplete, so the function returns the current count.

#If both the opening and closing tags are found, it indicates an occurrence of the tag. The count is incremented by 1.

#The function then extracts the remaining HTML content after the current closing tag using slicing.

#Finally, the function recursively calls itself with the remaining HTML to count additional occurrences of the tag. The result is added to the current count and returned.

#The recursive calls continue until there are no more occurrences of the tag or the HTML is invalid. The count is accumulated through each recursive call, and the final count is returned as the output.


##############################################################################

#CHOICE 4 & Menu
#displaying a menu with four options:  
#1. Count Digits 
#2. Find Max 
#3. Count Tags 
#4. Exit 
#- - - - - - - - - - - - - - - 
#here the user will enter a choice: 
#The user will select one of the options by entering the corresponding number. 

# we start by defining main():
#The main function is defined to handle the program's main logic.

#The program enters an infinite loop using while True to repeatedly display the menu and get the user's choice.

#Inside the loop, the menu options are displayed using print statements.

#The user's choice is obtained using input and stored in the choice variable.
#The program then checks the user's choice using an if-elif-else structure.

#If the choice is '1', the program executes the block for option 1: Count Digits. It prompts the user to enter an integer, calls the count_digits function to count the digits, and prints the result.

#If the choice is '2', the program executes the block for option 2: Find Max. It prompts the user to enter a list of integers, converts the input to a list of integers, calls the find_max function to find the maximum value, and prints the result.

#If the choice is '3', the program executes the block for option 3: Count Tags. It assigns a hardcoded HTML code to the html variable (or you can read it from an actual HTML file), prompts the user to enter a tag, calls the count_tags function to count the occurrences of the tag in the HTML, and prints the result.

#If the choice is '4', the program executes the block for option 4: Exit. It breaks out of the loop, terminating the program.

#If the choice does not match any of the valid options, the program executes the else block and prints an error message.

#The if __name__ == "__main__" condition ensures that the main function is only executed when the script is run directly, not when it is imported as a module.

#The program continues to loop until the user chooses the "Exit" option.
def main():
    while True:
      # Display the menu options
        print("1. Count Digits")
        print("2. Find Max")
        print("3. Count Tags")
        print("4. Exit")

      # Get the user's choice
        choice = input("Enter a choice: ")

        if choice == '1':
      # Option 1: Count Digits
            num = int(input("Enter an integer: "))
            count = count_digits(abs(num))
            print("Number of digits:", count)
          
        elif choice == '2':
      # Option 2: Find Max 
            nums = input("Enter a list of integers (space-separated): ").split()
            nums = [int(x) for x in nums]
            max_num = find_max(nums)
            print("Maximum value:", max_num)
          
        elif choice == '3':
      # Option 3: Count Tags  
            html = '''
                <html>
                <head>
                <title>ELKIK TRADING</title>
                </head>
                <body>
                <h1>Welcome to elkik.com</h1>
                <p>Here you'll find information about me and my hobbies.</p>
                <h2>Hobbies</h2>
                <ul>
                <li>Playing guitar</li>
                <li>Reading books</li>
                <li>Traveling</li>
                <li>My Motto: if you're going to get wet, why not go for a swim !!! </li>
                </ul>
                </body>
                </html>
            '''
            tag = input("Enter a tag: ")
            count = count_tags(html, tag)
            print("Occurrences of tag:", count)
          
        elif choice == '4':
     # Option 4: Exit
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
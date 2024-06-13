# Side note - this is the first time i've been scared of losing my code / accidentally deleting file ect.
# Difficult task, took several days and headaches. Realized I needed functions to repeat the menu call after calc.
# See Pseudo Code text file
# Did thorough testing...

'''
imports the modules required to add a delay, then exits the program.
I researched how to add a delay:
https://stackoverflow.com/questions/510348/how-do-i-make-a-time-delay
'''
import sys
import time


# Functions required for the menu() function, essential for the app. Also super neat (when closed - VS)

def num_one():
    # Function requesting 1st number from user, if input is invalid it repeats request. After 5 repeats it will close the program.

    tries = 0
    while tries < 5:
        try:
            first_num = float(input('\n\nPlease provide the first number: '))
            return first_num
        except ValueError:
            print("\nYou've provided an invalid number!")
            tries += 1
    if tries == 5:
        print("\n\n\nDue to invalid inputs, the program will now close. Have a great day!")
        time.sleep(1.2)
        sys.exit()


def op_func():
    # Function requesting the operation to be used, if input is invalid it repeats request. After 5 repeats it will close the program.

    operator_info = """\n\nPlease type which operation-type you wish to perform.

The Choices are:

    "+" For Addition
    "-" For Subtraction
    "*" For Multiplication
    "/" For Division

Operation: """
    valid_operation = ["+", "-", "*", "/"] # List of valid operations
    tries = 0

    while tries < 5:
        operation = input(operator_info)
        if operation in valid_operation:
            return operation
        else:
            print("\n\nYou've provided an invalid operation!")
            tries += 1
    if tries == 5:
        print("\n\n\nDue to invalid inputs, the program will now close. Have a great day!")
        time.sleep(1.2)
        sys.exit()


def num_two():
    # Function requesting 2nd number from user, if input is invalid it repeats request. After 5 repeats it will close the program.

    tries = 0
    while tries < 5:
        try:
            second_num = float(input('\n\nPlease provide the second number: '))
            return second_num
        except ValueError:
            print("\nYou've provided an invalid number!")
            tries += 1
    if tries == 5:
        print("\n\n\nDue to invalid inputs, the program will now close. Have a great day!")
        time.sleep(1.2)
        sys.exit()


def calc_answer():
    # Function making a calculation based on the user's chosen operation and the 2 numbers provided, stores the answer

    first_number = num_one()
    operation = op_func()
    second_number = num_two()
    
    try:
        if operation == "+":
            answer = first_number + second_number
        elif operation == "-":
            answer = first_number - second_number
        elif operation == "*":
            answer = first_number * second_number
        elif operation == "/":
            answer = first_number / second_number
    except ZeroDivisionError:
        print("\n\nYou're trying to divide by 0 aren't you? \nThe Answer is: undefined...I'll send you back to Main Menu\n\n")
        menu()

    # Showing the user their calculation and answer
    equation = f"{first_number} {operation} {second_number} = {answer}" 
    print("\n\nCalculation: " + equation + "\n\n")
    
    # Adding the completed calculation to the text file
    with open('equations.txt', 'a') as equations_file:
        equations_file.write(equation + "\n")


def menu():
    '''
    Creates a function requesting user to make a choice.
    Starts calculation if 1, shows calculation history if 2, closes program if 3.
    Otherwise it repeats the request to user due to invalid input. After 5 repeats it will close the program.
    '''

    greeting = """Welcome to Simple Calculator Dot IO!

Please type the corresponding number to select an option:

    1. Perform a simple calculation between 2 values.
    2. Show all previous calculations.
    3. Exit Program.

Your selection: """

    tries = 0
    while tries < 5:
        start_choice = input(greeting)

        if start_choice == "1":
            calc_answer()
        elif start_choice == "2":
            try:
                with open('equations.txt', 'r') as lines:
                    calculations = ""
                    for line in lines: # Loops through all lines in the file and stores it in calculations
                        calculations += line
                    print("\n\nYour previous calculations are:\n\n" + calculations + "\n")
            except FileNotFoundError:
                print("\n\nYou have not calculated anything yet...\n\n")
        elif start_choice == "3":
            print("\n\nHave a great day!")
            time.sleep(1.1)
            sys.exit()
        else:
            print("\n\nThe value provided is invalid! Please type a number from 1 to 3!\n\n")
            tries += 1
    if tries == 5:
        print("\nDue to invalid inputs, the program will now close. Have a great day!\n")
        time.sleep(1.2)
        sys.exit()


# Calls function. The start of the app!
menu()
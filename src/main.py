from datetime import datetime
from utils import*

print("Developer: ")
name = "Badhon Pain"
print(f"Name: {name}")

now = datetime.now()
print("Now:", now.strftime("%Y-%m-%d %H:%M:%S"))

def printCommands():
    print('''
        1. addition
        2. subtraction
        3. multiplication
        4. division
        5. exit
    ''')

def takeInput():
    a = int(input("Enter 1st number: "))
    b = int(input("Enter 2nd number: "))
    return a, b

printCommands()
while True:
    operation = input("Enter operation name: ")

    if operation == "exit":
        break
    elif operation == "help":
        printCommands()
    elif operation == "addition":
        a, b = takeInput()
        print(add(a, b))
    elif operation == "subtraction":
        a, b = takeInput()
        print(subtract(a, b))
    elif operation == "multiplication":
        a, b = takeInput()
        print(multiply(a, b))
    elif operation == "division":
        a, b = takeInput()
        print(divide(a, b))
    else :
        print("Invalid command !! Type 'help' to see available all commands.")




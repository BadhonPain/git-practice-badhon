from datetime import datetime
from utils import*

print("Developer: ")
name = "Badhon Pain"
print(f"Name: {name}")

now = datetime.now()
print("Now:", now.strftime("%Y-%m-%d %H:%M:%S"))

print('''
        1. addition
        2. subtraction
        3. multiplication
        4. division
      ''')
a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
operation = input("Enter operation name: ")
if operation=="addition" :
    print(add(a, b))
elif operation== "subtraction":
    print(subtract(a, b))
elif operation== "multiplication":
    print(multiply(a, b))
elif operation== "division":
    print(divide(a, b))
else:
    print("Invalid command! Try again")


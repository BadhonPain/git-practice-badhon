def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a, b):
    return a*b

def divide(a, b):
    if b==0:
       print("Can't divide by zero !!") 
       return 
    return a/b

    

print(add(5,7))
print(subtract(5,7))
print(multiply(5, 7))
print(divide(5, 7))
print(divide(2, 0))
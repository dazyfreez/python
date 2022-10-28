
#this will be a calculator

def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y
def power(x,y):
    return x**y
def square(x):
    return x**2
def root(x):
    return x**0.5
def discriminant(a,b,c):
    return b**2-4*a*c

print ("Welcome to the calculator")
print ("What do you want to do?")
print ("1. Add")
print ("2. Subtract")
print ("3. Multiply")
print ("4. Divide")
print ("5. Power")
print ("6. Square")
print ("7. Root")
print ("8. Discriminant")
print ("9. Exit")
# now we created a menu
# now we need a variable to store the user input
choice = input("Please enter your choice: ")
# now we need to check if the user input is valid
if choice in ('1','2','3','4','5','6','7','8','9'):
    if choice == '1':
        print ("Add")
        a = int(input("Please enter a number: "))
        b = int(input("Please enter a number: "))
        print (a,"+",b,"=", add(a,b))
    elif choice == '2':
        print ("Subtract")
        a = int(input("Please enter a number: "))
        b = int(input("Please enter a number: "))
        print (a,"-",b,"=", subtract(a,b))
    elif choice == '3':
        print ("Multiply")
        a = int(input("Please enter a number: "))
        b = int(input("Please enter a number: "))
        print (a,"*",b,"=", multiply(a,b))
    elif choice == '4':
        print ("Divide")
        a = int(input("Please enter a number: "))
        b = int(input("Please enter a number: "))
        print (a,"/",b,"=", divide(a,b))
    elif choice == '5':
        print ("Power")
        a = int(input("Please enter a number: "))
        b = int(input("Please enter a number: "))
        print (a,"**",b,"=", power(a,b))
    elif choice == '6':
        print ("Square")
        a = int(input("Please enter a number: "))
        print (a,"**2","=", square(a))
    elif choice == '7':
        print ("Root")
        a = int(input("Please enter a number: "))
        print (a,"**0.5","=", root(a))
    elif choice == '8':
        print ("Discriminant")
        a = int(input("Please enter a number: "))
        b = int(input("Please enter a number: "))
        c = int(input("Please enter a number: "))
        print (b,"**2-4*",a,"*",c,"=", discriminant(a,b,c))
        if discriminant(a,b,c) == 0:
            print ("The discriminant is wrong")
    elif choice == '9':
        print ("Program has ended")

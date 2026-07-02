def add(a, b) :
    return a + b


def subtract(a, b) :
    return a - b


def multiply(a, b) :
    return a * b


def divide(a, b) :
    if b == 0:
        return "Can't divide by zero."
    else:
        return a / b
    
def remainder(a,b) :
    if b == 0 :
        return "Can't divide by zero."
    else:
        return a % b
    
def square(a) :
    return a**2
    
def cube(a) :
    return a**3
    
def get_number(message) :

    while True :

        try :
            number = float(input(message))
            return number

        except :
            print("Please enter a valid number.")
    
print("\n Calculator Menu:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Remainder")
print("6. Square")
print("7. Cube")

while True :
    choice = input("Enter your choice (1-7): ")

    if choice in ["1", "2", "3", "4", "5", "6", "7"] :
        break

    print("Invalid Choice! Try Again.")


if choice in ["1", "2", "3", "4", "5"] :
    a = get_number("Enter first number: ")
    b = get_number("Enter second number: ")

elif choice in ["6", "7"] :
    number = get_number("Enter the number: ")

if choice == "1" :
    print("Result:", add(a,b))
elif choice == "2" :
    print("Result:", subtract(a,b))
elif choice == "3" :
    print("Result:", multiply(a,b))
elif choice == "4" :
    print("Result:", divide(a,b))
elif choice == "5" :
    print("Result:", remainder(a,b))
elif choice == "6" :
    print("Result:", square(number))
elif choice == "7" :
    print("Result:", cube(number))
else :
    print("Invalid Choice!")
def menu() :
    print("\n----- Unit Converter -----")
    print("1. Kilometers to Miles")
    print("2. Celsius to Fahrenheit")
    print("3. Kilograms to Pounds")
    print("4. Miles to Kilometers")
    print("5. Fahrenheit to Celcius")
    print("6. Pounds to Kilograms")


def get_choice() :
    choice = input("Enter your choice: ")
    return choice


def km_to_miles(km) :
    miles = km * 0.621371
    return miles


def celsius_to_fahrenheit(c) :
    fahrenheit = (c * 9/5) + 32
    return fahrenheit


def kg_to_pounds(kg) :
    pounds = kg * 2.20462
    return pounds


def miles_to_km(mil) :
    kil_m = mil / 0.621371
    return kil_m


def fah_to_cel(f) :
    cel =  (f - 32) * 5/9
    return cel


def pounds_to_kg(pou) :
    kil_g = pou / 2.20462
    return kil_g


def display_result(result, unit):
    print(f"Result: {result:.2f} {unit}")



menu()

choice = get_choice()

if choice == "1" :
    km = float(input("Enter Kilometers: "))
    result = km_to_miles(km)
    display_result(result, "Miles")

elif choice == "2" :
    c = float(input("Enter Celsius: "))
    result = celsius_to_fahrenheit(c)
    display_result(result, "Fahrenheit")

elif choice == "3" :
    kg = float(input("Enter Kilograms: "))
    result = kg_to_pounds(kg)
    display_result(result, "Pounds")

elif choice == "4" :
    mil = float(input("Enter Miles: "))
    result = miles_to_km(mil) 
    display_result(result, "Kilometers")

elif choice == "5" :
    f = float(input("Enter Fahrenheit: "))
    result = fah_to_cel(f)
    display_result(result, "Celsius")

elif choice == "6" :
    pou = float(input("Enter Pounds: "))
    result = pounds_to_kg(pou)
    display_result(result, "Kilograms")

else :
    print("Invalid Choice")
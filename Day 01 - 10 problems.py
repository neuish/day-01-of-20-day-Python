

#1. Write a program that prints your name, age, and favorite hobby.

def personal_details():
    name = input('enter your name in string:')
    age = input('enter the age in number:')
    hobby = input('enter your fav hobby in string:')
    print(f"{name} age is {age} and their fav hobby is {hobby}")


#2. Create a program that performs basic arithmetic operations (add, subtract, multiply, divide).

def basic_operation():
    x, y = map(int, input('enter 2 numbers saperated by space:').split())
    z = input('choose an operand:')
    if z == '+' : print(x + y)
    elif z == '-' : print(x - y)
    elif z == '*' : print(x * y)
    elif z == '/' : print(x / y)
    else: print('invalid operation, please try again')
    

#3. Write a program that converts kilometers to miles. note: 1 km = 0.6213712

def KM_to_mile():
    Km = float(input('enter the KM you want to convert to miles:'))
    mile = Km / 0.63
    print(f"{Km} kilometer is equal to {mile:.2f} miles")


#4. Create a program that calculates the area of a circle given its radius

def area_of_circle():
    r = float(input('enter the radius'))
    pi = 3.16
    area = pi * pow(r, 2)
    print(f"area od circle is {area:.2f}")



#5. Write a program that converts a temperature from Celsius to Fahrenheit. Use the formula:

def celcius_to_fahrenheit():
    celsius = float(input('enter the temperature in celsius:'))
    conversion = (celsius * (9/5)) + 32
    print(f"the converted temperature is {conversion:.2f}")


#6. Create a program that calculates simple interest. The formula is:

def simple_interest():
    P, R, T = map(float, input('enter principle, yearly rate, and time saperated by a space: ').split())
    SI = (P*R*T)/100
    print(f" the total simple interest for given time {T} years is {SI:.2f}")



#7. Write a program that calculates the Body Mass Index

def body_mass_index():
    x, y = map(float, input('enter height in metere and weight in Kg:').split())
    BMI = y / pow(x, 2) 
    print(f" the BMI is {BMI:2f}")



#8. Create a program that takes an input of time in minutes and converts it into hours and minutes

def hour_to_min():
    minute = int(input('enter time in minutes:'))
    hr = int(minute / 60)
    min = minute % 60
    print(f"the time is {hr} hours and {min} minutes")

#9. Write a program that takes three numbers as input and calculates their average.

def averge():
    x, y, z = map(int, input('enter 3 numbers saperated by space:').split())
    avg = (x+y+z)/3
    print(f" the average is {avg}")

#10. assembling all those into a bigger program using function definations for each
def main_menu():
    while True:
        print("\n--- Main Menu ---")
        print("1. Print Personal Details")
        print("2. Basic Arithmetic Operations")
        print("3. Kilometers to Miles Converter")
        print("4. Area of a Circle Calculator")
        print("5. Temperature Converter (Celsius to Fahrenheit)")
        print("6. Simple Interest Calculator")
        print("7. BMI Calculator")
        print("8. Time Converter (Minutes to Hours and Minutes)")
        print("9. Average of Three Numbers")
        print("0. Exit")
           # User input for menu choice
        choice = input("Enter your choice (0-10): ")

        # Running corresponding function based on user's choice
        if choice == "1":
            personal_details()
        elif choice == "2":
            basic_operation()
        elif choice == "3":
            KM_to_mile()
        elif choice == "4":
            area_of_circle()
        elif choice == "5":
            celcius_to_fahrenheit()
        elif choice == "6":
            simple_interest()
        elif choice == "7":
            body_mass_index()
        elif choice == "8":
            hour_to_min()
        elif choice == "9":
            averge()
        elif choice == "0":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

# Running the main menu
main_menu()
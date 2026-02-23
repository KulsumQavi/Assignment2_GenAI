print("Temperature converter")
print("1.Celsius to Fahrenheit")
print("2.Fahrenheit to Celsius")
print("3.Celsius to Kelvin")
print("4.Kelvin to Celsius")
print("5.Fahrenheit to Kelvin")
print("6.Kelvin to Fahrenheit")
print("7.Exit")

while True:
    choice =int(input("Enter your choice to convert temperature between number 1to 7 :"))

    #1:Celsius to Fahrenheit 
    if choice == 1:
        celsius =float(input("Enter temperature in Celsius: "))
        fahrenheit =(celsius * 9/5) + 32
        print("Result:", celsius,"°C =", fahrenheit,"°F")

    #2:Fahrenheit to Celsius
    elif choice == 2:
        fahrenheit = float(input("Enter temperature in Fahrenheit:"))
        celsius = (fahrenheit -32) * 5/9
        print("Result:",fahrenheit,"°F =",celsius,"°C")

    #3:Celsius to Kelvin
    elif choice == 3:
        celsius = float(input("Enter temperature in Celsius:"))
        kelvin = celsius + 273.15
        print("Result:",celsius,"°C =",kelvin,"K")

    #4:Kelvin to Celsius 
    elif choice == 4:
        kelvin = float(input("Enter temperature in Kelvin: "))
        celsius = kelvin - 273.15
        print("Result:",kelvin,"K =", celsius, "°C")

    #5: Fahrenheit to Kelvin
    elif choice ==5:
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        kelvin =(fahrenheit - 32) * 5/9 + 273.15
        print("Result:",fahrenheit,"°F =",kelvin,"K")

    #6:Kelvin to Fahrenheit
    elif choice == 6:
        kelvin =float(input("Enter temperature in Kelvin: "))
        fahrenheit =(kelvin -273.15)* 9/5 + 32
        print("Result:",kelvin,"K =",fahrenheit,"°F")

    #7:Exit
    elif choice== 7:
        print("Exit the program")
        break

    #Invalid choice
    else:
        print("Error Please enter a number between 1 and 7")

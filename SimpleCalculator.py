# Get User Input
try:
    # Ask the user to enter two numbers it can be of type int or float
    n1  = float(input("Enter first number: "))
    n2 = float(input("Enter second number: "))

    # Perform Calculations
    addition       = n1+n2 # Sum
    subtraction    = n1-n2 # Difference
    multiplication = n1*n2 # Product
    modulus        = n1%n2  # Remainder
    exponentiation = n1**n2# Exponent

    # If second number is zero it cannot be divided so it required special handling
    if n2== 0:
        division = "undefined it cannot divided by zero"
    else:
        division = round(n1/n2, 2)  # Rounding to 2 decimal places

    print("\nResults:")
    print(f"{n1}+{n2} = {addition}")
    print(f"{n1}-{n2} = {subtraction}")
    print(f"{n1}*{n2} = {multiplication}")
    print(f"{n1}/{n2} = {division}")
    print(f"{n1}%{n2} = {modulus}")
    print(f"{n1}^{n2} = {exponentiation}")

# Handling Invalid Input 
except ValueError:
    # Trigger when the user types something that is not of type integer or float
    print("Invalid input! Please enter int and float values only.")

except ZeroDivisionError:
    # Safety for modulus with zero 
    print("Error: Cannot perform modulus operation with zero.")
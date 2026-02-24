#Function to add two numbers
def add(a, b):
    return a + b
#Function to subtract two numbers
def subtract(a, b):
    return a - b
#Function to multiply two numbers
def multiply(a, b):
    return a * b
#Function to divide two numbers
def divide(a, b):
    # Handle division by zero
    if b == 0:
        return "Error: cannot divide by zero!"
    return a / b
#Function to find modulus (remainder)
def modulus(a, b):
    # Handle modulus by zero
    if b == 0:
        return "Error it cannot divide by zero"
    return a % b
#Function to find power
def power(a, b):
    return a ** b
#main function
def calculator():
    while True:
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Modulus")
        print("6. Power")
        print("7. Exit")
        try:
            choice = int(input("Enter choice: "))

            #Exit
            if choice == 7:
                print("Exiting Calculator")
                break

            #Invalid Choice 
            elif choice < 1 or choice > 7:
                print("enter a choice between 1 and 7")

            else:
                # Getting Two Numbers from user
                a = float(input("Enter first number : "))
                b = float(input("Enter second number: "))

                if choice == 1:
                    result = add(a, b)
                    print(a, "+", b, "=", result)

                elif choice == 2:
                    result = subtract(a, b)
                    print(a, "-",b,"=",result)

                elif choice == 3:
                    result = multiply(a,b)
                    print(a,"*",b,"=",result)

                elif choice ==4:
                    result =divide(a,b)
                    print(a,"/",b,"=",result)

                elif choice == 5:
                    result =modulus(a,b)
                    print(a,"%", b,"=",result)

                elif choice == 6:
                    result=power(a,b)
                    print(a,"^",b,"=",result)

        except ValueError:
            print("Error enter valid numbers only!")

calculator()
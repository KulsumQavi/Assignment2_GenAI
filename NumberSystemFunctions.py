#Function 1:Factorial
def factorial(n):
    if n < 0:
        return "Error Negative number"
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result

# Function 2:Prime Checker
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

#Function 3: Fibonacci
def fibonacci(n):
    if n <= 0:
        return "Error Enter positive number"
    if n == 1:
        return 0
    if n == 2:
        return 1
    first = 0
    second = 1
    for i in range(2, n):
        third = first + second
        first = second
        second = third
    return second

#Function 4:Sum of Digits
def sum_of_digits(n):
    n = abs(n)
    total = 0
    n = str(n)
    for digit in n:
        total = total + int(digit)
    return total

#Function 5:Reverse Number
def reverse_number(n):
    negative = False
    if n < 0:
        negative = True
        n = abs(n)
    n = str(n)
    reversed_n = ""
    for i in range(len(n) - 1, -1, -1):
        reversed_n = reversed_n + n[i]
    if negative:
        return -int(reversed_n)
    else:
        return int(reversed_n)

#Function 6:Armstrong checker
def is_armstrong(n):
    digits =str(n)
    power =len(digits)
    total =0
    for digit in digits:
        total = total +int(digit)**power
    if total == n:
        return True
    else:
        return False

#Function 7:GCD
def gcd(a,b):
    while b != 0:
        remainder = a%b
        a=b
        b=remainder
    return a

# Function 8: LCM
def lcm(a,b):
    return (a*b)//gcd(a,b)

#Function 9: Perfect Number
def is_perfect_number(n):
    if n <= 1:
        return False
    total = 0
    for i in range(1,n):
        if n % i == 0:
            total =total +i
    if total == n:
        return True
    else:
        return False

# Main Function
def math_menu():

    while True:

        print("1.Factorial")
        print("2.Prime Checker")
        print("3.Fibonacci")
        print("4.Sum of Digits")
        print("5.Reverse Number")
        print("6.Armstrong Checker")
        print("7. GCD")
        print("8. LCM")
        print("9.Perfect Number Checker")
        print("10.Exit")

        try:
            choice = int(input("Enter choice:"))

            if choice == 10:
                print("Exit")
                break

            elif choice < 1 or choice > 10:
                print("enter a choice between 1 and 10")

            elif choice == 1:
                n = int(input("Enter a number:"))
                print("Factorial =", factorial(n))

            elif choice == 2:
                n =int(input("Enter a number:"))
                if is_prime(n):
                    print(n,"is a prime number")
                else:
                    print(n,"is not a prime number")

            elif choice == 3:
                n = int(input("Enter position:"))
                print("Fibonacci at position",n,"=",fibonacci(n))

            elif choice == 4:
                n = int(input("Enter a number:"))
                print("Sum of digits =", sum_of_digits(n))

            elif choice == 5:
                n = int(input("Enter a number:"))
                print("Reversed =",reverse_number(n))

            elif choice == 6:
                n =int(input("Enter a number: "))
                if is_armstrong(n):
                    print(n, "is an Armstrong number")
                else:
                    print(n, "is not an Armstrong number")

            elif choice == 7:
                a = int(input("Enter first number:"))
                b = int(input("Enter second number:"))
                print("GCD =", gcd(a, b))

            elif choice == 8:
                a = int(input("Enter first number:"))
                b = int(input("Enter second number:"))
                print("LCM =", lcm(a,b))

            elif choice == 9:
                n = int(input("Enter a number:"))
                if is_perfect_number(n):
                    print(n,"is a Perfect number")
                else:
                    print(n,"is NOT a perfect number")

        except ValueError:
            print("Enter valid numbers only")
math_menu()
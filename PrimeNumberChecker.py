#PART 1: Check Single Number
try:
    #Get Input from User
    number = int(input("Enter a number: "))
    # Negative numbers and 0 are not prime
    if number < 0:
        print(number, "is NOT a prime number (negative numbers are not prime numcers)")

    # 0 is not prime
    elif number == 0:
        print("0 is NOT a prime number")

    # 1 is not prime
    elif number == 1:
        print("1 is NOT a prime number")

    # 2 is the only even prime number
    elif number == 2:
        print("2 is a PRIME number")

    else:
        #Check if Number is Prime
        # Assume number is prime at start
        is_prime = True

        # Check if number is divisible by any number from 2 to number-1
        for i in range(2, number):
            if number % i == 0:# If divisible then not prime
                is_prime = False
                break  #No need to check further

        #Display Result
        if is_prime:
            print(number, "is a PRIME number")
        else:
            print(number, "is NOT a prime number")


#PART 2: Find Primes in a Range

    print()
    start = int(input("Enter start range: "))
    end   = int(input("Enter end range  : "))

    if start > end:
        print("Error: Start range cannot be greater than end range!")

    else:
        #Find All Primes in Range 
        prime_in_range = ""  #Store all primes as a string

        for num in range(start, end + 1):
            #Skip numbers less than 2
            if num < 2:
                continue

            #Check if num is prime
            is_prime = True

            for i in range(2, num):
                if num % i == 0:
                    is_prime = False
                    break

            #If prime add to the list
            if is_prime:
                if prime_in_range == "":
                    prime_in_range  = str(num)#First prime in range
                else:
                    prime_in_range =prime_in_range + ", "+ str(num) # Add comma before next prime in range

        #Display Result
        if prime_in_range  == "":
            print("No prime numbers found in the range")
        else:
            print("Prime numbers:",prime_in_range )

except ValueError:
    print("Errorenter valid numbers only")
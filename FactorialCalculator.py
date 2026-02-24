try:
    #Get Input from User
    number =int(input("Enter a number:"))

    #Negative Numbers does not have factorial
    if number < 0:
        print("ErrorFactorial of negative number is not possible")

    # Handle 0
    # to handle zero factorial (0! = 1) 
    elif number == 0:
        print("0! = 1")

    else:
        #Calculate Factorial using Loop
        factorial = 1

        #Multiply from number down to 1
        for i in range(number, 0, -1):
            factorial = factorial * i

        #Building the step string like 5 x 4 x 3 x 2 x 1
        steps = ""
        for i in range(number, 0, -1):
            if i == 1:
                steps=steps+str(i) #Last number x after it
            else:
                steps=steps+str(i) +"x"#Adding x between numbers

        #Result 
        print(str(number)+"! = "+steps+"=" +str(factorial))

except ValueError:
    print("Error enter a valid number")
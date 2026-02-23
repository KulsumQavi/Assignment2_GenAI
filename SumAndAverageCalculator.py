try:
    #Get How Many Numbers 
    count = int(input("How many numbers?"))

    #Check Valid Input
    if count <= 0:
        print("Error enter a number greater than 0")

    else:
        #Take Numbers as Input using Loop
        total   = 0
        maximum = 0
        minimum = 0

        for i in range(1, count + 1):
            number = float(input("Enter number " + str(i) + ": "))

            # Add number to total
            total = total + number

            # Set first number as max and min
            if i == 1:
                maximum=number
                minimum = number

            # Checking if current number is greater than maximum
            if number >maximum:
                maximum = number

            # Checking if current number is less than minimum
            if number<minimum:
                minimum= number

         #Calculating average 
        average = total / count

        print("Sum     :", total)
        print("Average :", average)
        print("Maximum :", maximum)
        print("Minimum :", minimum)

except ValueError:
    print("Error enter valid numbers only")
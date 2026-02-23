try:
    #Get input from users
    year = int(input("Enter a year:"))

    #It should be valid year
    if year <= 0:
        print("Error Please enter a valid year greater than 0")

    else:
        # Check Leap Year Rules-
        #Divisible by 400 then it is always a Leap Year
        if year % 400 == 0:
            is_leap_year =True
            reason="Divisible by 400"

        #IF Divisible by 100 but NOT 400 then it is NOT a Leap Year
        elif year % 100 == 0:
            is_leap_year =False
            reason= "Divisible by 100 but not by 400"

        # If Divisible by 4 then it is Leap Year
        elif year % 4 == 0:
            is_leap_year=True
            reason ="Divisible by 4"

        # If it is Not divisible by 4 then it is not a Leap Year
        else:
            is_leap_year =False
            reason = "Not divisible by 4"


        print("Leap year checker")
        print("Year:",year)

        if is_leap_year:
            print("Result :Leap Year")
        else:
            print("Reslt: NOT a Leap Year")

        print("Reason:",reason)
    

except ValueError:
    print("Error Please enter a valid number")
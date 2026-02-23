
try:
    #Get input from users
    age= int(input("Enter age:"))
    day=input("Enter day (Monday/Tuesday/Wednesday/Thursday/Friday/Saturday/Sunday):")
    num_tickets =int(input("Enter number of tickets:"))

    #Checking Valid Inputs
    if age < 0:
        print("Error age cannot be negative")

    elif num_tickets <= 0:
        print("Errornumber of tickets must be greater than 0")

    elif day !="Monday" and day !="Tuesday" and day !="Wednesday" and day !="Thursday" and day !="Friday" and day !="Saturday" and day !="Sunday":
        print("Error enter a valid day exactly as shown")

    else:
        #Age Based Pricing

        if age < 3:
            base_price = 0
            category ="Free(Below 3)"

        elif age <= 12:
            base_price = 150
            category = "Child(3-12)"

        elif age <= 59:
            base_price = 300
            category ="Adult(13-59)"

        else:
            base_price = 200
            category="Senior(60+)"

        #Day Based discount

        if day =="Friday" or day =="Saturday" or day =="Sunday":
            discount_percent =20
        else:
            discount_percent=0

        #Discount amount per ticket
        discount_amount = base_price *discount_percent/100

        #Price after discount per ticket
        price_after_discount=base_price -discount_amount

        #Total amount for all tickets
        total_amount= price_after_discount * num_tickets

        #Display Results
        print("Ticket pricing")
        print("Age Category :", category)
        print("Day :", day)
        print("Number of Tickets:", num_tickets)
        print("Base Price  :Rs",base_price,"per ticket")

        if discount_percent > 0:
            print("Discount:", discount_percent, "% = Rs", discount_amount, "per ticket")
        else:
            print("Discount:No discount")

        print("Price per Ticket :Rs",price_after_discount)
        print("Total Amount : Rs",total_amount)


except ValueError:
    print("Error enter valid numbers for age and tickets")
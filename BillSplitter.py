# Bill Splitter
try:
    # ----------- Get Input from User -----------
    total_bill=float(input("Enter total bill: "))
    num_people=int(input("Number of people: "))
    tax_percentage=float(input("Tax percentage: "))
    tip_percentage=float(input("Tip percentage: "))

    # Check Invalid Inputs
    if total_bill<= 0:
        print("Error Bill amount must be greater than 0")

    elif num_people<= 0:
        print("Error Number of people must be greater than 0")

    elif tax_percentage< 0:
        print("Error Tax percentage cannot be negative")

    elif tip_percentage< 0:
        print("Error Tip percentage cannot be negative")

    else:
        #Subtotal is the original bill amount
        subtotal=total_bill

        #Tax amount=bill* tax percentage/100
        tax_amount=total_bill*tax_percentage/100

        #Bill after adding tax
        bill_after_tax=total_bill+tax_amount

        #Tipamount=bill aftertax*tip percentage / 100
        tip_amount=bill_after_tax*tip_percentage/100

        #Total bill = bill after tax+tip
        total =bill_after_tax+tip_amount

        #Amount each person has to pay
        per_person=total/num_people

        #Display Results
        print("Bill")
        print(f"Subtotal:₹{subtotal:.2f}")
        print(f"Tax({tax_percentage}%):₹{tax_amount:.2f}")
        print(f"After Tax:₹{bill_after_tax:.2f}")
        print(f"Tip({tip_percentage}%):₹{tip_amount:.2f}")
        print(f"Total:₹{total:.2f}")
        print(f"Per Person:₹{per_person:.2f}")

except ValueError:
    print("Error: Please enter valid numbers only!")
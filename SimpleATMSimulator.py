balance = 10000 #let balance  present in ATm be Rs 10000
minimum_balance = 500 # Minimum balance that should remain in the atm
while True:
    print("\nAtm Simulator")
    print("1.Check Balance")
    print("2.Deposit money")
    print("3.Withdraw money")
    print("4.Exit")

    try:
        choice = int(input("Enter choice:"))

        #1.Check Balance
        if choice == 1:
            print("Your current balance is:Rs", balance)

        #2.Deposit Money
        elif choice == 2:

            deposit_amount = float(input("Enter amount to deposit:"))

            # Check if deposit amount is valid
            if deposit_amount <= 0:
                print("Error deposit amount must be greater than 0")
            else:
                # Add deposit amount to balance
                balance = balance + deposit_amount
                print("Deposit successful")
                print("New balance: Rs.",balance)

        #3: Withdraw Money
        elif choice == 3:

            withdraw_amount = float(input("Enter amount to withdraw: "))

            # Check if withdraw amount is valid
            if withdraw_amount <= 0:
                print("Error Withdrawal amount must be greater than 0!")

            # Check if enough balance is available
            # Balance after withdrawal must be at least Rs. 500
            elif balance - withdraw_amount < minimum_balance:
                print("Error: Insufficient balance!")
                print("Minimum balance of Rs.",minimum_balance,"must remain at all times.")
                print("Maximum you can withdraw:Rs.",balance -minimum_balance)

            else:
                # Subtract withdraw amount from balance
                balance = balance - withdraw_amount
                print("Withdrawal successful!")
                print("New balance: Rs.", balance)

        #4.Exit 
        elif choice == 4:
            print("Thank you for using ATM")
            break 

        #Invalid choice
        else:
            print("Errorenter a valid choice between 1 and 4")

    except ValueError:
        print("Error enter a valid number")
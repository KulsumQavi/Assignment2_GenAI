try:
    #Get Input from User
    number = int(input("Enter number:"))
    range_end = int(input("Enter range (end):"))

    # Valid Inputs
    if range_end <= 0:
        print("Error Range should be greater than 0")

    else:
        #Printing multiplication Table 
        print("Multiplication table of",number)

        #Loop from 1 to range_end
        for i in range(1, range_end + 1):
            result = number * i
            print(number, "x", i,"=",result)

        print("\n--- BONUS: Full Multiplication Table (1-10) ---\n")

        # Print top header row (1 to 10)
        print("    |", end=" ")
        for i in range(1, 11):
            print(f"{i:4}", end=" ")
        print()

        # Print separator line
        print("-----" + "-----" * 10)

        # Outer loop for each row (1 to 10)
        for i in range(1, 11):

            # Print row header (left side number)
            print(f"{i:3} |", end=" ")

            # Inner loop for each column (1 to 10)
            for j in range(1, 11):
                result = i * j
                print(f"{result:4}", end=" ")

            # Move to next line after each row
            print()
except ValueError:
    print("Error Please enter valid numbers")
try:
   
    print("Choose the pattern ")
    print("1.Increasing Row Pattern")
    print("2.Same Number Pattern")
    print("3.Decreasing Row Pattern")
    print("4.Pyramid Pattern")
   
    choice = int(input("Enter pattern choice (1-4):"))
    height = int(input("Enter height of pattern:"))

    #Check Valid Input
    if choice < 1 or choice > 4:
        print("Error enter a valid choice between 1 and 4")

    elif height <= 0:
        print("Error Height must be greater than 0!")

    else:
        # Pattern 1:
        # 1
        # 1 2
        # 1 2 3
        # 1 2 3 4
        # 1 2 3 4 5

        if choice == 1:
            for i in range(1, height + 1):
                # j prints numbers from 1 to current row
                for j in range(1, i + 1):
                    print(j,end=" ")
                print()    # Move to next line after each row
        # Pattern 2:
        # 1
        # 2 2
        # 3 3 3
        # 4 4 4 4
        # 5 5 5 5 5
        elif choice == 2:
            # i controls the no of row
            for i in range(1, height + 1):
                # j prints the row number i, i times
                for j in range(1, i + 1):
                    print(i,end=" ")
                print()  # Move to next line after each row
        # Pattern 3:
        # 5 4 3 2 1
        # 4 3 2 1
        # 3 2 1
        # 2 1
        # 1

        elif choice == 3:
            # i starts from height and goes down to 1
            for i in range(height, 0, -1):
                # j prints numbers from i down to 1
                for j in range(i, 0, -1):
                    print(j, end=" ")
                print()    # Move to next line after each row

        # Pattern 4:
        # 1
        # 121
        # 12321
        # 1234321
        # 123454321
        elif choice == 4:
            # i controls the row number
            for i in range(1, height + 1):
                # j prints numbers from 1 up to i
                for j in range(1, i + 1):
                    print(j, end="")
                # j prints numbers from i-1 back down to 1
                for j in range(i - 1, 0, -1):
                    print(j, end="")
                print()    # Move to next line after each row

except ValueError:
    print("Error enter valid numbers")
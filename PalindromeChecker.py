try:
    #Get Input from User
    user_input = input("Enter word/number: ")

    if user_input == "":
        print("Error enter a word or number!")

    else:
        #Convert to Lowercase for comparison
        original_lower = user_input.lower()

        # Reversing the Input
        # [::-1] reverses the string
        reversed_input = user_input[::-1]
        reversed_lower = original_lower[::-1]

        #Check if Palindrome
        #Compare lowercase original with lowercase reversed
        if original_lower == reversed_lower:
            result = "PALINDROME"
        else:
            result = "NOT a Palindrome"

        print("Original:", user_input)
        print("Reversed:",reversed_input)
        print("Comparing:",original_lower, "==", reversed_lower)
        print("Result:",result)


except Exception:
    print("Error Enter one more time")
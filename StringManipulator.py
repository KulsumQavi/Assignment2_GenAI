try:
    # Get User Input
    sentence = input("Enter a sentence: ")

    # Checking if input is empty
    if sentence == "":
        print("Error: Please enter a valid sentence!")

    else:
        # Original sentence
        original = sentence

        # Total characters including spaces
        char_count_with_spaces = len(sentence)

        # Total characters without spaces
        # Count only non-space characters using loop
        char_count_without_spaces = 0
        for letter in sentence:
            if letter != " ":
                char_count_without_spaces = char_count_without_spaces + 1

        # Total words
        words_list = sentence.split()
        total_words =len(words_list)

        #Convert to uppercase
        uppercase_sentence = sentence.upper()

        #Convert to lowercase
        lowercase_sentence = sentence.lower()

        #Title case
        title_case_sentence = sentence.title()
        # First word
        first_word = words_list[0]

        #Last word
        last_word = words_list[-1]

        #Reverse sentence using loop
        reversed_sentence = ""
        for i in range(len(sentence) - 1, -1, -1):
            reversed_sentence = reversed_sentence + sentence[i]

        # Display Results
        print("Original :", original)
        print("Characters (with spaces):", char_count_with_spaces)
        print("Characters (without spaces):", char_count_without_spaces)
        print("Words:", total_words)
        print("Uppercase :", uppercase_sentence)
        print("Lowercase:", lowercase_sentence)
        print("Title Case:", title_case_sentence)
        print("First word:", first_word)
        print("Last word", last_word)
        print("Reversed:", reversed_sentence)

except Exception as error:
    print("Error occurred:",error)
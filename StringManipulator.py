# Perform multiple string operations on user sentence
try:
    #Get User Input
    sentence=input("Enter a sentence: ")
    # If user just presses Enter without typing anything
    if not sentence.strip():
        print("Error Please enter a valid sentence not empty")
    else:
        # Original sentence is sentence as entered by the user
        original=sentence

        # Total characters including spaces
        char_count_with_spaces=len(sentence)

        #Total characters excluding spaces
        # replace() is function that removes all spaces and then count remaining characters
        char_count_without_spaces=len(sentence.replace(" ", ""))

        #Total words of sentence
        #split() breaks sentence by space and then  returns a list of words
        words_list=sentence.split()
        total_words=len(words_list)

        # Convert full sentence to uppercase
        uppercase_sentence=sentence.upper()

        #Convert entire sentence to lowercase
        lowercase_sentence=sentence.lower()

        #Title Case..capitalizing first letter of every word of sentence
        title_case_sentence = sentence.title()

        # First word — index 0 of the words list
        first_word = words_list[0]

        #Last word — index -1 means last item in the list
        last_word = words_list[-1]

        #[::-1] reverses the entire string character by character
        reversed_sentence = sentence[::-1]

        #Displaying Results 
        print(f"\nOriginal:{original}")
        print(f"Characters (with spaces):{char_count_with_spaces}")
        print(f"Characters (without spaces): {char_count_without_spaces}")
        print(f"Words:{total_words}")
        print(f"Uppercase:{uppercase_sentence}")
        print(f"lowercase:{lowercase_sentence}")
        print(f"Title Case:{title_case_sentence}")
        print(f"First word:{first_word}")
        print(f"Last word:{last_word}")
        print(f"Reversed:{reversed_sentence}")

#Handling Unexpected Errors
except Exception as error:
    print(f"An unexpected error occurred: {error}")
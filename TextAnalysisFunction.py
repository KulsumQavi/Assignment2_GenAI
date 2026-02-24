#1.Count total words in text
def count_words(text):
    words = text.split()
    return len(words)

#2.Count vowels in text
def count_vowels(text):
    count = 0
    for letter in text:
        if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
            count = count + 1
        elif letter == "A" or letter == "E" or letter == "I" or letter == "O" or letter == "U":
            count = count + 1
    return count

#3: Count consonants in text
def count_consonants(text):
    vowels = "aeiouAEIOU"
    count  = 0
    for letter in text:
        # Letter must be alphabet and not a vowel
        if letter.isalpha() and letter not in vowels:
            count = count + 1
    return count

#4.Reverse the text
def reverse_text(text):
    reversed_text = ""
    for i in range(len(text) - 1, -1, -1):  # Loop from last to first
        reversed_text = reversed_text + text[i]
    return reversed_text

#5: Check if text is palindrome
def is_palindrome(text):
    # Remove spaces and convert to lowercase
    clean_text = ""
    for letter in text:
        if letter != " ":
            clean_text = clean_text + letter.lower()

    # Reverse text
    reversed_clean = ""
    for i in range(len(clean_text) - 1, -1, -1):
        reversed_clean = reversed_clean + clean_text[i]

    if clean_text == reversed_clean:
        return True
    else:
        return False

#6: Remove all vowels from text
def remove_vowels(text):
    vowels ="aeiouAEIOU"
    result = ""
    for letter in text:
        if letter not in vowels:
            result = result + letter
    return result

#7.Count frequency of each word
def word_frequency(text):
    words = text.lower().split()
    frequency = {}

    for word in words:
        if word in frequency:
            frequency[word]=frequency[word] +1
        else:
            frequency[word]=1

    return frequency
#8:Find the longest word
def longest_word(text):
    words= text.split()
    longest = ""

    for word in words:
        if len(word) >len(longest):
            longest = word

    return longest

#Calls all above functions and displays results
def analyze_text(text):

    words= count_words(text)
    vowels= count_vowels(text)
    consonants= count_consonants(text)
    reversed_t= reverse_text(text)
    palindrome= is_palindrome(text)
    no_vowels= remove_vowels(text)
    frequency = word_frequency(text)
    long_word= longest_word(text)

    print("Words :",words)
    print("Vowels:",vowels)
    print("Consonants :",consonants)
    print("Reversed :",reversed_t)

    if palindrome:
        print("Palindrome: Yes")
    else:
        print("Palindrome:No")

    print("Without Vowels:", no_vowels)
    print("Longest Word:", long_word, "("+ str(len(long_word)) + " letters)")

    # Print word frequency
    print("Word Frequency :", end=" ")
    for word in frequency:
        print(word + ":" + str(frequency[word]), end="  ")
    print()


try:
    text = input("Enter text: ")

    if text == "":
        print("Error nter some text!")
    else:
        analyze_text(text)

except Exception as e:
    print("Error",e)
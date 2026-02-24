import random
best_score = 0 #to keep the track \

#asking to play again
while True:
    #random number is picked
    secret_number  = random.randint(1, 100)
    max_attempts   = 7
    attempts_used  = 0
    guessed_right  = False

    print("NUMBER GUESSING GAME")
    print("Number is picked between 1-100")
    print("You have", max_attempts, "attempts. Good Luck!")

    #Game Loop
    while attempts_used < max_attempts:

        attempts_left = max_attempts - attempts_used

        try:
            guess = int(input("Attempts left: " + str(attempts_left) + " | Enter your guess: "))

            #Check Valid Input
            if guess < 1 or guess > 100:
                print("enter a number between 1 and 100")
                continue

            #For valid attempt
            attempts_used = attempts_used + 1

            #if Guess is Correct 
            if guess == secret_number:
                guessed_right = True
                break 

            #Hinting when close within 5 
            difference = secret_number - guess
            if difference < 0:
                difference = difference * -1

            if difference <= 5:
                print("you are extremely close!")

            #Too High or Too Low 
            elif guess > secret_number:
                print("Too High!Try lower.")

            else:
                print("Too Low!Try higher.")

        except ValueError:
            print("Error Please enter a valid number!")

    #Game Over Results
    if guessed_right:
        print("\n Congratulations You guessed it right!")
        print("The number was:", secret_number)
        print("Attempts used :", attempts_used)

        #Updating Best Score
        if best_score == 0 or attempts_used < best_score:
            best_score = attempts_used
            print("New Best Score:",best_score,"attempts!")
        else:
            print("Your Best Score:",best_score,"attempts")

    else:
        print("Game Over! You used all", max_attempts,"attempts.")
        print("The number was:", secret_number)

    #To Play again
    print("Do you want to play again?")
    play_again = input("Enter yes or no: ")

    if play_again =="yes":
        continue
    else:
        print("Thanks for playing Your Best Score was:", best_score, "attempts")
        break
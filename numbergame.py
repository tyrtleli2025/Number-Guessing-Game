import random

def main():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    print("\nPlease select the difficulty level:")
    print("1. Easy (10 chances)")
    print("2. Medium (5 chances)")
    print("3. Hard (3 chances)")

    valid = False
    numChances = 0
    while not valid:
        try: 
            difficultyLevel = int(input("\nEnter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if difficultyLevel == 1:
            numChances = 10
            print("Great! You have selected the 'Easy' difficulty!")
            valid = True
        elif difficultyLevel == 2: 
            numChances = 5
            print("Ok, you have selected the 'Medium' difficulty!")
            valid = True
        elif difficultyLevel == 3:
            numChances = 3
            print("Woah, you have selected the 'Hard' difficulty!")
            valid = True
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

    print("\nLet's start the game!")
    computerNum = random.randint(0,100)

    userGuess = 0
    numGuesses = 0
    while numChances > 0:
        numGuesses+=1
        try:
            userGuess = int(input("\nEnter your guess: "))
        except ValueError:
            print("Please enter a number.")
            continue

        if userGuess < computerNum:
            print(f"Incorrect! The number is greater than {userGuess}")

        elif userGuess > computerNum:
            print(f"Incorrect! The number is less than {userGuess}")
        elif userGuess == computerNum:
            print(f"Congratulations! You got the number in {numGuesses} attempts!")
            break

        numChances -= 1
        

main()
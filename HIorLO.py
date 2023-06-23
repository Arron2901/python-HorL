import random

print("""
Welcome to Higher or Lower. To begin with please enter a random number between 1 and 100!
""")

randomNumber = random.randint(1, 100)
numberOfTries = 1
numberFound = False

while numberFound == False:

    userGuess = input("Enter your guess: ") 
    userGuess = int(userGuess)

    if userGuess == randomNumber:
        print(f"""
Congratulations, you guessed the correct number!

Correct Number: {randomNumber}
Number of tries: {numberOfTries}
        """)
        exit()
    
    if userGuess < randomNumber:
        print("""Higher
        """)
        numberOfTries += 1
    
    if userGuess > randomNumber:
        print("""Lower
        """)
        numberOfTries += 1
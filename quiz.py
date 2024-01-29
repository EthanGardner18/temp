import random
print("LETS PLAY THE QUIZ GAME!")

guess = (int)(input("Guess a number 1 though 100: "))

if (guess == random.randint(1,10)):
    print("You guessed Correctly!")
else:
    print("You were incorrect loser")

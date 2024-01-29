import random
print("LETS PLAY THE QUIZ GAME!")

<<<<<<< HEAD
guess = (int)(input("Guess a number 1 though 500: "))
=======
guess = (int)(input("Guess a number 1 though 12: "))
>>>>>>> 979ec2a812f8d83b090d83e202766709b6a5e3c5

if (guess == random.randint(1,10)):
    print("You guessed Correctly!")
else:
    print("You were incorrect loser")

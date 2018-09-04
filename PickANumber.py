import random
import math
import string

def randomGen(range):
    i = random.randint(1,(range))
    return(i)

def kenProofInput(out , ch):
    while True:
        if ch == "int":
            try:
                x = int(input(out))
                return x
            except ValueError:
                print("Not a valid input, please try again")

        elif ch == "str":
            try:
                x = str(input(out))
                return x
            except ValueError:
                print("Not a valid input, please try again")

        elif ch == "float":
            try:
                x = float(input(out))
                return x
            except ValueError:
                print("Not a valid input, please try again")


if __name__ == '__main__':
    x = True
    while x:
        print("Welcome to the Random Number Picker.\nIn order to play, try guessing the number the computer is thinking")
        level = 2 ** kenProofInput("Choose any natural number to pick a level to play: ", "int")
        print (level)
        print("You have chosen a level in which the range of numbers is from 1 to {}.".format(level))
        num = randomGen(level)

        guess = False
        count = 0
        while guess == False:
            g = kenProofInput("Guess: " , "int")
            if g == num:
                count += 1
                print("Congratulations, you guessed the number {} in {} tries".format(num , count))
                guess = True
            if g > num:
                print("GO  LOWER")
                count += 1
            if g < num:
                print("GO  HIGHER")
                count += 1

        again = kenProofInput("Would you like to play again? Y/N ", "char")
        if again.lower() != "y":
            break

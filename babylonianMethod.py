# WSQ10
#In this assignment you will write a function to calculate
# the square root of a number using the Babylonian method. You can
# search for that method, it will be easy to find. The function should
# receive a number and return floating point number. Obviously you should
# test your function, so create a main program that asks the user a value,
# calculates the square root and displays that.

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

def bablylonianM(num, lev):
    guess = 0
    while (guess * guess) < num:
        guess += 1

    for x in range(0,lev):
        guess = (guess + (num/guess))*0.5

    return guess

if __name__ == '__main__':
    num = kenProofInput("Please enter the number: ","int")
    lev = kenProofInput("Please enter a level of precision: ","int")
    if lev == 0:
        lev = 1
    elif lev < 0:
        lev *= -1

    result = bablylonianM(num, lev)

    print("The approximation of the square root of {} is {}".format(num, result))

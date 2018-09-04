#Code by: rghost        Academic Purposes   \#WSQ04

#This code is to do the following:
# Write a program that asks for a range of integers and then prints the sum of
# the numbers in that range (inclusive).

#You can use a formula to calculate this of course but what we want you to do
#here is practice using a loop to do repetitive work.
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

def sumInRange(high , low):
    x = 0
    while high != low-1 :
        # print(high)
        x += high
        high -= 1
        # print(x)
    return x

if __name__ == '__main__':

    x = kenProofInput("Enter the higher range: ", "int")
    y = kenProofInput("Enter the lower range: ", "int")
    if y > x:
        print("You entered a Lower Range that's higher than your Higher Range")
        inv = kenProofInput("Would you like to invert the ranges? ", "str")
        if inv == "y":
            z = y
            y = x
            x = z
    if x > y:
        print("The sum from {} to {} = {} ".format( y, x, sumInRange(x , y)))

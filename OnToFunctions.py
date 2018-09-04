#Code by: rghost        Academic Purposes   #WSQ05

#This code is to do the following:

# You will go back and do WSQ01 – Fun with Numbers again.
# But this time, write a function for each calculation.
# Each function should define two parameters (in this example of type int)
# and return the correct value as an integer as well.
# You main program needs to ask the user for the input and then call each
# function to calculate the answer for each of the parts.
def add(x,y):
    return x + y

def subs(x,y):
    return x - y

def mult(x,y):
    return x * y

def div(x,y):
    z = int(x) / int(y)
    return z

def remain(x,y):
    return x % y

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

    print("You will be asked to enter two integers\n")
    x = kenProofInput("Enter Integer 1: ","int")
    y = kenProofInput("Enter Integer 2: ","int")

    print("{} + {} = {}".format(x , y , add(x,y))) #   The sum of the two numbers.
    print("{} - {} = {}".format(x , y , subs(x,y))) #   The difference of the two numbers.
    print("{} * {} = {}".format(x , y , mult(x,y))) #   The product of the two numbers.
    print("{0:0} / {1:0} = {2:0.0f}".format(x , y , div(x,y))) #   The integer based division of the two numbers (so no decimal point). First divided by second.
    print("{} % {} = {}".format(x , y , remain(x,y))) #   The remainder of integer division of the two numbers.

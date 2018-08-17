#Code by: rghost        Academic Purposes 

#This code is to do the following:
# Ask the user for two integer values, then use those two values to calculate and show the following:
#   The sum of the two numbers.
#   The difference of the two numbers.
#   The product of the two numbers.
#   The integer based division of the two numbers (so no decimal point). First divided by second.
#   The remainder of integer division of the two numbers.


if __name__ == '__main__':

    print("You will be asked to enter to integers\n")
    x = int(input("Enter Integer 1: "))
    y = int(input("Enter Integer 2: "))

    print(str(x) + " + " + str(y) + " = " + str(x + y)) #   The sum of the two numbers.
    print(str(x) + " - " + str(y) + " = " + str(x - y)) #   The difference of the two numbers.
    print(str(x) + " * " + str(y) + " = " + str(x * y)) #   The product of the two numbers.
    print(str(x) + " / " + str(y) + " = " + str(int(x / y))) #   The integer based division of the two numbers (so no decimal point). First divided by second.
    print(str(x) + " % " + str(y) + " = " + str(x % y)) #   The remainder of integer division of the two numbers.

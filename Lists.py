# WSQ07
#This code is to do the following:
# Create a program that asks the user for 10 numbers  (floating point).
# Store those numbers in a list. Show to the user the total, average and
# standard deviation of those numbers.
from math import sqrt

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

def sumOfList(array):
    sum = 0
    for actualNum in array:
        sum += actualNum
    return sum

def mean(array):
    return sumOfList(array)/len(array)

def stndDeviation(array):
    var = 0
    for x in array:
        num = (x - mean(array))**2
        var += num

    var = var / (len(array)-1.0)
    return sqrt(var)
if __name__ == '__main__':
    print("Welcome to the List program")

    while True:
        x = 1
        list = []
        for x in range(1,11):
            list.append(kenProofInput("Please enter your {} number: ".format(x),"float"))
        print("\nThis is your list: " + str(list))
        print("The sum of your list is: " + str(sumOfList(list)))
        print("The average of your list is: " + str(mean(list)))
        print("The Standard deviation of your list is: " + str(stndDeviation(list)))

        cont = kenProofInput("\nWould you like to enter another list? y/any key","str")

        if cont != "y":
            break

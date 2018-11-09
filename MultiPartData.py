#Code by: rghost        Academic Purposes   \#WSQ09

#This code is to do the following:
# So for this assignment I would like to see you create a
# function that receives as parameter the name of a file (this
# would be a string value like data.txt) and your function counts
# the number of lines and the number of characters in the file
# which it returns as a single value (but with two values). You
#  will want to look at how to use and return a tuple from a function
#  and how to open and read text files line by line.

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
def parser(fileName):
    while True:
        try:

            with open(fileName) as f:
                text = f.read()
                break
        except FileNotFoundError:
            return "File Not Found"
    nLineChar = [0,0]
    for x in text:
        if x == "\n":
            nLineChar[0] += 1
        elif x != " ":
            nLineChar[1] += 1
    return nLineChar

if __name__ == '__main__':
    file = kenProofInput("Enter the name of the file with .txt: ", "str")
    t = parser(file)
    print("This file has {} lines and {} characters".format(t[0],t[1]))

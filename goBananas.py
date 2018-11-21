#WSQ11

# Write a function called find_bananas which receives a single parameter called
# filename (a string) and returns a positive integer which is the number of times
# the word (string) “banana”  (or “BANANA” ) is found in the file. The banana can
# be any case (‘BaNana’ or ‘BANANA’ or ‘banana’, etc) and they can be “stuck
# together” like “banAnaBANANA” (that counts as two). Create your own test file
# (plain text) to check your work.

def find_bananas(filename):
    try:
        with open(filename) as fobj:
            text = fobj.read()

    except FileNotFoundError:
        print("Text file does not exist")
        text= ""

    text = text.lower().replace(' ','').split("banana")

    return len(text)-1

if __name__ == '__main__':
    file = input("Enter file name: ")
    print("This file has ", find_bananas(file)," bananas.")

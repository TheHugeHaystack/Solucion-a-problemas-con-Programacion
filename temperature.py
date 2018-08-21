#Code by: rghost        Academic Purposes

#This code is to do the following:
# Write a program that will prompt the user for a temperature asking the user between Fahrenheit and Celsius;
# then, convert it to the other. You may recall that the formula is C = 5 ∗ (F − 32)/9.
# Modify the program to state whether or not water would boil at the temperature given.
import string
if __name__ == '__main__':
    c = True;
    while c:
        t=0;
        opt = input("Please enter if you would like to convert from Celsius or Fahrenheit to the other (C/F): ");
        if opt.lower() == "c":
            t = input("Enter your temperature in Celsius ");
            print("A temperature of " + str(t) + " degrees Celsius is "+ str(float(t)*(9/5)+32) +" in Fahrenheit");
            if float(t)*(9/5)+32 >= 100:
                print ("Water boils at this temperature (under typical conditions).")
            else:
                print("Water does not boil at this temperature (under typical conditions).")

        elif opt == "f":
            t = input("Enter your temperature in Fahrenheit ");
            print("A temperature of " + str(t) + " degrees Fahrenheit is "+ str((float(t)-32)*5/9) +" in Celsius");
            if (float(t)-32)*5/9 >= 212:
                print ("Water boils at this temperature (under typical conditions).")
            else:
                print("Water does not boil at this temperature (under typical conditions).")

        else:
            print("Not a valid answer");


        a = input("Would you like to enter another temperature? Y/AnyKey* ")
        if a.lower() != "y":
            break;

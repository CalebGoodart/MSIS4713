#!python3
import math
import sys


def recusivefact(x):  # The recursive version for fun :P
    if x == 1:
        return 1
    elif x == 0:
        return 1
    return x * recusivefact(x-1)


def fact(x):  # The iterated version of factorial
    total = 1
    for i in range(1, x+1):
        total *= i
    return total


def mathsfact(x):  # The Math.factorial version
    return math.factorial(x)


while(True):
    num = int(input("Input an Integer (not too big) greater than 1: "))

    if num > 20:
        print("Lets not break the processor, try again")
    elif num > 100:
        print("Seriously, this number is too big!  Exiting now.")
        sys.exit()
    else:
        temp1 = fact(num)
        temp2 = mathsfact(num)
        status = temp1 == temp2
        print(recusivefact(num))
        print("Looping gives a value of " + str(temp1))
        print("The factorial function returns a value of " + str(temp2))
        print("Do the two methods result in the same value? " + str(status))




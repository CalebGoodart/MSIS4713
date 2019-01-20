#! python3

# Program by Caleb Goodart
# MSIS4713
# Mod01

import sys
from random import randint

print("Welcome to the soda machine. This machine take 5, 10 and 25 cent coins")
soda = input("What soda would you like?  ")
PRICE = randint(-3, 3)*5 + 100  # price veering by 5,10,15 above or below 100
print("The price is " + str(PRICE))

while True:  # checks for the two cases and subtracts the entered coin value from price
    print("You owe " + str(PRICE))
    PRICE -= int(input("insert coin: "))
    if PRICE == 0:  # case for exact change
        print("Enjoy your soda")
        sys.exit()
    elif PRICE < 0:  # case for change
        print(str(abs(PRICE)) + " cents is your change, Enjoy your soda")
        sys.exit()

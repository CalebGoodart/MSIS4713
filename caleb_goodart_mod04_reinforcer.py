#! python3

# Program by Caleb Goodart
# MSIS4713
# Mod04 reinforcer


from random import randint
import sys

source_string = " ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 abcdefghijklmnopqrstuvwxyz @%+\/'!#$^?:,(){}[]~`-_. "


def make_password(length):

    space_in_password = 0
    caps_nexted = 0
    caps_min = 0
    nums_nexted = 0
    nums_min = 0
    sp_nexted = 0
    sp_min = 0

    while True:
        new_password = ""

        for i in range(length):
            new_password = new_password + source_string[randint(0, len(source_string) - 1)]

        error = test_password(new_password)

        if error == 0:

            print("Good password generated!\n")
            print(new_password.center(28))
            print("\nFailure Causes:\n")
            print("Spaces in password: ".rjust(28) + str(space_in_password))
            print("Two capital letters next to each other: ".rjust(48) + str(caps_nexted))
            print("Two number next to each other: ".rjust(39) + str(nums_nexted))
            print("Two special characters next to each other: ".rjust(51) + str(sp_nexted))
            print("Less than two capital letters: ".rjust(39) + str(caps_min))
            print("Less than two number: ".rjust(30) + str(nums_min))
            print("Less than two special characters: ".rjust(42) + str(sp_min))
            total_errors = sp_min + sp_nexted + nums_min + nums_nexted + caps_min + caps_nexted + space_in_password
            print("\nTotal Number of Failures: " + str(total_errors))
            return total_errors

        elif error == 1:
            space_in_password += 1
        elif error == 2:
            caps_nexted += 1
        elif error == 3:
            caps_min += 1
        elif error == 4:
            nums_nexted += 1
        elif error == 5:
            nums_min += 1
        elif error == 6:
            sp_nexted += 1
        elif error == 7:
            sp_min += 1


def test_password(password):

    if " " in password:
        return 1

    # Checks for 3 sets of cases for Caps Numbers and Special chars and returns a unique return value
    for i in range(len(password) - 1):
        min_count = 0
        # test for Capitals next to each other and the number of caps
        if password[i] in source_string[1:28]:
            min_count += 1
            if password[i+1] in source_string[1:28]:
                return 2

        if min_count > 2:
            return 3

        min_count = 0

        # check for numbers next to each other and number of numbers
        if password[i] in source_string[28:39]:
            min_count += 1
            if password[i+1] in source_string[28:39]:
                return 4

        if min_count > 2:
            return 5

        min_count = 0

        # checks for specials together and their number
        if password[i] in source_string[65:90]:
            min_count += 1
            if password[i + 1] in source_string[65:90]:
                return 6

        if min_count > 2:
            return 7

    return 0


while True:

    pass_length = 12 # int(input("Enter a password length: "))

    if pass_length < 12:
        print("password needs to be longer!")
    elif pass_length > 20:
        print("password is too long!")
    else:
        make_password(pass_length)
        sys.exit()


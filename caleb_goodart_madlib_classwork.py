#! python3

# Program by Caleb Goodart
# MSIS4713
# madlib


def madlib(person, num, obj, animal, emotion):
    print("One day " + person +
          " went to the store and bought " + num +
          " " + obj + ".\n" +
          person + " fed these to the" + animal +
          ", which made it very " + emotion + ".\n")


while True:
    print("Let's play a quick round of madlibs. I need some information from you.")
    madlib(
        input("\nA person's name: "),
        input("A whole number, like 3 or 15 or something: "),
        input("Some objects (more than one) like pencils or cabbages or something: "),
        input("A type of animal: "),
        input("An emotion: "))

    temp = input("Press Y to play again: ")
    if temp == "Y" or temp == "y":
        continue
    else:
        break


#! python3

# Program by Caleb Goodart
# MSIS4713
# Mod03


from random import randint

list_of_ten = []
print("Create a list filled with some words and some numbers.\n")

for i in range(10):
    list_of_ten[i] = input("Please enter a number or a word: ")

print("This list has 10 items.")
if len(list_of_ten) == 10:
    print("True")
else:
    print("False")

print("\nThis is the list")
print(list_of_ten)

# swaps the first and tenth index data
swap = list_of_ten[0]
list_of_ten[0] = list_of_ten[9]
list_of_ten[9] = swap
del swap

print("\nThis is the list after swapping the first and last items")
print(list_of_ten)

print("\nThese are the first three and last three items in the list:")
print(str(list_of_ten[0:3]) + " " + str(list_of_ten[7:10]))
print("\nThese are the individual items in they list")

for i in range(len(list_of_ten)):
    print(list_of_ten[i])

if "cat" in list_of_ten:
    print("There is cat is in the list")
else:
    print("There is no cat in this list")

marvel_char = input("\nPlease insert the name of a Marvel character ")
index = randint(0, 9)
print("\n" + marvel_char + " is at index " + str(index))
list_of_ten.insert(index, marvel_char)

ints_list = []
# User try catch block to filter the ints out
for k in range(len(list_of_ten)):
    try:
        ints_list.append(int(list_of_ten[k]))

    except ValueError:
        continue

print("\nThese are the integers from the list\n")
print(ints_list)

list_of_ten = tuple(list_of_ten)
print("This is the tuple of the list\n")
print(list_of_ten)

try:
    list_of_ten[0] = "cat"
except TypeError:
    print("Tuples are immutable!")

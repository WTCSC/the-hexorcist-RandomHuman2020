import functs
from os import environ
import platform
import string

# Microsoft uses a different variable for the user's username than Linux or macOS, this is needed to make it work correctly cross-platform.
if platform.system() == "Linux" or platform.system() == "Darwin":
    username = environ.get("USER")
elif platform.system() == "Windows":
    username = environ.get("USERNAME")

print(f"Welcome to the Hexorcist, {username}.")

# This while loop allows the script to continue asking for the same input until the user inputs a valid number. The same description applies to the following two loops.
good_input = False
while not good_input:
    in_num = input("Enter the number you wish to convert.\n> ")
    if any(char in string.punctuation for char in in_num):
        good_input = False
        print("The Hexorcist does not understand these 'symbols'.")
    else:
        good_input = True

good_base_in = False
while not good_base_in:
    in_base = input("Enter this number's current base. (This falls between 2 and 36.)\n> ")

    try:
        in_base_int = int(in_base)
        if in_base_int <= 36:
            good_base_in = True
        else:
            print("That base is outside of the Hexorcist's range.")
            good_base_in = False
    except ValueError:
        print("That's not a valid base. Try again.")
        good_base_in = False

good_base_out = False
while not good_base_out:
    out_base = input("Enter the base you wish to convert this number into. (This falls between 2 and 36.)\n> ")

    try:
        out_base_int = int(out_base)
        if out_base_int <= 36:
            good_base_out = True
        else:
            print("That base is outside of the Hexorcist's range.")
            good_base_out = False
    except ValueError:
        print("That's not a valid base. Try again.")
        good_base_out = False


print("Throwing rocks at the wall to see what numbers come out...")

num_in_decimal = functs.to_decimal(in_num, in_base_int)

num_in_final = functs.from_decimal(num_in_decimal, out_base_int)

print(f"{num_in_decimal} (Base-{in_base_int}) is {num_in_final} (Base-{out_base_int})")
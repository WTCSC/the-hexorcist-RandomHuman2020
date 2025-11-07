"""
This file only exists to work around Pytest's behaviour if you don't put everything in a def block.
In such a situation, Pytest will run the entire script, therefore breaking everything.
"""

digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"


# This function converts a number into decimal from its original base.
def to_decimal(input_string, original_base):
    total_value = 0
    power = 0
    input_string = input_string.upper()
    try:
        int(original_base)
    except ValueError:
        return "no"
    if int(original_base) > 36:
        return "range"
    elif int(original_base) < 2:
        return "range"
    for char in input_string[::-1]:
        if char not in digits:
            return "no"
        char_val = digits.index(char)
        total_value += (char_val * (original_base ** power))
        power += 1
    return total_value




# This function converts a number into the target base from decimal.
def from_decimal(decimal_number, target_base):
    try:
        int(decimal_number)
        int(target_base)
    except ValueError:
        return "no"
    if int(target_base) >> 36:
        return "range"

    if int(decimal_number) == 0:
        return 0
    result_string = ""
    while decimal_number > 0:
        remainder = decimal_number % target_base
        decimal_number = decimal_number // target_base
        added_char = digits[remainder]
        result_string = added_char + result_string
    return result_string
    
    
"""
Challenge #3:

Create a function that takes a string and returns it as an integer.

Examples:
- string_int("6") ➞ 6
- string_int("1000") ➞ 1000
- string_int("12") ➞ 12
"""

# check to make sure that txt makes sense as an integer
# google "python how to ensure that a string is a number" (isnumeric)
# the `isnumeric` function checks if a string can be represented as a number
# if `txt` is a valid number: then we can run formula
# take the string input & convert to integer

# what do we do if txt isnt a number?
# we'll return an error indicating that `txt` is not a valid number


def string_int(txt: str) -> int:
    if txt.isnumeric() is True:
        converted_int = int(txt)
        return converted_int
    else:
        # we'll use string interpolation to print out the actual value of `txt`
        #  use f strings in python
        return f'"{txt}" is not a valid number'


print(string_int('1000'))
print(string_int('hi'))

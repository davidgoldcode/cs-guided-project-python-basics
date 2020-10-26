"""
Challenge #6:

Create a function that takes a string, checks if it has the same number of "x"s
and "o"s and returns either True or False.

- Return a boolean value (True or False).
- The string can contain any character.
- When no x and no o are in the string, return True.

Examples:
- XO("ooxx") ➞ True
- XO("xooxx") ➞ False
- XO("ooxXm") ➞ True (Case insensitive)
- XO("zpzpzpp") ➞ True (Returns True if no x and o)
- XO("zzoo") ➞ False
"""

# how do we keep track of number of 'x's & 'o's
# let's just keep two variables - one that tracks # of 'x's & 'o's
# figure out the # of 'o's & 'x's in the input string
# check fi the number is the same
# return true if same, false otherwise


def XO(txt: str) -> bool:
    xs = 0
    os = 0
    # we will iterate over txt
    for character in txt:
        if character.lower() == 'o':
            os += 1
        elif character.lower() == 'x':
            xs += 1
        else:
            None
    return xs == os


# def XO(txt: str) -> bool:
#     xs = 0
#     os = 0
#     # we will iterate over txt
#     for character in txt:
#         if character == 'o' or character == 'O':
#             os += 1
#         elif character == 'x' or character == 'X':
#             xs += 1
#         else:
#             None
#     return xs == os


# def XO(txt: str) -> bool:
#     txt = txt.lower()
#     return txt.count('o') == txt.count('x')
#     # Your code here

print(XO("ooxx"))
print(XO("xooxx"))
print(XO("ooxXm"))
print(XO("zpzpzpp"))
print(XO("zzoo"))

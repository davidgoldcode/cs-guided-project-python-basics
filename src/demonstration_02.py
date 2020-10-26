"""
Challenge #2:

Write a function that takes an integer `minutes` and converts it to seconds.

Examples:
- convert(5) ➞ 300
- convert(3) ➞ 180
- convert(2) ➞ 120
"""

# there are 60 seconds in a minute
# we need to take `minutes` & multipy by 60 in order to convert
# return the converted result


def convert(minutes: int) -> int:
    return minutes * 60

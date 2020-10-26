"""
Challenge #5:

Create a function that returns a list of strings sorted by length in ascending
order.

Examples:
- sort_by_length(["a", "ccc", "dddd", "bb"]) ➞ ["a", "bb", "ccc", "dddd"]
- sort_by_length(["apple", "pie", "shortcake"]) ➞ ["pie", "apple", "shortcake"]
- sort_by_length(["may", "april", "september", "august"]) ➞ ["may", "april", "august", "september"]
- sort_by_length([]) ➞ []
"""

# takes a list of strings & sorts themin such a way that
# the shorter strings come first, with the lognest string last
# how do we sort an array/list by the lenght of the elem
# return sorted output
# the `.sort()` method on lists in python sorts in place
# does it by alphabetical order, NOT length


def sort_by_length(lst):
    lst.sort(key=len)
    return lst


print(sort_by_length(["a", "ccc", "dddd", "bb"]))
print(sort_by_length(["apple", "pie", "shortcake"]))
print(sort_by_length(["may", "april", "september", "august"]))
print(sort_by_length([]))

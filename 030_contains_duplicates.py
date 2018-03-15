"""
Given an array of integers, find if the array contains any duplicates.
Your function should return true if any value appears at least twice in the array,
and it should return false if every element is distinct.

Eg.: [1, 2, 3, 4, 2, 1] -> True
Eg.: [1, 2, 3, 4] -> False
Eg.: [] -> False

dictionary = {
    1: 1,
    2: 1, etc.
    When 3: 1+1 return True
}

"""

def contains_duplicates(given_array):
    counter = {}
    for item in given_array:
        if item in counter:
            return True
        else:
            counter[item] = 1
    return False

assert contains_duplicates([1, 2, 3, 4, 2, 1]) == True
assert contains_duplicates([1, 2, 3, 4]) == False
assert contains_duplicates([]) == False

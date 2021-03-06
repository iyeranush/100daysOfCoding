"""
Given a sorted array, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example:

    Given nums = [1,1,2],

    Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
    It doesn't matter what you leave beyond the new length.
"""

def remove_duplicates(given_array):
    prev = None
    new_length = 0
    for i in given_array:
        if prev != i:
            new_length += 1
        prev = i
    return new_length

assert remove_duplicates([1, 1, 2]) == 2
assert remove_duplicates([1, 2, 2, 3, 4, 4]) == 4
assert remove_duplicates([]) == 0

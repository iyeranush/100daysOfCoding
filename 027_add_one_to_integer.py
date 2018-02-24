"""
Given an array of integers which represents an integer, add one to the integer
And return the final value.
Eg. [1, 3, 4, 5] represents 1345
Add 1 to it -> 1346
Return [1, 3, 4, 6]

* The elements of the array will be between 0-9
* The  result array could be longer than the given array

Cases:
[1, 3, 4, 5] + 1 -> [1, 3, 4, 6]
[1, 0, 0, 0] + 1 -> [1, 0, 0, 1]
[1, 0, 9, 9] + 1 -> [1, 1, 0, 0]
[9, 9, 9] + 1 -> [1, 0, 0, 0]
"""

def add_one(given_array):
    length = len(given_array)
    result = [0]* length

    i = length-1
    carry = 1
    while i >= 0:
        _sum = given_array[i] + carry
        if _sum == 10:
            carry = 1
        else:
            carry = 0
        result[i] = _sum % 10
        i -= 1
    if carry == 1:
        result = [1] + result
    return result

assert add_one([9, 9, 9]) == [1, 0, 0, 0]
assert add_one([1, 0, 9, 9]) == [1, 1, 0, 0]
assert add_one([1, 3, 4, 5]) == [1, 3, 4, 6]
assert add_one([1, 0, 0, 0]) == [1, 0, 0, 1]

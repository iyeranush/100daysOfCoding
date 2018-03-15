"""
Given k(integer), and and array
find the k most frequent elements in the array
Implementation:
1) create a dictionary of all elements with count of occurence
2) create a new array that has max length of given_array +1
3) now iterate through the dictionary and add it to the new array in the spot that corresponds to the count of key.
Eg. [1, 2, 3, 1, 2, 3, 2, 3] k = 2
returns [2, 3]
key:count = {1:2, 2:3, 3:3}
Max occurence = length number of times. Here, 8.
result_array = [None, None, None, None, None, None, None, None, None]
result_array = [None, None, [1], [2, 3], None, None, None, None, None]
result = [2, 3, 1]
result.first(k) = [2, 3]
"""

def k_most_frequent_elements(given_array, k):
    counter = {}
    for item in given_array:
        if item in counter:
            counter[item] += 1
        else:
            counter[item] = 1

    length_array = len(given_array)
    temp_array = [None]*(length_array + 1)
    for key in counter:
        freq = counter[key]
        if temp_array[freq] == None:
            temp_array[freq] = [key]
        else:
            temp_array[freq].append(key)

    result = []
    for i in range(length_array, 0, -1):
        if temp_array[i]:
            result = result + temp_array[i]
    return result[0:k] if result else None

assert k_most_frequent_elements([1, 2, 3, 1, 2, 3, 2, 3], 2) == [2, 3]
assert k_most_frequent_elements([1, 2, 3, 1, 2, 3, 2, 3], 3) == [2, 3, 1]


"""
Longest consecutive subsequence
Given array [1, 8, 6, 2, 10, 3, 4] => [1, 2, 3, 4] or length of subsequence=4
"""

def longest_consecutive_subsequence(given_array):
    element_lookup = {}
    for item in given_array:
        if item not in element_lookup:
            element_lookup[item] = True
    # 1, 2, 3, 4
    lcs = []
    for key in element_lookup:
        counter = 0
        lcs_temp = []
        if (key - 1) not in element_lookup:
            key_element = key
            while key_element in element_lookup:
                lcs_temp.append(key_element)
                key_element += 1
            if len(lcs_temp) > len(lcs):
                lcs = lcs_temp

    return lcs

assert longest_consecutive_subsequence([3, 2, 1, 4, 8]) == [1, 2, 3, 4]
assert longest_consecutive_subsequence([3, 2, 1, 4, 8, 7, 6, 9, 10]) == [6, 7, 8, 9, 10]


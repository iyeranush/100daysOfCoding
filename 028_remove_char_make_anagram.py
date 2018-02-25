"""
Q: Given two strings (lowercase), how many char do we remove (from either) to make anagram?
Return: number of char
Eg:
string1 = 'hello'
string2 = 'billion'
return: 6 ('he' from first and 'biin' from second)
"""


CHARS = 26
def make_anagram(s1, s2):
    count_char1 = [0]*CHARS
    count_char2 = [0]*CHARS

    for c in s1:
        pos = ord(c) - ord('a')
        count_char1[pos] += 1

    for c in s2:
        pos = ord(c) - ord('a')
        count_char2[pos] += 1

    total_number = 0
    for i in range(0, 26):
        total_number = total_number + abs(count_char1[i] - count_char2[i])
    return total_number

assert make_anagram('hello', 'billion') == 6
assert make_anagram('care', 'are') == 1


"""
Given a string, find th first recurring character

Note:
    The string when empty, return None
    in string : "abcdabcd" -> a ("a" is the first recussing char)
Implementation:
"""

def first_recussing_char(given_string):
    char_tracker = {}
    for c in given_string:
        if c not in char_tracker:
            char_tracker[c] = True
        else:
            return c

assert first_recussing_char("abcdabc") == 'a'
assert first_recussing_char("abcd") == None

"""
Q: Find the longest consequtive character in given string
Eg: AABDDCBBBBCCC -> (B, 4)
Because B occurs 4 times in the string consecutive
"""


def get_longest_consecutive_char(given_string):
    prev = None
    count = 0
    max_char = None
    max_count = 0

    for c in given_string:
        if c == prev:
            count += 1
        if c != prev:
            if count > max_count:
                max_char = prev
                max_count = count
            count = 1
        prev = c
    if not max_count:
        max_char = prev
        max_count = count

    return [max_char, max_count]

assert get_longest_consecutive_char('AABDDCBBBBCCC') == ['B', 4]
assert get_longest_consecutive_char('AAAA') == ['A', 4]
assert get_longest_consecutive_char('AABC') == ['A', 2]

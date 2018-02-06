'''
LEETCODE:
Write a function that takes a string as input and returns the string reversed.
Example:
Given s = "hello", return "olleh".
'''
def reverse_string(s):
    """
    :type s: str
    :rtype: str
    """
    total_len = len(s)
    reversed_string = [None]*total_len
    i = 0
    while i != total_len:
        reversed_string[i] = s[total_len-1-i]
        i += 1
    return "".join(reversed_string)


def main():
    assert reverse_string("hello") == "olleh"

if __name__ == '__main__':
    main()

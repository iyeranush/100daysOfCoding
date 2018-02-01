#!/bin/python

# A left rotation operation on an array of size n shifts each of the array's elements d unit to the left.
# For example, if 2 left rotations are performed on array [1 2 3 4 5],
# then the array would become [3 4 5 1 2].

import sys

def leftRotation(a, d):
    total_length = len(a)

    new_array = [(i-d, item) if i-d >= 0 else (i-d+total_length, item) for i, item in enumerate(a)]
    for item in new_array:
        a[item[0]] = item[1]
    return a

if __name__ == "__main__":
    n, d = raw_input().strip().split(' ')
    n, d = [int(n), int(d)]
    a = map(int, raw_input().strip().split(' '))
    result = leftRotation(a, d)
    print " ".join(map(str, result))

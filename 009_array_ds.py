#!/bin/python3
'''
An array is a type of data structure that stores elements of the same type in a contiguous block of memory.
Given an array, A, of n integers, print each element in reverse order as a single line of space-separated integers.
Sample Input
------------
4
1 4 3 2

Sample Output
-------------
2 3 4 1

'''



import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

arr.reverse()
sys.stdout.write(" ".join([str(num) for num in arr]))
sys.stdout.flush()

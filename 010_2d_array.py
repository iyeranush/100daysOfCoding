#!/bin/python

'''
Calculate the hourglass sum for every hourglass in Input array, then print the maximum hourglass sum.

Given 6*6 2D Array:
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
We define an hourglass in  to be a subset of values with indices falling in this pattern in 's graphical representation:

a b c
  d
e f g
'''

import sys

arr = []
for arr_i in range(6):
    arr_temp = input().strip().split(' ')
    arr_temp = [int(item) for item in arr_temp]
    arr.append(arr_temp)

max_depth = 6 - 2
max_sum = None
for i in range(max_depth):
    for j in range(max_depth):
        hourglass_arr = [arr[i][j], arr[i][j+1], arr[i][j+2], arr[i+1][j+1], arr[i+2][j], arr[i+2][j+1], arr[i+2][j+2]]
        hourglass_sum = sum(hourglass_arr)
        if max_sum is None or (max_sum and max_sum < hourglass_sum):
            max_sum = hourglass_sum

print(max_sum)

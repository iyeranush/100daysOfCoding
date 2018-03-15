"""
Count Negative Integers in Row/Column-Wise Sorted Matrix
1) Iterate through the whole array and count -ve int every time your encounter. O(nm)
2) Start from top right, and as you encounter -ve move down. O(m+n)
"""

def count_negative(given_array):
    n = len(given_array)
    m = len(given_array[0])
    j = m -1
    i = 0

    count = 0
    while (j >= 0 and i < n):
        if given_array[i][j] >= 0:
            j -= 1
        elif given_array[i][j] < 0:
            count += j+1
            i += 1
    return count

arr = [[-3, -2, -1, 1], [-2, 2, 3, 4], [4, 5, 7, 8]]
assert count_negative(arr) == 4

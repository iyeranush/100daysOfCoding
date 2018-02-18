"""
Question: Move all zeroes in array to the end in-place.
Return: Same array
"""

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def push_zeros_to_the_end(arr):
    move_counter = 0
    length = len(arr)
    for i in range(length):
        if arr[i] == 0:
            move_counter += 1
        else:
            swap(arr, i, i-move_counter)

def main():
    arr = [1, 0, 2, 0, 3, 0]
    push_zeros_to_the_end(arr)
    assert arr == [1, 2, 3, 0, 0, 0]

    arr = [0, 0, 0, 1, 2, 3]
    push_zeros_to_the_end(arr)
    assert arr == [1, 2, 3, 0, 0, 0]

if __name__ == '__main__':
    main()

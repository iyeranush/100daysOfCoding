# Given an array [1, 2], find all subsets of the array
# Example solution: {}, {1}, {2}, {1, 2}
# Print in any order
# Print to stdout
# Problem solved with recursion
# O(2^n)

def print_subset(arr):
    print(' '.join([str(item) for item in arr if item is not None]))

def find_subsets(arr):
    subset_arr = [None]*len(arr)
    helper(arr, subset_arr, 0)

def helper(arr, subset_arr, index):
    if index == len(arr):
        print_subset(subset_arr)
    else:
        subset_arr[index] = None
        helper(arr, subset_arr, index+1)
        subset_arr[index] = arr[index]
        helper(arr, subset_arr, index+1)

def main():
    arr = [int(item) for item in input().strip().split(' ')]
    find_subsets(arr)

if __name__ == '__main__':
    main()

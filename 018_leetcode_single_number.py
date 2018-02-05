'''
Given a list of integers, where each number occurs even number of times,
Find that one integer which occurs odd number of times
Assumption:
1. Will all be integers
2. Only one int occurs odd times
'''


def find_single_number(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    integer_counter = {}
    for item in nums:
        if item in integer_counter:
            del integer_counter[item]
        else:
            integer_counter[item] = 1
    return [key for key in integer_counter][0]

def main():
    arr = [1, 2, 3, 2, 1]
    single_number = find_single_number(arr)
    print("The given list:", arr)
    print("Number that occurs once:", single_number)

if __name__ == '__main__':
    main()

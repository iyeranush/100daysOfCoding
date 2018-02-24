def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    O(n^2)
    """
    _len = len(nums)
    for index, item in enumerate(nums):
        for j in range(index+1, _len):
            if nums[index] + nums[j] == target:
                return [nums[index], nums[j]]

assert twoSum([2, 4, 8, 11, 7], 10) == [2, 8]


def two_sum_hash_table(nums, target):
    '''
    nums: array of int
    targer: int
    return: list of int
    eg: nums = [2, 4, 8, 11, 6]
    target = 10
    solution = [(2, 8), (4, 6)]
    Time complexity: O(n)
    '''
    pairs = {}
    result = []
    for i in nums:
        if i in pairs:
            result.append((pairs[i], i))
        else:
            pairs[target-i] = i

    return result

assert two_sum_hash_table([2, 4, 8, 11, 6], 10) == [(2, 8), (4, 6)]

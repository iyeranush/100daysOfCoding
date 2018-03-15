"""
Binary search
1) iterative
2) recursive
"""


ordered_list = [1, 2, 3, 4, 5, 6]

def binary_search_iterative(ordered_list, search_element):
    length = len(ordered_list)-1
    start = 0
    end = length
    while start != end:
        mid = int((end + start)/2)
        if search_element == ordered_list[mid]:
            return "Element {} found in index {} in the list".format(search_element, mid)
        elif search_element > ordered_list[mid]:
            start = mid + 1
        else:
            end = mid
    return "Element {} not found in the list".format(search_element)

print(binary_search_iterative(ordered_list, 7))
print(binary_search_iterative(ordered_list, 2))

def binary_search_recursive(ordered_list, search_element):
    start = 0
    end = len(ordered_list) - 1
    return binary_search(ordered_list, start, end, search_element)

def binary_search(arr, start, end, search):
    if start > end:
        return "Element {} not found in the list".format(search)
    mid = int((end + start)/2)
    if arr[mid] == search:
        return ("Found search {}, at position {}".format( search, mid))
    elif arr[mid] > search:
        binary_search(arr, start, mid-1, search)
    else:
        binary_search(arr, mid+1, end, search)

print(binary_search_recursive(ordered_list, 7))
print(binary_search_recursive(ordered_list, 2))

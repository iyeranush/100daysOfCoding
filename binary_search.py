# Functin to perform binary search.
# Takes an ordered list and a search element.
# Returns the index of the search element in the list.

ordered_list = [1, 2, 3, 4, 5, 6]

def binary_search(ordered_list, search_element):
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

print(binary_search(ordered_list, 7))
print(binary_search(ordered_list, 2))

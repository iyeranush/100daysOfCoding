def merge_sort_array(given_array):
    l = 0
    r = len(given_array) -1
    temp = [None]*len(given_array)
    merge_sort(given_array, temp, l, r)
    return given_array

def merge_sort(arr, temp, l, r):
    if l == r:
        return
    m = int((l + r)/2)
    merge_sort(arr, temp, l, m)
    merge_sort(arr, temp, m+1, r)
    merge_halves(arr, temp, l, r)

def merge_halves(arr, temp, l_start, r_end):
    l_end = int((l_start + r_end)/2)
    r_start = l_end + 1

    i = l_start
    l = l_start
    r = r_start

    while(l <= l_end and r <= r_end):
        if arr[l] <= arr[r]:
            temp[i] = arr[l]
            l+=1
        else:
            temp[i] = arr[r]
            r+=1
        i+=1
    '''
    if l <= l_end:
        for ind in range(l, l_end+1):
            temp[i] = arr[ind]
            i+=1
    if r <= r_end:
        for ind in range(r, r_end+1):
            temp[i] = arr[ind]
            i+=1
    for ind in range(l_start, r_end+1):
        arr[ind] = temp[ind]
    '''
    if l <= l_end:
        temp[i:r_end+1] = arr[l:l_end+1]
    if r <= r_end:
        temp[i:r_end+1] = arr[r:r_end+1]

    arr[l_start:r_end+1] = temp[l_start:r_end+1]

assert merge_sort_array([5, 4, 3, 1, 6, 8, 7, 2]) == [1, 2, 3, 4, 5, 6, 7, 8]

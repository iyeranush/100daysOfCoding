# Time Complexity: O(n/2) = O(n)
# SPace complexity: Constan. Inplace swaping

def swap(a, b):
    temp = a
    a = b
    b = temp
    return a, b

def reverse_inplace(arr):
    length = len(arr)
    for i in range(int(length/2)):
        if length-1-i != i:
            arr[i], arr[length-1-i] = swap(arr[i], arr[length-1-i])

def main():
    arr = [int(item) for item in input().strip().split(' ')]
    reverse_inplace(arr)
    print(' '.join([str(item) for item in arr]))

if __name__ == '__main__':
    main()

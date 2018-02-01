'''
SPARSE ARRAY:
The first line contains N, the number of strings.
The next N lines each contain a string.
The next line contains Q, the number of queries.
The following Q lines each contain a query string.

Sample Input

4
aba
baba
aba
xzxb
3
aba
xzxb
ab
Sample Output

2
1
0
'''


def search_string_ocurrance(strings, search_string):
    map_search_string_by_counter = {i: 0 for i in search_string}
    for string in strings:
        if string in map_search_string_by_counter:
            map_search_string_by_counter[string] += 1
    return [map_search_string_by_counter[string] for string in search_string]

def main():
    n = int(input().strip())
    strings = []
    for _ in range(0, n):
        strings.append(str(input().strip()))
    q = int(input().strip())
    search_strings = []
    for _ in range(0, q):
        search_strings.append(str(input().strip()))

    ocurrance = search_string_ocurrance(strings, search_strings)
    for item in ocurrance:
        print(item)

if __name__ == "__main__":
    main()

"""
LONGEST COMMON SUBSEQUENCE (LCS)
--------------------------

LCS between two strings "BATD", "ABACD" will be "BAD"
Note that the subsequence does not have consecutive characters.

Three approach:
    1) recursive O(2^(n+m))
    2) Memoize O(2nm) lcs called atmost twice == O(nm)
    3) Bottom-up

"""

def lcs(P, Q, n, m):
    if n == 0 or m == 0:
        result = 0
    elif P[n-1] == Q[m-1]:
        result = 1 + lcs(P, Q, n-1, m-1)
    elif P[n-1] != Q[m-1]:
        temp1 = lcs(P, Q, n, m-1)
        temp2 = lcs(P, Q, m-1, n)
        result = max(temp1, temp2)
    return result

def lcs_memo(P, Q, n, m, memo):
    if memo[n-1][m-1]:
        return memo[n-1][m-1]
    if n == 0 or m == 0:
        result = 0
    elif P[n-1] == Q[m-1]:
        result = 1 + lcs(P, Q, n-1, m-1)
    elif P[n-1] != Q[m-1]:
        temp1 = lcs(P, Q, n, m-1)
        temp2 = lcs(P, Q, m-1, n)
        result = max(temp1, temp2)
    memo[n-1][m-1] = result
    return result

assert lcs("ABC", "XYBSC", 3, 5) == 2

memo = [[None for x in range(5)] for _ in range(3)]
assert lcs_memo("ABC", "XYBSC", 3, 5, memo) == 2




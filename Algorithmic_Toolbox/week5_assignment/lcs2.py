# Uses python3

import sys
from pprint import pprint


def lcs2(a, b):
    """
    DYNAMIC PROGRAMMING APPROACH:
    Determine the length of the longest common subsequence (non-contiguous, i.e
    non-continuous) between2 given strings. Subsequences must be in order.
    Eg. lcs2('acb','abz')
    >>> 2
    Here 'ab' in the first string matches 'ab' in the second.
    """
    n, m = len(a)+1, len(b)+1
    dp_table = [[None for i in range(n)] for j in range(m)]
    for y in range(n):
        dp_table[0][y] = 0
    for x in range(m):
        dp_table[x][0] = 0
    a = [' ']+a
    b = [' ']+b
    for row in range(1, m):
        for col in range(1, n):
            if a[col] == b[row]:
                dp_table[row][col] = 1 + dp_table[row-1][col-1]
            else:
                dp_table[row][col] = max(dp_table[row][col-1], dp_table[row-1][col])
    return dp_table[-1][-1]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))

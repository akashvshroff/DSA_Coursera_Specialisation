# Uses python3

import sys


def lcs2(a, b):
    """
    RECURSIVE APPROACH:
    Determine the length of the longest common subsequence (non-contiguous, i.e
    non-continuous) between2 given strings. Subsequences must be in order.
    Eg. lcs2('acb','abz')
    >>> 2
    Here 'ab' in the first string matches 'ab' in the second.
    """
    if not a or not b:
        return 0
    if a[-1] == b[-1]:
        longest_res = 1 + lcs2(a[:-1], b[:-1])
    else:
        longest_res = max(lcs2(a[:-1], b), lcs2(a, b[:-1]))
    return longest_res


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

# python3

import sys


def solve_naive(string, slices):
    """
    Naive solution to a problem outlining the implementation of a rope data
    structure which facilitates easy slicing and merging.
    """
    for i, j, k in slices:
        chars = string[i:j+1]
        string = string[:i] + string[j+1:]
        # print(string, chars)
        if len(string) == k:
            string += chars
            continue
        for m in range(len(string)):
            if m == k:
                string = string[:m] + chars + string[m:]
                break
    return ''.join(string)


if __name__ == '__main__':
    s = list(input().strip())
    n = int(input())
    queries = []
    for query in range(n):
        queries.append(list(map(int, input().split())))
    print(solve_naive(s, queries))

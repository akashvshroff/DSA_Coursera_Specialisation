# Uses python3

import sys
from pprint import pprint


def lcs3(a, b, c):
    """
    An extension of the dynamic programming lcs2 program which finds the length
    of the longest common subsequence between 3 strings by using a 3-d dynamic
    programming table.
    """
    a = [' '] + a
    b = [' '] + b
    c = [' '] + c
    num_x, num_y, num_z = len(a), len(b), len(c)
    dp_table = [[[0 for k in range(num_z)] for j in range(num_y)] for i in range(num_x)]
    for x in range(1, num_x):
        for y in range(1, num_y):
            for z in range(1, num_z):
                if a[x] == b[y] == c[z]:
                    dp_table[x][y][z] = 1 + dp_table[x-1][y-1][z-1]
                else:
                    dp_table[x][y][z] = max(
                        dp_table[x][y][z-1],
                        dp_table[x][y-1][z],
                        dp_table[x-1][y][z]
                    )
    return dp_table[-1][-1][-1]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))

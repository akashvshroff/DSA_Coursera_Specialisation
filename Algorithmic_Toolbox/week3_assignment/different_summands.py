# Uses python3
import sys
import math


def optimal_summands(n):
    """
    Given n, find the largest pairwise distinct integer partition. Here largest
    indicates number of terms in the partition.
    """
    summands = []
    k = n
    l = 1
    while k > 0:
        if k <= 2*l:
            summands.append(k)
            k -= k
        else:
            summands.append(l)
            k -= l
        l += 1
    return summands


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')

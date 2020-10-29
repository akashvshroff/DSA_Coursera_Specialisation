# python3
import sys


def first_to_last(s):
    """
    For a BWT, return an array which marks the occurence number
    for each symbol in the string s. Starts with -1 since
    occurences are 0-based.
    """
    counts = {'$': 0, "A": 0, 'C': 0, 'G': 0, 'T': 0}
    for char in s:
        counts[char] += 1
    c = {'$': 0}
    sum_so_far = counts['$']
    for char in ['A', 'C', 'G', 'T']:
        c[char] = sum_so_far
        sum_so_far += counts[char]
    arr = [0] * len(s)
    for i in range(len(s) - 1, -1, -1):
        arr[i] = counts[s[i]] + c[s[i]] - 1
        counts[s[i]] -= 1
    return arr


def InverseBWT(bwt):
    """
    Given the Burrow-Wheeler Transform of a string, return the
    original string efficiently by employing the First-Last
    property of the BWT.
    """
    f2l = first_to_last(bwt)
    print(f2l)
    cur = 0
    s = '$'
    for _ in range(1, len(bwt)):
        s = bwt[cur] + s
        cur = f2l[cur]
    return s


if __name__ == '__main__':
    bwt = sys.stdin.readline().strip()
    print(InverseBWT(bwt))

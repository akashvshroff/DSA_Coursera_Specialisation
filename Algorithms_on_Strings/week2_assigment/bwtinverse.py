# python3
import sys


def InverseBWT(bwt):
    """
    Given the Burrow-Wheeler Transform of a string, return the
    original string efficiently by employing the First-Last
    property of the BWT.
    """
    hash = {}
    last_col = []
    hash_1 = {}
    first_col = []
    bwt_asc = sorted(bwt)
    for i in range(len(bwt)):
        ch = bwt[i]
        if hash.get(ch, None) is None:
            hash[ch] = 0
        last_col.append('{}{}'.format(ch, hash[ch]))
        hash[ch] += 1
        ch = bwt_asc[i]
        if hash_1.get(ch, None) is None:
            hash_1[ch] = 0
        first_col.append('{}{}'.format(ch, hash_1[ch]))
        hash_1[ch] += 1

    s = '$'
    cur = 0
    while len(s) != len(bwt):
        char = last_col[cur]
        s = char[0] + s
        cur = first_col.index(char)
    return s


if __name__ == '__main__':
    bwt = sys.stdin.readline().strip()
    print(InverseBWT(bwt))

# python3

def preprocess_bwt(bwt, symbols=['$', 'A', 'C', 'G', 'T']):
    """
    Preprocess the BWT string to generate 2 arrays:
    1. The first is a dict of lists where the keys are
    all the symbols in the hashmap and the value is a list of ints
    where each integer in the list refers to the number of occurences
    of the symbol so far.
    2. The second is a hash_map first occurence which
    maps each symbol to the index it occurs first in the
    sorted list of symbols for the BWT.
    """
    n = len(bwt)
    bwt_sorted = sorted(bwt)
    c = {ch: 0 for ch in symbols}
    count = {ch: [0 for _ in range(n+1)] for ch in symbols}
    for i in range(n):
        c[bwt[i]] += 1
        for ch in symbols:
            count[ch][i+1] = c[ch]
    first = {}
    for id, ch in enumerate(bwt_sorted):
        if first.get(ch, None) is None:
            first[ch] = id
    return count, first


def bwt_matching(bwt, pattern, count, first):
    """
    Use the Burrows-Wheeler transform to return the number of 
    exact matches of any pattern in a text.
    """
    top = 0
    bottom = len(bwt) - 1
    while top <= bottom:
        if pattern:
            symbol = pattern.pop()
            if symbol in bwt[top:bottom + 1]:
                top = first[symbol] + count[symbol][top]
                bottom = first[symbol] + count[symbol][bottom + 1] - 1
            else:
                return 0
        else:
            return bottom - top + 1


def main(bwt, patterns):
    """
    Driver function that preprocesses the BWT and calls upon the bwt_matching fn.
    """
    count, first = preprocess_bwt(bwt)
    res = []
    for pattern in patterns:
        res.append(str(bwt_matching(bwt, list(pattern), count, first)))
    print(' '.join(res))


if __name__ == '__main__':
    bwt = input()
    n = int(input())
    patterns = input().split()
    main(bwt, patterns)

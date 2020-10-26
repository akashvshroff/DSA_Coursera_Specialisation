# python3
import sys


def trie_construction(patterns):
    """
    Driver program to create a trie from a set of patterns.
    """
    if not patterns:
        return {}
    trie = {0: {}}
    max_key = 1
    for pattern in patterns:
        cur = trie[0]
        for letter in pattern:
            if letter in cur:  # match found
                cur = trie[cur[letter]]
            else:
                cur[letter] = max_key
                trie[max_key] = {}
                cur = trie[max_key]
                max_key += 1
    return trie


def prefix_matching(text, trie):
    """
    Find starting index of all matches of a pattern in a text.
    """
    v = 0
    for i in range(len(text)):
        symbol = text[i]
        if symbol in trie[v]:
            v = trie[v][symbol]
            if v not in trie or not trie[v]:
                return True
        else:
            return False


def solve(text, n, patterns):
    result = []

    trie = trie_construction(patterns)

    for i in range(len(text)):
        if prefix_matching(text[i:], trie):
            result.append(i)

    return result


text = sys.stdin.readline().strip()
n = int(sys.stdin.readline().strip())
patterns = []
for i in range(n):
    patterns += [sys.stdin.readline().strip()]

ans = solve(text, n, patterns)

sys.stdout.write(' '.join(map(str, ans)) + '\n')

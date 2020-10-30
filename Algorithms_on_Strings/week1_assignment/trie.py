# Uses python3
import sys


def build_trie(patterns):
    """
    Return the trie built from patterns
    in the form of a dictionary of dictionaries,
    e.g. {0:{'A':1,'T':2},1:{'C':3}}
    where the key of the external dictionary is
    the node ID (integer), and the internal dictionary
    contains all the trie edges outgoing from the corresponding
    node, and the keys are the letters on those edges, and the
    values are the node IDs to which these edges lead.
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


if __name__ == '__main__':
    patterns = sys.stdin.read().split()[1:]
    trie = build_trie(patterns)
    for node in trie:
        for c in trie[node]:
            print("{}->{}:{}".format(node, trie[node][c], c))

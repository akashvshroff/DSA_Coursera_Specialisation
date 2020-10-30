# python3
import sys


class Node:
    def __init__(self):
        """
        Node for the trie class.
        """
        self.children = {}


class Trie:
    def __init__(self):
        self.root = Node()

    def add(self, word):
        """
        Add a word to the try
        """
        cur = self.root
        for letter in word:
            if letter in cur.children:
                cur = cur.children[letter]
            else:
                cur.children[letter] = Node()
                cur = cur.children[letter]


def trie_construction(patterns):
    """
    Driver program to create a trie from a set of patterns.
    """
    trie = Trie()
    for pattern in patterns:
        trie.add(pattern)
    return trie


def prefix_matching(text, trie):
    """
    Find starting index of all matches of a pattern in a text.
    """
    cur = trie.root
    for letter in text:
        if not cur.children:
            return True
        if letter in cur.children:
            cur = cur.children[letter]
            if not cur.children:
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

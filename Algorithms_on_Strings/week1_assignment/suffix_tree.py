# python3
import sys


class Node:
    def __init__(self, label=''):
        """
        Node for the trie class.
        """
        self.children = {}
        self.label = label  # label leading up to this node


class Trie:
    def __init__(self, s):
        self.root = Node()
        self.root.children[s[0]] = Node(s)
        self.add(s)

    def add(self, word):
        """
        Add all suffixes to the trie, compressing it. There are 3 scenarios:
        1. Inserting a new word into the trie, could be at root or at any internal
        node.
        2. Adding a prefix to an existing node.
        3. Inserting a word in a partial match.
        """
        for i in range(1, len(word)):
            cur = self.root
            j = i
            while j < len(word):
                if word[j] in cur.children:
                    child = cur.children[word[j]]
                    label = child.label
                    k = j + 1
                    while k - j < len(label) and word[k] == label[k - j]:
                        k += 1
                    if k - j == len(label):  # label is exhausted, so move to next one
                        cur = child
                        j = k
                    else:  # either split a node or add prefix
                        c_exist, c_new = label[k - j], word[k]
                        mid = Node(label[:k - j])
                        mid.children[c_new] = Node(word[k:])
                        child.label = label[k - j:]
                        mid.children[c_exist] = child
                        cur.children[word[j]] = mid
                else:  # scenario 1 -> create new node
                    cur.children[word[j]] = Node(word[j:])


def show_trie(root):
    queue = []
    queue.append(root)
    while queue:
        u = queue.pop()
        if u != root:
            print(u.label)
        for label, node in u.children.items():
            queue.append(node)


def build_suffix_tree(text):
    """
    Build a suffix tree of the string text and show all
    of the labels of its edges (the corresponding substringsof the text) in any order.
    """
    trie = Trie(text)
    show_trie(trie.root)


if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    build_suffix_tree(text)

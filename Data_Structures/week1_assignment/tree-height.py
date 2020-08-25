# python3

import sys
import threading
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


class Node:
    """
    Helper function to create tree nodes.
    """

    def __init__(self, key=None):
        self.key = key
        self.children = []


def build_tree(n, node_data):
    """
    Given info about nodes, build a tree.
    """
    nodes = [Node(i) for i in range(n)]
    root = None
    for child in range(n):
        parent = node_data[child]
        if parent == -1:
            root = child
        else:
            nodes[parent].children.append(nodes[child])
    return 1 + find_height(nodes[root].children)


def find_height(tree):
    """
    Find the height of a given tree using recursion.
    """
    if not tree:
        return 0
    return 1 + max(find_height(child.children) for child in tree)


def main():
    n = int(input())
    node_data = list(map(int, input().split()))
    print(build_tree(n, node_data))


threading.Thread(target=main).start()

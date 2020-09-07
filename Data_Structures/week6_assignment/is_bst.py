#!/usr/bin/python3

import sys
import threading

sys.setrecursionlimit(2*10**9)  # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


class CheckBST:
    def __init__(self, tree):
        self.left = True
        self.right = True
        self.key, self.l_child, self.r_child = [], [], []
        self.is_valid = False
        for k, l, r in tree:
            self.key.append(k)
            self.l_child.append(l)
            self.r_child.append(r)
        if len(tree) > 1:
            self.is_valid = self.is_binary_search_tree(0, float("-inf"), float("inf"))
        else:
            self.is_valid = True

    def is_binary_search_tree(self, cur, min_, max_):
        """
        Recursive approach to check whether a binary search tree is the valid,
        i.e that for each node, it is larger than the left child and smaller than
        its right.
        """
        if cur == -1:
            return True
        if not min_ < self.key[cur] < max_:
            return False
        if self.l_child[cur] != -1:
            self.left = self.is_binary_search_tree(self.l_child[cur], min_, self.key[cur])
        if self.r_child[cur] != -1:
            self.right = self.is_binary_search_tree(self.r_child[cur], self.key[cur], max_)
        return self.left and self.right


def main():
    nodes = int(sys.stdin.readline().strip())
    tree = []
    for i in range(nodes):
        tree.append(list(map(int, sys.stdin.readline().strip().split())))
    bst = CheckBST(tree)
    if bst.is_valid:
        print("CORRECT")
    else:
        print("INCORRECT")


threading.Thread(target=main).start()

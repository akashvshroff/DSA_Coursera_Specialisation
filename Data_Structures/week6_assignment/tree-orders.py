# python3

import sys
import threading
sys.setrecursionlimit(10**6)  # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


class TreeOrders:
    def __init__(self):
        self.in_order_res, self.pre_order_res, self.post_order_res = [], [], []

    def read(self):
        """
        Given a tree rooted an index-0, print the pre,post and in-order traversals.
        """
        self.n = int(sys.stdin.readline())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c
        r = 0
        self.in_order(r)
        self.pre_order(r)
        self.post_order(r)

    def in_order(self, root):
        """
        In order traversal of a tree - from smallest to largest node.
        Left-Root-Right
        """
        if root == -1:
            return
        self.in_order(self.left[root])
        self.in_order_res.append(self.key[root])
        self.in_order(self.right[root])

    def pre_order(self, root):
        """
        Root-Left-Right
        """
        if root == -1:
            return
        self.pre_order_res.append(self.key[root])
        self.pre_order(self.left[root])
        self.pre_order(self.right[root])

    def post_order(self, root):
        """
        Left-Right-Root
        """
        if root == -1:
            return
        self.post_order(self.left[root])
        self.post_order(self.right[root])
        self.post_order_res.append(self.key[root])


def main():
    tree = TreeOrders()
    tree.read()
    print(" ".join(map(str, tree.in_order_res)))
    print(" ".join(map(str, tree.pre_order_res)))
    print(" ".join(map(str, tree.post_order_res)))


threading.Thread(target=main).start()

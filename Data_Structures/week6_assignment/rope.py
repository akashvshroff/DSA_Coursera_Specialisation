"""
Good job! (Max time used: 0.59/3.00, max memory used: 17231872/536870912.)

Whew! That was one hell of a challenge. My recommendations to people who are stuck:

-Reuse the splay tree from set_range_size. Replace int key with char key, long long size with size.

-Change update to update the size instead of size (node size is 1 + left size + right size)

-Change find() to orderstatistic function shown in the videos, I used an iterative version

-Write a function to give in order traversal of your splay tree

-In your process function split from right to left, as suggested by other users. Meaning: split at j + 1, then at i. Merge from left to right. My process used three splits and three merges
"""

root = None


class Vertex:
    def __init__(self, key, char, size, left, right, parent):
        (self.key, self.char, self.size, self.left, self.right,
         self.parent) = (key, char, size, left, right, parent)


def update(v):
    """
    Increase or edit the size parameter based on any changes owing to
    splaying.
    """
    if v == None:
        return
    v.size = 1 + (v.left.size if v.left != None else 0) + \
        (v.right.size if v.right != None else 0)
    if v.left != None:
        v.left.parent = v
    if v.right != None:
        v.right.parent = v


def small_rotation(v):
    """
    A smaller rotation on a specific case on splaying.
    """
    parent = v.parent
    if parent == None:
        return
    grandparent = v.parent.parent
    if parent.left == v:
        m = v.right
        v.right = parent
        parent.left = m
    else:
        m = v.left
        v.left = parent
        parent.right = m
    update(parent)
    update(v)
    v.parent = grandparent
    if grandparent != None:
        if grandparent.left == parent:
            grandparent.left = v
        else:
            grandparent.right = v


def big_rotation(v):
    """
    Calls upon small rotation twice to facilitate splaying.
    """
    if v.parent.left == v and v.parent.parent.left == v.parent:
        # Zig-zig
        small_rotation(v.parent)
        small_rotation(v)
    elif v.parent.right == v and v.parent.parent.right == v.parent:
        # Zig-zig
        small_rotation(v.parent)
        small_rotation(v)
    else:
        # Zig-zag
        small_rotation(v)
        small_rotation(v)


def splay(v):
    """
    Makes the variable v the root node of the tree.
    """
    if v == None:
        return None
    while v.parent != None:
        if v.parent.parent == None:
            small_rotation(v)
            break
        big_rotation(v)
    return v


def find_order_statistic(node, k):
    """
    Returns the kth smallest element in the tree.
    """
    if not node:
        return None
    if not node.left:
        s = -1
    else:
        s = node.left.size
    if k == s+1:
        return node
    elif k < s+1:
        return find_order_statistic(node.left, k)
    else:
        return find_order_statistic(node.right, k-s-1)


def split(root, k):
    """
    Split a tree based on the kth smallest element.
    """
    split_node = find_order_statistic(root, k)
    if split_node is None:
        return (root, None)
    right = splay(split_node)
    left = right.left
    right.left = None
    if left != None:
        left.parent = None
    update(left)
    update(right)
    return (left, right)


def merge(left, right):
    """
    Merge two given trees.
    """
    if left is None:
        return right
    if right is None:
        return left
    while right.left != None:  # going to end in the smallest element of right.
        right = right.left
    right = splay(right)
    right.left = left
    update(right)
    return right


def in_order_traversal(root, res=[]):
    """
    Prints an in-order traversal of the tree. Left-Node-Right.
    """
    if not root:
        return res
    res = in_order_traversal(root.left, res)
    res.append(root.char)
    res = in_order_traversal(root.right, res)
    return res


def make_tree(s):
    """
    Create a tree using the characters of a string.
    """
    global root
    for id, char in enumerate(s):
        new_vertex = Vertex(id, char, 0, None, None, None)
        root = merge(root, new_vertex)


def process_queries(qs):
    """
    Process the given queries and then print the in-order traversal.
    """
    global root
    for i, j, k in qs:
        useful, rem = split(root, j+1)
        prefix, to_use = split(useful, i)
        root = merge(prefix, rem)
        prefix, suffix = split(root, k)
        root = merge(merge(prefix, to_use), suffix)
    res = in_order_traversal(root, [])
    print(''.join(res))


if __name__ == '__main__':
    s = input()
    n = int(input())
    qs = []
    for _ in range(n):
        qs.append(list(map(int, input().split())))
    make_tree(s)
    process_queries(qs)

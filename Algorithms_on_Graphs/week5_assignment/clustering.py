# Uses python3
import sys
import math
import itertools as it


class DisjointSet:
    """
    Disjoint set implementation to use for the Kruskal's algorithm.
    """

    def __init__(self, n):
        self.parent = [None for _ in range(n)]
        self.rank = [None for _ in range(n)]
        self.num_sets = n

    def make_set(self, i):
        self.parent[i] = i
        self.rank[i] = 0

    def find(self, i):
        if i != self.parent[i]:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i == root_j:
            return
        self.num_sets -= 1
        if self.rank[root_i] > self.rank[root_j]:
            self.parent[root_j] = root_i
        else:
            self.parent[root_i] = root_j
            if self.rank[root_i] == self.rank[root_j]:
                self.rank[root_j] = self.rank[root_i] + 1


def kruskal(edges, n, k, x, y):
    """
    Modified kruskal's algorithm to find the maximum distance between k-clusters
    of a graph.
    """
    ds = DisjointSet(n)
    for i in range(n):
        ds.make_set(i)
    for u, v in edges:
        if ds.find(u) != ds.find(v):  # not in the same set
            if ds.num_sets == k:
                return edge_sort((u, v))
            else:
                ds.union(u, v)


def distance(x1, y1, x2, y2):
    """
    Returns distance between 2 points on a cartesian graph.
    """
    return math.sqrt((x1-x2)**2+(y1-y2)**2)


def edge_sort(edge):
    u, v = edge
    return distance(x[u], y[u], x[v], y[v])


def clustering(x, y, k, n):
    """
    Call upon Kruskal's algorithm after sorting all the edges in ascending
    order as per distance.
    """
    edges = list(it.combinations(range(n), 2))
    edges.sort(key=edge_sort)
    return kruskal(edges, n, k, x, y)


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    data = data[1:]
    x = data[0:2 * n:2]
    y = data[1:2 * n:2]
    data = data[2 * n:]
    k = data[0]
    print("{0:.9f}".format(clustering(x, y, k, n)))

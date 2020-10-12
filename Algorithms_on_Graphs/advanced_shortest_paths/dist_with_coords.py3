#!/usr/bin/python3

import sys
import heapq
import math


class AStar:
    def __init__(self, n, adj, cost, x, y):
        self.n = n  # number of nodes
        self.adj = adj  # adj nodes for each node
        self.cost = cost  # weight of an edge
        self.inf = n*10**6  # all node lengths are smaller
        self.d = {}  # dict to store distances
        self.visited = {}  # already processed
        self.workset = set()  # nodes processed
        # Coordinates of the nodes
        self.x = x
        self.y = y

    def distance(self, x1, y1, x2, y2):
        """
        Returns the cartesian distance between 2 co-ordinates on the graph,
        serves as the potential for A*.
        """
        return math.sqrt((x1-x2)**2+(y1-y2)**2)

    def clear(self):
        """
        Reinitialises the data structures for the next query.
        """
        self.d = {}
        self.visited = {}
        self.workset = set()

    def process(self, q, v, x, y):
        """
        Process all the outgoing nodes from q and relax the
        edges using the cost of the edge as well as the
        cartesian distance from the start vertex to the
        current vertex.
        """
        self.visited[v] = True
        dist = self.d.get(v, self.inf)
        for id, vertex in enumerate(self.adj[v]):
            if self.d.get(vertex, self.inf) > dist + self.cost[v][id]:
                self.d[vertex] = dist + self.cost[v][id]
                estimate = self.d[vertex] + \
                    self.distance(x, y, self.x[vertex], self.y[vertex])
                heapq.heappush(q, (estimate, vertex))

    def query(self, s, t):
        """
        Driver function for the A* algorithm which returns the
        shortest path between s and t.
        """
        self.clear()
        self.d[s] = 0
        q = [(0, s)]
        heapq.heapify(q)
        while q:
            v_obj = heapq.heappop(q)
            v_dist, v = v_obj
            if not self.visited.get(v, False):
                self.process(q, v, self.x[s], self.y[s])
        return self.d.get(t, -1)


def readl():
    return map(int, sys.stdin.readline().split())


if __name__ == '__main__':
    n, m = readl()
    x = [0 for _ in range(n)]
    y = [0 for _ in range(n)]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for i in range(n):
        a, b = readl()
        x[i] = a
        y[i] = b
    for e in range(m):
        u, v, c = readl()
        adj[u-1].append(v-1)
        cost[u-1].append(c)
    t, = readl()
    astar = AStar(n, adj, cost, x, y)
    for i in range(t):
        s, t = readl()
        print(astar.query(s-1, t-1))

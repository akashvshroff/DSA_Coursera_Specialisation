#!/usr/bin/python3

import sys
import heapq


class BiDij:
    def __init__(self, n):
        self.n = n   # Number of nodes
        self.inf = n*10**6  # All distances in the graph are smaller
        # Initialize distances for forward and backward searches
        self.d = [[self.inf]*n, [self.inf]*n]
        # visited[v] == True iff v was visited by forward or backward search
        self.visited = [[False for _ in range(n)] for s in range(2)]
        self.workset = set()  # Nodes visited by forward or backward search

    def clear(self):
        """
        Reinitialize the data structures for the next query after
        the previous query.
        """
        for v in self.workset:
            self.d[0][v] = self.d[1][v] = self.inf
            self.visited[0][v] = self.visited[1][v] = False
        self.workset = set()

    def visit(self, q, side, v, dist):
        """
        Try to relax the distance to node v from direction side by value dist.
        """
        if self.d[side][v] > dist:
            self.d[side][v] = dist
            heapq.heappush(q[side], (dist, v))
        return q

    def shortest_distance(self):
        """
        Retrieve the shortest distance from s to t by finding the
        best middle node.
        """
        distance = float('inf')
        for u in self.workset:
            distance = min(distance, self.d[0][u] + self.d[1][u])
        return distance if distance not in [float('inf'), self.inf] else -1

    def query(self, adj, cost, s, t):
        """
        Driver function that uses the bidirectional dijkstra function to find
        the shortest distance from s to t.
        """
        self.clear()
        if s == t:
            return 0
        self.d[0][s] = 0
        self.d[1][t] = 0
        q = [[(self.d[0][i], i) for i in range(n)], [(self.d[1][i], i) for i
                                                     in range(n)]]
        heapq.heapify(q[0])
        heapq.heapify(q[1])
        side = 0
        next_side = 1
        while q[0] and q[1]:
            v = heapq.heappop(q[side])
            v_dist, v_id = v
            if not self.visited[side][v_id]:
                self.visited[side][v_id] = True
                for i, u in enumerate(adj[side][v_id]):
                    q = self.visit(q, side, u,
                                   v_dist+cost[side][v_id][i])
                    self.workset.add(u)
            if self.visited[next_side][v_id]:
                return self.shortest_distance()
            side, next_side = next_side, side
        return -1


def readl():
    return map(int, sys.stdin.readline().split())


if __name__ == '__main__':
    n, m = readl()
    adj = [[[] for _ in range(n)], [[] for _ in range(n)]]
    cost = [[[] for _ in range(n)], [[] for _ in range(n)]]
    for e in range(m):
        u, v, c = readl()
        adj[0][u-1].append(v-1)
        cost[0][u-1].append(c)
        adj[1][v-1].append(u-1)
        cost[1][v-1].append(c)
    t, = readl()
    bidij = BiDij(n)
    for i in range(t):
        s, t = readl()
        print(bidij.query(adj, cost, s-1, t-1))

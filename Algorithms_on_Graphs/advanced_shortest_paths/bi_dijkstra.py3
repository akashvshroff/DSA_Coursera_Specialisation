#!/usr/bin/python3

import sys
import heapq


class BiDij:
    def __init__(self, n):
        self.n = n   # Number of nodes
        self.inf = n*10**6  # All distances in the graph are smaller
        # Initialize distances for forward and backward searches
        # visited[v] == True iff v was visited by forward or backward search
        self.workset = set()  # Nodes visited by forward or backward search
        self.set_memory()

    def set_memory(self):
        """
        Defaults the dist and proc variables
        """
        self.dist = {}
        self.dist_r = {}
        self.proc = {}
        self.proc_r = {}

    def clear(self):
        """
        Reinitialize the data structures for the next query after
        the previous query.
        """
        self.set_memory()
        self.workset = set()
        self.q = []
        self.q_r = []

    def shortest_distance(self, v):
        """
        Retrieve the shortest distance from s to t by finding the
        best middle node.
        """
        try:
            distance = self.dist[v] + self.dist_r[v]
        except KeyError:
            return -1
        for vertex in self.workset:
            dst = self.dist.get(vertex, self.inf) + \
                self.dist_r.get(vertex, self.inf)
            if dst < distance:
                distance = dst
        return distance

    def process(self, q, v, vs, weights, dist):
        """
        Process a node and relax all the edges adjoining the node.
        """
        for id, u in enumerate(vs):
            if dist.get(u, self.inf) > dist.get(v, self.inf) + weights[id]:
                dist[u] = dist.get(v, self.inf) + weights[id]
                heapq.heappush(q, (dist[u], u))
            self.workset.add(u)

    def query(self, adj, cost, s, t):
        """
        Driver function that uses the bidirectional dijkstra function to find
        the shortest distance from s to t.
        """
        if s == t:
            return 0
        self.clear()
        self.dist[s] = 0
        self.dist_r[t] = 0
        self.q = [(0, s)]
        self.q_r = [(0, t)]
        heapq.heapify(self.q)
        heapq.heapify(self.q_r)
        while self.q and self.q_r:
            v = heapq.heappop(self.q)
            v_d, v_id = v
            if not self.proc.get(v_id, False):
                self.process(self.q, v_id, adj[0][v_id],
                             cost[0][v_id], self.dist)
                self.proc[v_id] = True
            if self.proc_r.get(v_id, False):
                return self.shortest_distance(v_id)
            v_r = heapq.heappop(self.q_r)
            vr_d, vr_id = v_r
            if not self.proc_r.get(vr_id, False):
                self.process(self.q_r, vr_id, adj[1][vr_id],
                             cost[1][vr_id], self.dist_r)
                self.proc_r[vr_id] = True
            if self.proc.get(vr_id, False):
                return self.shortest_distance(vr_id)
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

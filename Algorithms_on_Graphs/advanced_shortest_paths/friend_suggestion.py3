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
        Try to relax the distance to node v from direction side by value dist.
        """
        # print(f'pre dist: {dist}')
        # print(f'pre heap: {q}')
        for id, u in enumerate(vs):
            # print(f'u: {u}')
            if dist.get(u, self.inf) > dist.get(v, self.inf) + weights[id]:
                dist[u] = dist.get(v, self.inf) + weights[id]
                heapq.heappush(q, (dist[u], u))
            self.workset.add(u)
        # print(f'post dist: {dist}')
        # print(f'post heap: {q}')

    def query(self, adj, cost, s, t):
        """
        Driver function that uses the bidirectional dijkstra function to find
        the shortest distance from s to t.
        """
        # print('****')
        # print(f's: {s}, t: {t}')
        # print(f'proc: {self.proc}, proc_r: {self.proc_r}')
        if s == t:
            return 0
        self.clear()
        self.dist[s] = 0
        self.dist_r[t] = 0
        self.q = [(self.inf, i) if i != s else (0, i) for i in range(self.n)]
        self.q_r = [(self.inf, j) if j != t else (0, t) for j in range(self.n)]
        heapq.heapify(self.q)
        heapq.heapify(self.q_r)
        while self.q and self.q_r:
            # print('forward')
            # print(f'self.q: {self.q}')
            v = heapq.heappop(self.q)
            # print(f'v: {v}')
            v_d, v_id = v
            if not self.proc.get(v_id, False):
                self.process(self.q, v_id, adj[0][v_id],
                             cost[0][v_id], self.dist)
                self.proc[v_id] = True
            if self.proc_r.get(v_id, False):
                # print('processed in forward')
                return self.shortest_distance(v_id)
            # print('reverse')
            # print(f'self.q_r: {self.q_r}')
            v_r = heapq.heappop(self.q_r)
            # print(f'self.v_r: {v_r}')
            vr_d, vr_id = v_r
            if not self.proc_r.get(vr_id, False):
                self.process(self.q_r, vr_id, adj[1][vr_id],
                             cost[1][vr_id], self.dist_r)
                self.proc_r[vr_id] = True
            if self.proc.get(vr_id, False):
                # print('processed in rev')
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

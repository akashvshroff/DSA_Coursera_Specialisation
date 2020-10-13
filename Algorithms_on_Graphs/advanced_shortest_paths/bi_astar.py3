#!/usr/bin/python3

import sys
import heapq
import math


class BiAStar:
    def __init__(self, n, adj, cost, adj_r, cost_r, x, y):
        self.n = n  # number of nodes
        self.adj = adj  # adj nodes for each node
        self.cost = cost  # weight of an edge
        self.adj_r = adj_r  # reverse graph
        self.cost_r = cost_r  # reverse costs
        self.inf = n*10**6  # all node lengths are smaller
        self.workset = set()  # nodes processed
        # Coordinates of the nodes
        self.x = x
        self.y = y
        self.xs, self.ys, self.xt, self.yt = None, None, None, None

    def set_memory(self):
        """
        Defaults the dist and proc variables.
        """
        self.dist = {}  # forward distance
        self.dist_r = {}  # backward distance
        self.proc = {}  # visited forward
        self.proc_r = {}  # visited backward

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
        self.set_memory()
        self.workset = set()
        self.xs, self.ys, self.xt, self.yt = None, None, None, None

    def shortest_distance(self, v):
        """
        Retrieve the shortest distance from s to t by finding the
        best middle node.
        """
        try:
            shortest = self.dist[v] + self.dist_r[v]
        except KeyError:
            return -1
        for vertex in self.workset:
            dst = self.dist.get(vertex, self.inf) + \
                self.dist_r.get(vertex, self.inf)
            if dst < shortest:
                shortest = dst
        return shortest

    def process(self, queue, v, d, adj, cost, side):
        """
        Process all the outgoing nodes from v and relax the
        edges using the cost of the edge as well as the
        cartesian distance from the start vertex to the
        current vertex - uses two potential function which
        are added to the queue based on the side (forward = 0,
        backward = 1).
        """
        dist = d.get(v, self.inf)
        for id, vertex in enumerate(adj[v]):
            if d.get(vertex, self.inf) > dist + cost[v][id]:
                d[vertex] = dist + cost[v][id]
                pif = self.distance(
                    self.xs, self.ys, self.x[vertex], self.y[vertex])
                pir = self.distance(
                    self.xt, self.yt, self.x[vertex], self.y[vertex])
                pf = (pif - pir) / 2.0
                pr = -pf
                estimate = d[vertex] + (pr if side else pf)
                heapq.heappush(queue, (estimate, vertex))
            self.workset.add(vertex)

    def query(self, s, t):
        """
        Driver function for the bi-directional A* algorithm
        which returns the shortest path between s and t.
        """
        self.clear()
        if s == t:
            return 0
        self.dist[s] = 0  # distances from start s
        self.dist_r[t] = 0  # distance from end t
        q = [(0, s)]  # forward queue
        q_r = [(0, t)]  # backward queue
        self.xs = self.x[s]
        self.ys = self.y[s]
        self.xt = self.x[t]
        self.yt = self.y[t]
        heapq.heapify(q)
        heapq.heapify(q_r)
        while q and q_r:
            v_dist, v = heapq.heappop(q)
            if not self.proc.get(v, False):
                self.proc[v] = True
                self.process(q, v, self.dist,
                             self.adj, self.cost, 0)
            if self.proc_r.get(v, False):
                return self.shortest_distance(v)
            vr_dist, vr = heapq.heappop(q_r)
            if not self.proc_r.get(vr, False):
                self.proc_r[vr] = True
                self.process(q_r, vr, self.dist_r,
                             self.adj_r, self.cost_r, 1)
            if self.proc.get(vr, False):
                return self.shortest_distance(vr)
        return -1


def readl():
    return map(int, sys.stdin.readline().split())


if __name__ == '__main__':
    n, m = readl()
    x = [0 for _ in range(n)]
    y = [0 for _ in range(n)]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    adj_r = [[] for _ in range(n)]
    cost_r = [[] for _ in range(n)]
    for i in range(n):
        a, b = readl()
        x[i] = a
        y[i] = b
    for e in range(m):
        u, v, c = readl()
        adj[u-1].append(v-1)
        cost[u - 1].append(c)
        adj_r[v - 1].append(u - 1)
        cost_r[v - 1].append(c)
    t, = readl()
    bi_astar = BiAStar(n, adj, cost, adj_r, cost_r, x, y)
    for i in range(t):
        s, t = readl()
        print(bi_astar.query(s-1, t-1))

# Uses python3

import sys


class Acyclic:
    def __init__(self, adj, n):
        self.adj = adj
        self.visited = {i: False for i in range(n)}
        self.n = n
        self.clock = 1
        self.previsit = [0]*n
        self.postvisit = [0]*n

    def pre(self, v):
        self.previsit[v] = self.clock
        self.clock += 1

    def post(self, v):
        self.postvisit[v] = self.clock
        self.clock += 1

    def explore(self, v):
        self.visited[v] = True
        self.pre(v)
        for vertex in self.adj[v]:
            if not self.visited[vertex]:
                self.explore(vertex)
        self.post(v)

    def dfs(self):
        for vertex in range(self.n):
            if not self.visited[vertex]:
                self.explore(vertex)

    def acyclic(self):
        self.dfs()
        for u in range(n):
            for v in self.adj[u]:
                if not self.postvisit[u] > self.postvisit[v]:
                    return 1
        return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    obj = Acyclic(adj, n)
    print(obj.acyclic())

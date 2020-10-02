# Uses python3

import sys


class Acyclic:
    def __init__(self, adj, n):
        self.adj = adj
        self.visited = {i: False for i in range(n)}
        self.stack = {k: False for k in range(n)}  # true if in stack
        self.n = n
        self.clock = 1

    def explore(self, v):
        """
        Explores all the nodes that are reachable from v. Uses a pseudo-stack
        to see if any node that has already been visited is being visited again.
        """
        self.visited[v] = True
        self.stack[v] = True
        # self.pre(v)
        for vertex in self.adj[v]:
            if not self.visited[vertex]:
                if self.explore(vertex):
                    return True
            elif self.stack[vertex]:
                return True
        # self.post(v)
        self.stack[v] = False  # popping stack
        return False

    def dfs(self):
        for vertex in range(self.n):
            if not self.visited[vertex]:
                if self.explore(vertex):
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
    print(obj.dfs())

# Uses python3

import sys

sys.setrecursionlimit(200000)


class TopoSort:
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

    def toposort(self):
        """
        Returns nodes in a linear, topological ordering.
        """
        self.dfs()
        nodes_sorted = sorted(range(n), key=lambda x: self.postvisit[x], reverse=True)
        return nodes_sorted


def explore(v, visited, adj):
    visited[v] = True
    for vertex in adj[v]:
        if not visited[vertex]:
            visited = explore(vertex, visited, adj)
    return visited


def number_of_strongly_connected_components(adj, rev_adj, n):
    """
    Finds the number of strongly connected comps by running the explore function
    on the sink of the graph, you get the strongly connected comp and then
    you can simple mark those nodes as visited and re-run.
    """
    result = 0
    linear_sort = TopoSort(rev_adj, n)
    rev_nodes = linear_sort.toposort()
    visited = {i: False for i in range(n)}
    for sink in rev_nodes:
        if not visited[sink]:
            visited = explore(sink, visited, adj)
            result += 1
    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    rev_adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        rev_adj[b-1].append(a-1)
    print(number_of_strongly_connected_components(adj, rev_adj, n))

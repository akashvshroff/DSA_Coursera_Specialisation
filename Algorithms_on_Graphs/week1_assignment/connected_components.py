# Uses python3

import sys


def explore(v, visited, adj):
    """
    Checks all the neighbours v in a recursive algorithm and sets all the nodes
    that you can visit to true.
    """
    visited[v] = True
    for w in adj[v]:
        if not visited[w]:
            visited = explore(w, visited, adj)
    return visited


def dfs(n, adj):
    """
    Depth First Search of the graph to find the number of connected components
    """
    num = 0
    visited = {i: False for i in range(n)}
    for v in range(n):
        if not visited[v]:
            visited = explore(v, visited, adj)
            num += 1
    return num


def number_of_components(n, adj):
    return dfs(n, adj)


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(number_of_components(n, adj))

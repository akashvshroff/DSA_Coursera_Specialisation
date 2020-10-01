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


def reach(adj, x, y, n):
    """
    Initialises a hashmap that checks reachability and returns if reachable.
    """
    visited = {i: False for i in range(n)}
    visited = explore(x, visited, adj)
    return 1 if visited[y] else 0


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(reach(adj, x, y, n))

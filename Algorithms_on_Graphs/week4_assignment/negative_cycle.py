# Uses python3

import sys


def relax(u, v, dist, c):
    if dist[v] > dist[u] + c:
        dist[v] = dist[u] + c
        return True
    return False


def bellman_ford(adj, cost, n, s):
    """
    Bellman-Ford algorithm to detect a negative weight cycle in a graph by
    relaxing edges and checking if an edge relaxed on the Vth iteration where
    V is the number of nodes in the graph.
    """
    dist = [float('inf') for _ in range(n)]
    prev = [None for _ in range(n)]
    dist[s] = 0
    for iteration in range(n-1):
        for u in range(n):
            for id, vertex in enumerate(adj[u]):
                relax(u, vertex, dist, cost[u][id])
    # final iteration
    for u in range(n):
        for id, vertex in enumerate(adj[u]):
            if relax(u, vertex, dist, cost[u][id]):
                return 1
    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n+1)]
    cost = [[] for _ in range(n+1)]
    adj[0] = [i for i in range(1, n+1)]
    cost[0] = [i for i in range(1, n+1)]
    for ((a, b), w) in edges:
        adj[a].append(b)
        cost[a].append(w)
    print(bellman_ford(adj, cost, n+1, 0))

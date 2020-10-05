# Uses python3

import sys
import queue


def bipartite(adj, n):
    bi = [None for _ in range(n)]
    bi[0] = True
    q = queue.Queue()
    q.put(0)
    while not q.empty():
        u = q.get()
        cur = bi[u]
        for v in adj[u]:
            if bi[v] is None:  # unvisited
                q.put(v)
                bi[v] = not cur
            else:  # visited
                if bi[v] == cur:  # not bipartite
                    return 0
    return 1


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
    print(bipartite(adj, n))

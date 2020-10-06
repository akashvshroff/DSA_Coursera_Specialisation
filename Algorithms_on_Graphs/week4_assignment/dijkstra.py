# Uses python3

import sys
import heapq


def distance(adj, cost, s, t, n):
    """
    An implementation of Dijkstra's algorithm in order to find the shortest
    path between 2 nodes based on some weight attributed to each edge.
    """
    dist = [float("inf") for _ in range(n)]
    prev = [None for _ in range(n)]
    dist[s] = 0
    heap = [(dist[i], i) for i in range(n)]
    heapq.heapify(heap)
    min_checked = {i: False for i in range(n)}  # checks if the min has already been found
    while heap:
        u = heapq.heappop(heap)  # min id tuple
        d, id = u
        if not min_checked[id]:
            for cost_id, vertex in enumerate(adj[id]):
                if dist[vertex] > d + cost[id][cost_id]:
                    dist[vertex] = d + cost[id][cost_id]
                    prev[vertex] = id
                    heapq.heappush(heap, (dist[vertex], vertex))
        min_checked[id] = True  # so that it cannot be checked again
    return dist[t] if dist[t] != float('inf') else -1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t, n))

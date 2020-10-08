# Uses python3
import sys
import math
import heapq


def distance(x1, y1, x2, y2):
    """
    Returns the distance between 2 points on a graph.
    """
    return math.sqrt((x1-x2)**2+(y1-y2)**2)


def prim(s, n, x, y):
    """
    Uses Prim's algorithm to find the lenght of the minimum spanning tree for a
    collection of cartesian points.
    """
    heap = [(float('inf'), i) if i != s else (0, i) for i in range(n)]
    visited = {i: False for i in range(n)}
    cost = [float('inf') for i in range(n)]
    cost[s] = 0
    total = 0.0
    heapq.heapify(heap)
    while heap:
        v = heapq.heappop(heap)
        v_c, v_id = v
        if not visited[v_id]:
            for z in range(n):
                if z != v_id:
                    vertex_distance = distance(x[v_id], y[v_id], x[z], y[z])
                    if not visited[z] and cost[z] > vertex_distance:
                        cost[z] = vertex_distance
                        heapq.heappush(heap, (cost[z], z))
            total += v_c
        visited[v_id] = True
    return total


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(prim(0, n, x, y)))

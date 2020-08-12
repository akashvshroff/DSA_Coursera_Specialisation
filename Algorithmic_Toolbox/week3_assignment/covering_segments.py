# Uses python3
import sys


def optimal_points(segments):
    """
    Given start and end points of line segments as a list, find the minimum no.
    of points such that every line segment contains one such point.
    """
    points = []
    segments.sort(key=lambda x: x[1])
    while segments:
        to_rem = []
        num = segments[0][1]
        points.append(num)
        for segment in segments:
            if segment[0] <= num <= segment[1]:
                to_rem.append(segment)
        for item in to_rem:
            segments.remove(item)
    return points


if __name__ == '__main__':
    n = int(input())
    segments = []
    for i in range(n):
        segments.append(list(map(int, input().split())))
    points = optimal_points(segments)
    print(len(points))
    print(*points)

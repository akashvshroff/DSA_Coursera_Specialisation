# Uses python3
import sys
import math


def distance(p1, p2):
    """
    Returns the distance between 2 points based on the distance formula.
    """
    return ((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)**0.5


def small_min(points):
    """
    Smallest distance between 3 or less points.
    """
    res = float('inf')
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            res = min(res, distance(points[i], points[j]))
    return res


def across_distance(rem_y, dist):
    """
    Points across the division line.
    """
    rem_y.sort(key=lambda x: x[1])
    res = dist
    for i in range(len(rem_y)):
        for j in range(i+1, min(i+8, len(rem_y))):
            if abs(rem_y[i][1]-rem_y[j][1]) <= dist:
                res = min(res, distance(rem_y[i], rem_y[j]))
    return res


def minimum_distance(points):
    """
    Determines the minimum distance between 2 points in a set of given points
    using a divide and conquer approach.
    """
    # print(points)
    if len(points) <= 3:
        return small_min(points)
    mid = len(points)//2
    l_points = points[:mid]
    r_points = points[mid:]

    left_min = minimum_distance(l_points)
    right_min = minimum_distance(r_points)

    cur_min = min(left_min, right_min)
    mid_x = (l_points[-1][0] + r_points[0][0])/2
    rem_y = [p for p in points if abs(p[0]-mid_x) <= cur_min]
    if len(rem_y) > 1:
        cur_min = across_distance(rem_y, cur_min)
    return cur_min


if __name__ == '__main__':
    n = int(input())
    points = []
    for i in range(n):
        x, y = list(map(int, input().split()))
        points.append([x, y])
    points.sort(key=lambda x: x[0])
    print("{0:.9f}".format(minimum_distance(points)))

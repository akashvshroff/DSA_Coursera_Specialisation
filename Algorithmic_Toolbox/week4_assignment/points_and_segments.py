# Uses python3
import sys


def helper_sort(item):
    """
    Helper sort function that attributes values to the directions that are used
    to sort.
    """
    vals = {
        'L': 1,  # left end of segment
        'P': 2,  # a point
        'R': 3  # right end of segment
    }
    return item[0], vals[item[1]]


def segregate_items(starts, ends, points):
    """
    Segregates the items based on their characteristics and combines them as a
    2-d array where the index 0 holds the value and the index 1 holds either 'L'
    ,'P' or 'R' indicating left end, point or right end.
    """
    res = []
    for s in starts:
        res.append([s, 'L'])
    for e in ends:
        res.append([e, 'R'])
    for p in points:
        res.append([p, 'P'])
    res.sort(key=helper_sort)
    return res


def fast_count_segments(starts, ends, points):
    """
    Counts the number of line segments that a point can be found in.
    """
    graph_items = segregate_items(starts, ends, points)
    # print(graph_items)
    point_cnt = {p: 0 for p in points}
    cur = 0
    for item in graph_items:
        if item[1] == 'L':
            cur += 1
        elif item[1] == 'R':
            cur -= 1
        else:
            point_cnt[item[0]] = cur

    cnt = [point_cnt[point] for point in points]
    return cnt

# def naive_count_segments(starts, ends, points):
#     cnt = [0] * len(points)
#     for i in range(len(points)):
#         for j in range(len(starts)):
#             if starts[j] <= points[i] <= ends[j]:
#                 cnt[i] += 1
#     return cnt


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')

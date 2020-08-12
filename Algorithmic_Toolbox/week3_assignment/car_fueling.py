# python3
import sys


def compute_min_refills(distance, tank, stops):
    """
    Find the minimum number of refuelling stops along a distance AB where the
    vehicle has a certain tank capacity and fuel stops are arranged randomly at
    some distance from A.
    """
    stops.insert(0, 0)
    stops.append(distance)
    num_refills, cur_refill = 0, 0
    n = len(stops)-1
    while cur_refill < n:  # if it is n, it has reached destination.
        last_refill = cur_refill
        while cur_refill < n and stops[cur_refill+1] - stops[last_refill] <= tank:
            cur_refill += 1
        if cur_refill == last_refill:
            return -1
        if cur_refill < n:
            num_refills += 1
    return num_refills


if __name__ == '__main__':
    # d = int(input())
    # m = int(input())
    # n = int(input())
    # stops = list(map(int, input().split()))
    d, m, n, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))

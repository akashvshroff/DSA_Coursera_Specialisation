# Uses python3
import sys


def optimal_weight(n, W, w):
    """
    A dynamic programming solution to the discrete knapsack problem without
    repetitions where you maximise value while adhering to a limit on the total
    weight. Here the value corresponds the weight and there is no distinct value
    althought that would use the same approach only replacing the w[i] marked
    by an asterisk by v[i] where v[i] corresponds to the value of the ith item.
    """
    if not W or not n:
        return 0
    w.insert(0, 0)  # w runs from 1 to n to match with the dp table.
    value = [[0 for y in range(W+1)] for x in range(n+1)]
    for i in range(1, n+1):
        for weight in range(1, W+1):
            value[i][weight] = value[i-1][weight]
            if w[i] <= weight:
                val = value[i-1][weight-w[i]] + w[i]  # * Replace with v[i]
                if value[i][weight] < val:
                    value[i][weight] = val
    return value[n][W]


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(n, W, w))

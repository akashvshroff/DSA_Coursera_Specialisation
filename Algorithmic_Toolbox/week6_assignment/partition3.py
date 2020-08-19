# Uses python3
import sys


def optimal_weight(W, w):
    """
    A dynamic programming solution to the discrete knapsack problem without
    repetitions where you maximise value while adhering to a limit on the total
    weight. Here the value corresponds the weight and there is no distinct value
    althought that would use the same approach only replacing the w[i] marked
    by an asterisk by v[i] where v[i] corresponds to the value of the ith item.
    """
    n = len(w)
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

    items_chosen = []
    i = len(w) - 1
    j = W

    while i and j:
        if value[i][j] != value[i-1][j]:  # item has been chosen
            items_chosen.append(i)
            j -= w[i]
        i -= 1

    if items_chosen:
        for item in items_chosen:
            w.pop(item)
    w.pop(0)  # filler element added
    return value[-1][-1], w


def partition3(A, k=3):
    """
    A dynamic programming approach to the 3-partition problem where the 0/1
    knapsack problem is used to determine whether an array of integers can be
    split into 3 groups whose sum is equal.
    """
    total = sum(A)
    if not A or not total or total % k:
        return 0
    bucket_sum = total//k
    w1, A = optimal_weight(bucket_sum, A)
    w2, A = optimal_weight(bucket_sum, A)
    if w1 == bucket_sum and w2 == bucket_sum:
        return 1
    else:
        return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition3(A))

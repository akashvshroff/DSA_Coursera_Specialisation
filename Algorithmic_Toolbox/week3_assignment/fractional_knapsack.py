# Uses python3
import sys


def get_optimal_value(n, capacity, weights, values):
    """
    The fractional knapsack problem - filling a bag with a set capacity (weight
    limit) with items in order to maximise value.
    """
    value = 0.0
    val_weight = [[values[i], weights[i]] for i in range(n)]
    sorted_items = sorted(val_weight, key=lambda x: x[0]/x[1], reverse=True)
    for i in range(n):
        if not capacity:
            return value
        vi, wi = sorted_items[i]
        a = min(wi, capacity)
        value += a*vi/wi
        capacity -= a
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(n, capacity, weights, values)
    print("{:.10f}".format(opt_value))

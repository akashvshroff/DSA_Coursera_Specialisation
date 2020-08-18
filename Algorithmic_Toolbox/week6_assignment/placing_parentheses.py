# Uses python3
from pprint import pprint


def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False


def min_and_max(i, j, op, m, M):
    """
    Helper function to get min and max of a sub-expression.
    """
    max_val = float('-inf')
    min_val = float("inf")
    for k in range(i, j):
        a = evalt(M[i][k], M[k+1][j], op[k])
        b = evalt(M[i][k], m[k+1][j], op[k])
        c = evalt(m[i][k], M[k+1][j], op[k])
        d = evalt(m[i][k], m[k+1][j], op[k])
        max_val = max(max_val, a, b, c, d)
        min_val = min(min_val, a, b, c, d)
    return min_val, max_val


def get_maximum_value(dataset):
    """
    Maximise the value of an arithmetic expression by placing parentheses and
    altering the order of operations.
    """
    d = [int(i) for i in dataset if i.isdigit()]
    op = [o for o in dataset if o in ['*', '-', '+']]
    n = len(d)
    d.insert(0, None)
    op.insert(0, None)
    m = [[0 for x in range(n+1)] for y in range(n+1)]
    M = [[0 for x in range(n+1)] for y in range(n+1)]
    for i in range(1, n+1):
        m[i][i] = d[i]
        M[i][i] = d[i]
    for s in range(1, n):
        for i in range(1, n-s+1):
            j = i + s
            m[i][j], M[i][j] = min_and_max(i, j, op, m, M)
    return M[1][n]


if __name__ == "__main__":
    pprint(get_maximum_value(input()))

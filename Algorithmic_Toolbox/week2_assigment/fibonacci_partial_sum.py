# Uses python3
import sys


def get_sum(n):
    n = n % 60
    if n <= 1:
        return n
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a


def fibonacci_partial_sum_naive(f, t):
    """
    Sum of fibonacci numbers from F(f) to F(t).
    """
    sum_f = get_sum(f+1)-1 if f else 0
    sum_t = get_sum(t+2)-1
    return (sum_t-sum_f) % 10


if __name__ == '__main__':
    input = sys.stdin.read()
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_naive(from_, to))

# Uses python3
import sys


def get_pisano(m):
    prev, cur = 0, 1
    for i in range(m*m):
        prev, cur = cur, (prev+cur) % m
        if prev == 0 and cur == 1:
            return i+1


def get_fibonacci_huge(n, m):
    """
    Get the fibonacci number for n mod m with n ranging to 10^14.
    """
    pp = get_pisano(m)
    n = n % pp
    if n <= 1:
        return n
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a % m


if __name__ == '__main__':
    input = sys.stdin.read()
    n, m = map(int, input.split())
    print(get_fibonacci_huge(n, m))

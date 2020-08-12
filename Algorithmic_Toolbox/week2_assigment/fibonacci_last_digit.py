# Uses python3
import sys


def get_fibonacci_last_digit(n):
    """
    Last digit of a large fibonacci number, till 10^7.
    """
    if n <= 1:
        return n
    a, b = 0, 1
    for i in range(n):
        a, b = b, (a+b) % 10
    return a


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit(n))

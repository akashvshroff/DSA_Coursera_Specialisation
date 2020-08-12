# Uses python3
import sys


def get_sum(n):
    n = n % 60  # pisano period of 10
    if n <= 1:
        return n
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a


def get_last_digit(num):
    """
    Get last digit of the sum of fibonacci numbers till F(num).
    """
    s = get_sum(num+2)-1
    return s % 10


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_last_digit())

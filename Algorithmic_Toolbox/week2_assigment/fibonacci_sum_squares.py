# Uses python3
from sys import stdin


def fibonacci_last_digit(n):
    n = n % 60
    if n <= 1:
        return n
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a % 10


def sum_squares(n):
    """
    Last digit of the sum of squares of the first n fibonacci numbers.
    """
    return (fibonacci_last_digit(n)*fibonacci_last_digit(n+1)) % 10


if __name__ == '__main__':
    n = int(stdin.read())
    print(sum_squares(n))

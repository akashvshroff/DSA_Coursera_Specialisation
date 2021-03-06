# Uses python3
import sys


def gcd_naive(a, b):
    return a if not b else gcd_naive(b, a % b)


if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    a, b = (a, b) if b <= a else (b, a)
    print(gcd_naive(a, b))

# Uses python3

import sys


def greater_or_equal(num1, num2):
    if num2 == float('-inf'):
        return True
    if num1+num2 >= num2+num1:
        return True
    return False


def largest_number(digits):
    """
    The largest number obtainable using arbitrary positive integer numbers.
    Eg. 23 93 39 would be 933923.
    """
    res = ""
    while digits:
        max_digit = float("-inf")
        for digit in digits:
            if greater_or_equal(digit, max_digit):
                max_digit = digit
        res += max_digit
        digits.remove(max_digit)
    return res


if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))

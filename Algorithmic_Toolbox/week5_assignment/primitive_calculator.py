# Uses python3
import sys


def optimal_sequence(n):
    num_ops = [[] for i in range(n+1)]
    num_ops[1] = [1]
    for i in range(2, n+1):
        to_check = []
        to_check += [num_ops[i - 1]]
        to_check += [num_ops[i//2]] if not i % 2 else []
        to_check += [num_ops[i//3]] if not i % 3 else []
        num_ops[i] = min(to_check, key=len)+[i]
    return num_ops[n]


if __name__ == '__main__':
    n = int(input())
    sequence = list(optimal_sequence(n))
    print(len(sequence) - 1)
    for x in sequence:
        print(x, end=' ')

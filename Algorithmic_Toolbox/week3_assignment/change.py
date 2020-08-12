# Uses python3
import sys


def get_change(m):
    """
    Using only 1,5 and 10 denomination coins, return the minimum amount of
    coins needed to make change for an integer m.
    """
    amt = m
    coins = [10, 5, 1]
    num_coins = 0
    for coin in coins:
        if not m:
            break
        if coin <= m:
            used, rem = divmod(m, coin)
            num_coins += used
            m = rem
    return num_coins


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))

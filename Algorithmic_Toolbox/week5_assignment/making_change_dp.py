import sys


def make_change(amt, coins=[1, 3, 4]):
    """
    Returns the optimal number of coins needed to make change using dynamic
    programming.
    """
    if not amt:
        return 0
    min_coins = [None for i in range(0, amt+1)]
    min_coins[0] = 0
    for money in range(1, amt+1):
        min_coins[money] = float("inf")
        for coin in coins:
            if coin <= money:
                num_coins = min_coins[money-coin]+1
                if num_coins < min_coins[money]:
                    min_coins[money] = num_coins
    return min_coins[amt]


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(make_change(m))

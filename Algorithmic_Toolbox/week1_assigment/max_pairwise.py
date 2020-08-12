def pairwise():
    n = int(input())
    arr = [int(x) for x in input().split()]
    arr.sort()
    print(arr[-1]*arr[-2])


if __name__ == '__main__':
    pairwise()

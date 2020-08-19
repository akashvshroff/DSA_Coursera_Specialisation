def partition_driver(arr, k=3):
    """
    Driver function that determines if a parition is possible.
    """
    sum_items = sum(arr)
    if sum_items % k or not sum_items:
        return 0
    used = [False for _ in arr]
    return partition3(0, arr, used, k, 0, sum_items//k)


def partition3(start, arr, used, k, progress_sum, target_sum):
    """
    Another approach to solve the 3-partition problem using backtracking.
    """
    if k == 1:
        return 1
    if progress_sum == target_sum:
        return partition3(0, arr, used, k-1, 0, target_sum)
    if progress_sum > target_sum:
        return 0
    for i in range(start, len(arr)):
        if not used[i]:
            used[i] = True
            if partition3(i+1, arr, used, k, progress_sum + arr[i], target_sum):
                return 1
            used[i] = False
    return 0


if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))
    print(partition_driver(nums))

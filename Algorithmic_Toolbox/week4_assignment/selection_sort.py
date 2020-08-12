def sort_selection(nums):
    """
    The easiest sorting technique that chooses the smallest(or max) element at
    each iteration of the inner loop and places it in the first spot, following
    which it continues from the next element. O(n^2) time complexity.
    """
    for i in range(len(nums)):
        min_index = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]
    return nums


print(sort_selection([1, 2, 3, 4, 2, 3, 1, 23, 4, 4, 67, 543, 29]))

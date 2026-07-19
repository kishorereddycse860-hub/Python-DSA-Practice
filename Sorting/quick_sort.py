# Problem Statement: Given an array of size n, sort the array using Quick Sort.
"""
Problem Statement: Given an array of integers called nums, sort the array in non-decreasing order
using the quick sort algorithm (iterative, no functions) and return the sorted array.
"""

nums = list(map(int, input().split()))
n = len(nums)
# stack to store (low, high) ranges instead of recursive calls
stack = [(0, n - 1)]
while stack:
    low, high = stack.pop()
    if low < high:
        # ---- Partition logic (inline, no function) ----
        pivot = nums[low]
        i = low
        j = high
        while i < j:
            while nums[i] <= pivot and i <= high - 1:
                i = i + 1
            while nums[j] > pivot and j >= low + 1:
                j = j - 1
            if i < j:
                nums[i], nums[j] = nums[j], nums[i]
        nums[low], nums[j] = nums[j], nums[low]
        partition_index = j
        # ---- End of partition logic ----
        # push left and right sub-ranges onto the stack (instead of recursive calls)
        stack.append((low, partition_index - 1))
        stack.append((partition_index + 1, high))
print(nums)

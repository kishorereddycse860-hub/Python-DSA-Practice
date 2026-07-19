# Problem Statement: Given an array of size n, sort the array using Merge Sort.
"""
Problem Statement: Given an array of integers called nums, sort the array in non-decreasing order
using the merge sort algorithm and return the sorted array.
"""
nums = list(map(int, input().split()))
n = len(nums)

width = 1
while width < n:
    left = 0
    while left < n - 1:
        mid = min(left + width - 1, n - 1)
        right = min(left + 2 * width - 1, n - 1)

        left_arr = nums[left:mid+1]
        right_arr = nums[mid+1:right+1]

        i = 0
        j = 0
        k = left
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] <= right_arr[j]:
                nums[k] = left_arr[i]
                i = i + 1
            else:
                nums[k] = right_arr[j]
                j = j + 1
            k = k + 1

        while i < len(left_arr):
            nums[k] = left_arr[i]
            i = i + 1
            k = k + 1

        while j < len(right_arr):
            nums[k] = right_arr[j]
            j = j + 1
            k = k + 1

        left = left + 2 * width
    width = width * 2

print(nums)

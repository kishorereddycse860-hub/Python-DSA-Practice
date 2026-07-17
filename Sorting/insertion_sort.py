"""
Problem Statement: Given an array of integers called nums, sort the array in non-decreasing order 
using the insertion sort algorithm and return the sorted array.
A sorted array in non-decreasing order is an array where each element is greater than or equal to 
all preceding elements in the array.

Time Complexity: O(n^2) worst/average case, O(n) best case (already sorted)
Space Complexity: O(1)
"""
nums = list(map(int, input().split()))
a = len(nums)
for i in range(1, a):
    j = i
    while j > 0 and nums[j - 1] > nums[j]:
        temp = nums[j]
        nums[j] = nums[j - 1]
        nums[j - 1] = temp
        j = j - 1
print(nums)

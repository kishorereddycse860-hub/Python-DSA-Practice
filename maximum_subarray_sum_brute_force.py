"""
Problem: Maximum Subarray Sum (Brute Force)
Statement: Given an integer array nums, find the subarray with the largest sum 
           and return the sum of the elements present in that subarray.
           (A subarray is a contiguous non-empty sequence of elements.)

Approach:
    - Generate every possible subarray using two nested loops.
    - Outer loop fixes the starting index i.
    - Inner loop extends the subarray by moving the ending index j.
    - Keep a running current_sum by adding nums[j] at each step.
    - Compare current_sum with max_sum and update whenever a larger sum is found.

Time Complexity: O(n^2)  -> nested loops checking all subarrays
Space Complexity: O(1)   -> no extra data structure used
"""

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
n = len(nums)

max_sum = float('-inf')

for i in range(n):
    current_sum = 0
    for j in range(i, n):
        current_sum += nums[j]
        max_sum = max(max_sum, current_sum)

print("Maximum Subarray Sum (Brute Force):", max_sum)

"""
Problem: Left Rotate the Array by One

Given an integer array nums, rotate the array to the left by one position.
No need to return anything - modify the array in-place.

Example:
Input: nums = [1, 2, 3, 4, 5]
Output: [2, 3, 4, 5, 1]

Approach: Store the first element in a temp variable, shift all other
elements one position to the left, then place temp at the last index.

Time Complexity: O(n)
Space Complexity: O(1)
"""

n = int(input())
nums = list(map(int, input().split()))

temp = nums[0]
for i in range(1, n):
    nums[i - 1] = nums[i]
nums[n - 1] = temp

print(*nums)

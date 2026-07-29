"""
Problem: Rotate Array by Two (Left Rotation)

Given an integer array nums, rotate the array to the left by two positions.
The first two elements move to the last two indices, and every other
element shifts two positions to the left.

Example:
Input: nums = [1, 2, 3, 4, 5]
Output: [3, 4, 5, 1, 2]

Approach:
- Store the first two elements in a temporary list.
- Shift every element two positions to the left.
- Place the stored elements at the last two indices.

Time Complexity: O(n)
Space Complexity: O(1) additional space
"""

n = int(input("Enter the size of array: "))
nums = []
for i in range(n):
    nums.append(int(input()))

if n >= 2:
    temp = nums[:2]
    for i in range(n - 2):
        nums[i] = nums[i + 2]
    nums[n - 2] = temp[0]
    nums[n - 1] = temp[1]

print(nums)

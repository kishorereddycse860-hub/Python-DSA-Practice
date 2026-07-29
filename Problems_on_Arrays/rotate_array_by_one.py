"""
Problem: Rotate Array by One (Left Rotation)

Given an integer array nums, rotate the array to the left by one position.
The first element moves to the last index, and every other element
shifts one position to the left.

Example:
Input: nums = [1, 2, 3, 4, 5]
Output: [2, 3, 4, 5, 1]

Approach:
- Store the first element in a temporary variable.
- Shift every element one position to the left.
- Place the stored first element at the last index.

Time Complexity: O(n)
Space Complexity: O(1) additional space
"""

n = int(input("Enter the size of array: "))
nums = []
for i in range(n):
    nums.append(int(input()))

if n > 0:
    temp = nums[0]
    for i in range(n - 1):
        nums[i] = nums[i + 1]
    nums[n - 1] = temp

print(nums)

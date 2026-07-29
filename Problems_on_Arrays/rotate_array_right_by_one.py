"""
Problem: Rotate Array by One (Right Rotation)

Given an integer array nums, rotate the array to the right by one position.
The last element moves to the first index, and every other element
shifts one position to the right.

Example:
Input: nums = [1, 2, 3, 4, 5]
Output: [5, 1, 2, 3, 4]

Approach:
- Store the last element in a temporary variable.
- Shift every element one position to the right, iterating backwards
  to avoid overwriting values before they're used.
- Place the stored last element at index 0.

Time Complexity: O(n)
Space Complexity: O(1) additional space
"""

n = int(input("Enter the size of array: "))
nums = []
for i in range(n):
    nums.append(int(input()))

if n > 0:
    temp = nums[n - 1]
    for i in range(n - 1, 0, -1):
        nums[i] = nums[i - 1]
    nums[0] = temp

print(nums)

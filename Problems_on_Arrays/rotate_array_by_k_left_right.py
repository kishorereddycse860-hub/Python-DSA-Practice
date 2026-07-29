"""
Problem: Rotate Array by K (Left or Right Rotation)

Given an integer array nums and a number k, rotate the array by k
positions either to the left or to the right, based on user input.

Example (Left):
Input: nums = [1, 2, 3, 4, 5], k = 2, direction = left
Output: [3, 4, 5, 1, 2]

Example (Right):
Input: nums = [1, 2, 3, 4, 5], k = 2, direction = right
Output: [4, 5, 1, 2, 3]

Approach:
- Normalize k using k = k % n, since rotating by n positions brings
  the array back to its original state (handles k > n safely).
- Left rotation:
    - Store the first k elements in a temporary list.
    - Shift every element k positions to the left.
    - Place the stored elements at the last k indices.
- Right rotation:
    - Store the last k elements in a temporary list.
    - Shift every element k positions to the right, iterating
      backwards to avoid overwriting values before they're used.
    - Place the stored elements at the first k indices.

Time Complexity: O(n)
Space Complexity: O(k) additional space (for the temp list)
"""

n = int(input("Enter the size of array: "))
nums = []
print("Enter the array elements:")
for i in range(n):
    nums.append(int(input()))

a = input("Enter left or right: ").strip().lower()
k = int(input("Enter the number of elements to rotate: "))

if n > 0:
    k = k % n   # normalize k to avoid issues when k > n

if a == "left":
    temp = nums[:k]
    for i in range(n - k):
        nums[i] = nums[i + k]
    nums[n - k:] = temp
    print(nums)
elif a == "right":
    temp = nums[-k:] if k > 0 else []
    for i in range(n - 1, k - 1, -1):
        nums[i] = nums[i - k]
    nums[:k] = temp
    print(nums)
else:
    print("Invalid input. Please enter 'left' or 'right'.")

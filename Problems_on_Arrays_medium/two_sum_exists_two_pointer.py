"""
Problem: Two Sum - Check if a pair with given sum exists in Array (Variant 1)

Given an array of integers nums[] and an integer target, check if there exist
two numbers in the array whose sum equals target.

Approach: Two Pointer
    - First, sort the array (two pointer technique requires sorted order).
    - Take two pointers: left = 0 (start) and right = n-1 (end).
    - Calculate current_sum = nums[left] + nums[right].
        - If current_sum == target -> pair found, print "YES".
        - If current_sum < target  -> sum too small, move left pointer forward
                                       (left += 1) to increase the sum.
        - If current_sum > target  -> sum too large, move right pointer backward
                                       (right -= 1) to decrease the sum.
    - Repeat until left < right. If pointers cross without a match -> print "NO".

Time Complexity  : O(n log n)  -> dominated by the sorting step
                                  (the two-pointer scan itself is O(n))
Space Complexity : O(1)        -> in-place sort, no extra space
                                  (Note: sorting disturbs original indices,
                                   so this approach is only suited to the
                                   YES/NO variant, not the "return indices" one)
"""


n = int(input("Enter the size of array: "))
nums = []
for _ in range(n):
    nums.append(int(input("Enter the elements to add into array: ")))
target = int(input("Enter the target value: "))
nums.sort() left = 0
right = n - 1
found = False
while left < right:
    current_sum = nums[left] + nums[right]
    if current_sum == target:
        found = True
        print("YES")
        break
    elif current_sum < target:
        left += 1 
    else:
        right -= 1
if not found:
    print("NO")

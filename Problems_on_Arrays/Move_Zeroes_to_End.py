"""
Problem: Move Zeroes to End
----------------------------
Given an array of integers, move all zeros to the end of the array
while maintaining the relative order of the non-zero elements.

Approach: Extra Space (Temp List)
----------------------------------
- Traverse the array once.
- Store all non-zero elements in a 'result' list (in their original order).
- Store all zero elements in a separate 'temp' list.
- Concatenate result + temp to get the final answer.

Time Complexity:  O(n)
Space Complexity: O(n)  -> uses extra lists (not in-place)

Example:
Input:  0 1 0 3 12
Output: 1 3 12 0 0
"""

nums = list(map(int, input().split()))

result = []
temp = []

for i in range(len(nums)):
    if nums[i] == 0:
        temp.append(nums[i])
    else:
        result.append(nums[i])

result = result + temp

print(*result)

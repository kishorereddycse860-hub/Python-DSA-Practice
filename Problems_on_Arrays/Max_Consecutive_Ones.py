"""
Count Maximum Consecutive One's in the array

Problem Statement: Given an array that contains only 1 and 0 return the count of maximum consecutive ones in the array.
"""

n = int(input("enter the size of array:"))
nums = []
for i in range(n):
    nums.append(int(input()))

count = 0
max_count = 0

for i in range(len(nums)):
    if nums[i] == 1:
        count += 1
        max_count = max(max_count, count)
    else:
        count = 0

print("maximum consecutive ones:", max_count)

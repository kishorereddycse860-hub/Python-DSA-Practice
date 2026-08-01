"""
Problem Statement: Given a non-empty array of integers arr, every element appears twice except for one. Find that single one.
"""

n = int(input("enter the size of array:"))
nums = []
for i in range(n):
    nums.append(int(input()))

for i in range(len(nums)):
    count = 0
    for j in range(len(nums)):
        if nums[j] == nums[i]:
            count += 1
    if count == 1:
        print("the element which is single:", nums[i])
        break

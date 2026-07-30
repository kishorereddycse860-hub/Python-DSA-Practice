"""
Problem Statement: Given an array, and an element num the task is to find if num is present in the given array or not.
If present print the index of the element or print -1.
"""

n = int(input("enter the size of array:"))
nums = []
for i in range(n):
    nums.append(int(input()))

num = int(input("enter the element to be searched:"))

found_index = -1
for i in range(len(nums)):
    if nums[i] == num:
        found_index = i
        break

print(found_index)

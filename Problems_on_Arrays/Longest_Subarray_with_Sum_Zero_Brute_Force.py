"""
Longest Subarray with Sum Zero

Problem Statement: Given an array containing both positive and negative integers,
we have to find the length of the longest subarray with the sum of all elements
equal to zero.
"""

n = int(input("enter the size of array:"))
nums = []
for i in range(n):
    nums.append(int(input()))

max_len = 0
for i in range(n):
    current_sum = 0
    for j in range(i, n):
        current_sum += nums[j]
        if current_sum == 0:
            length = j - i + 1
            max_len = max(max_len, length)

print("longest subarray length:", max_len)

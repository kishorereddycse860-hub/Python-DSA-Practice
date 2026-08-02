"""
Longest Subarray with given Sum K (Positives)
Problem Statement: Given an array nums of size n and an integer k, find the length
of the longest sub-array that sums to k. If no such sub-array exists, return 0.
"""
n = int(input("enter the size of array:"))
nums = []
for i in range(n):
    nums.append(int(input()))
k = int(input("enter the target sum k:"))
max_len = 0
for i in range(n):
    current_sum = 0
    for j in range(i, n):
        current_sum += nums[j]
        if current_sum == k:
            length = j - i + 1
            max_len = max(max_len, length)
print("longest subarray length:", max_len)

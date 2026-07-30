"""
Given an array arr[] of size n-1 with distinct integers in the range of [1, n].
This array represents a permutation of the integers from 1 to n with one element missing. Find the missing element in the array.
"""

n = int(input("enter the size of array:"))
nums = []
for i in range(n):
    nums.append(int(input()))

total = n + 1

expected_sum = total * (total + 1) // 2
actual_sum = sum(nums)

missing = expected_sum - actual_sum
print("the missing element is :", missing)

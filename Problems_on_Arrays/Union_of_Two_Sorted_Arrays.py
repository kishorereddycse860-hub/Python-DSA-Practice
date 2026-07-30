"""
Union of Two Sorted Arrays

Problem Statement: Given two sorted arrays, arr1, and arr2 of size n and m. Find the union of two sorted arrays.

The union of two arrays can be defined as the common and distinct elements in the two arrays.

NOTE: Elements in the union should be in ascending order.
"""

n = int(input("enter the size of array(n):"))
nums = []
nums1 = []

for i in range(n):
    nums.append(int(input()))

m = int(input("enter the size of array(m):"))
for i in range(m):
    val = int(input())
    if val not in nums1:
        nums1.append(val)

for i in range(len(nums)):
    if nums[i] not in nums1:
        nums1.append(nums[i])

nums1.sort()
print(*nums1)

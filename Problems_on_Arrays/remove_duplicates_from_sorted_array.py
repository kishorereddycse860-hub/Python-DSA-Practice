"""
Problem Statement: Given an integer array sorted in non-decreasing order, remove the 
duplicates in place such that each unique element appears only once. The relative 
order of the elements should be kept the same.

If there are k elements after removing the duplicates, then the first k elements of 
the array should hold the final result. It doesn't matter what you leave beyond the 
first k elements.

Approach:
Since the array is sorted, all duplicate values will always be adjacent to each other.
We use two pointers:
- 'i' scans through the entire array from left to right.
- 'k' tracks the count of unique elements found so far, and also acts as the index 
  where the next unique element should be placed.
We start with k = 1, since the first element is always unique by default.
For every element nums[i], we compare it with nums[k-1] (the last confirmed unique 
element). If they are different, nums[i] is a new unique value, so we place it at 
index k and increment k. If they are the same, it's a duplicate, so we simply skip it.
At the end, k holds the total number of unique elements, and the first k elements 
of nums hold the final in-place result.

Time Complexity: O(n)  -> single pass through the array
Space Complexity: O(1) -> no extra data structure used, modification done in-place
"""

def remove_duplicates(nums):
    if len(nums) == 0:
        return 0
    k = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[k-1]:
            nums[k] = nums[i]
            k += 1
    return k

nums = list(map(int, input().split(",")))
k = remove_duplicates(nums)
print(k)
print(nums[:k])

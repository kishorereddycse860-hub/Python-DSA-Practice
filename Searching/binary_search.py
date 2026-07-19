# Problem Statement: Given a sorted array and a target value, find the index of the target using Binary Search.
"""
Problem Statement: Given a sorted array of integers called nums and an integer target,
return the index of target in nums using Binary Search. If target is not found, return -1.
"""

nums = list(map(int, input().split()))
target = int(input())

low = 0
high = len(nums) - 1
result = -1

while low <= high:
    mid = (low + high) // 2

    if nums[mid] == target:
        result = mid
        break
    elif nums[mid] < target:
        low = mid + 1
    else:
        high = mid - 1

print(result)

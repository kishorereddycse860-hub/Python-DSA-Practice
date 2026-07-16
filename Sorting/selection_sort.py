# Selection Sort - takes space-separated integers as input
# Given an array of N integers, implement the Selection sorting algorithm
# Time Complexity: O(n^2) - all cases
# Space Complexity: O(1)

nums = list(map(int, input().split()))
a = len(nums)
for i in range(a):
    min_idx = i
    for j in range(i + 1, a):
        if nums[j] < nums[min_idx]:
            min_idx = j
    temp = nums[i]
    nums[i] = nums[min_idx]
    nums[min_idx] = temp
print(nums)

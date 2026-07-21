# Bubble Sort - takes space-separated integers as input
# Time Complexity: O(n^2)
# Space Complexity: O(1)

nums = list(map(int, input().split()))
a = len(nums)
for i in range(a):
    for j in range(a - 1):
        if nums[j] > nums[j + 1]:
            temp = nums[j]
            nums[j] = nums[j + 1]
            nums[j + 1] = temp
print(nums)

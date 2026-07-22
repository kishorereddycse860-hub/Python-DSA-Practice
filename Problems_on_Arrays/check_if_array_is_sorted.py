"""
The idea is pretty simple here, We will start with the element at the 0th index, and will compare it with all of its future elements that are present in the array.
If the picked element is smaller than or equal to all of its future values then we will move to the next Index/element until the whole array is traversed.
If any of the picked elements is greater than its future elements, Then simply we will return False.
If the size of the array is Zero or One i.e ( N = 0 or N = 1 ) or the entire array is traversed successfully then we will simply return True.
"""

def is_sorted(nums):
    l = len(nums)
    if l == 0 or l == 1:
        return True
    for i in range(l-1):
        if nums[i] > nums[i+1]:
            return False
    return True

nums = list(map(int, input().split(",")))
print(is_sorted(nums))

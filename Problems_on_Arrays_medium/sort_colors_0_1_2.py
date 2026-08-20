"""
Problem: Sort Colors (0s, 1s, 2s)
Link: https://leetcode.com/problems/sort-colors/
Difficulty: Medium
Topic: Sorting

Given an array nums consisting of only 0, 1, or 2, sort the array
in-place so that objects of the same color are adjacent, in the
order 0, 1, 2 (non-decreasing order).

Approach: Brute Force (Bubble Sort)
Time Complexity: O(n^2)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a = len(nums)
        for i in range(a):
            for j in range(a - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]


# Local test (not required on LeetCode, useful for your own repo testing)
if __name__ == "__main__":
    nums = [2, 0, 2, 1, 1, 0]
    Solution().sortColors(nums)
    print("Sorted array:", nums)

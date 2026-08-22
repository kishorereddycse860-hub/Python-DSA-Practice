"""
Problem: Majority Element (N/2 Approach)

Given an integer array nums of size n, return the majority element.
The majority element is the element that appears more than n/2 times
in the array. The array is guaranteed to have a majority element.

Approach: Better (Hashmap / Dictionary Frequency Counting)
- Traverse the array once and build a frequency dictionary for each element.
- Traverse the dictionary and return the key whose frequency > n/2.

Time Complexity: O(n)  -> single pass to build freq dict + single pass to check
Space Complexity: O(n) -> extra dictionary to store frequency of elements
"""

n = int(input("Enter the size of the array: "))
nums = []
for q in range(n):
    nums.append(int(input("Enter The Numbers To Enter In The Array: ")))

a = len(nums)
s = n // 2
freq = {}

for i in range(a):
    if nums[i] in freq:
        freq[nums[i]] += 1
    else:
        freq[nums[i]] = 1

for key in freq:
    if freq[key] > s:
        print(key)
        break

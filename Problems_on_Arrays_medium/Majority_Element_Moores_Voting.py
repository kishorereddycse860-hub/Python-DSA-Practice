"""
Problem: Majority Element (Moore's Voting Algorithm)

Given an integer array nums of size n, return the majority element.
The majority element is the element that appears more than n/2 times
in the array. The array is guaranteed to have a majority element.

Approach: Optimal (Moore's Voting Algorithm)
- Maintain a candidate and a count.
- If count becomes 0, pick the current element as the new candidate.
- If current element equals candidate, increment count, else decrement count.
- Since majority element occurs more than n/2 times, it can never be fully
  cancelled out, so candidate holds the majority element at the end.
- No verification pass needed since majority element is guaranteed to exist.

Time Complexity: O(n)  -> single pass through the array
Space Complexity: O(1) -> only two variables used, no extra data structure
"""

n = int(input("Enter the size of the array: "))
nums = []
for q in range(n):
    nums.append(int(input("Enter The Numbers To Enter In The Array: ")))

count = 0
candidate = None

for i in range(n):
    if count == 0:
        candidate = nums[i]
    if nums[i] == candidate:
        count += 1
    else:
        count -= 1

print(candidate)

"""
Problem: Two Sum - Check if a pair with given sum exists in Array (Variant 1)

Given an array of integers nums[] and an integer target, check if there exist
two numbers in the array whose sum equals target.

Approach: Brute Force
    - Use two nested loops to check every possible pair (q, p) where q != p.
    - The condition q != p ensures we don't add an element to itself,
      but still allows pairing duplicate values at different indices.
    - If any pair sums up to target, set found = True, print "YES",
      and break out of both loops immediately.
    - If no such pair is found after checking all combinations, print "NO".

Time Complexity  : O(n^2)  -> nested loop checks every (q, p) combination
Space Complexity : O(1)    -> no extra space used
"""

n = int(input("Enter the size of array: "))
nums = []
for e in range(n):
    nums.append(int(input("Enter the elements to add into array: ")))
target = int(input("Enter the target value: "))
a = len(nums)  
found = False
for q in range(a):
    for p in range(a):
        if q != p and nums[q] + nums[p] == target:
            found = True
            print("YES")
            break 
    if found:
        break  
if not found:
    print("NO")

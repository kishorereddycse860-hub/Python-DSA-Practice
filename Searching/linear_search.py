"""
Linear Search Algorithm
Time Complexity: O(n)
Space Complexity: O(1)
"""

array = [1, 2, 3, 4, 5, 6, 7]
target = 6
found = False

for i in range(len(array)):
    if target == array[i]:
        print("Element found at index:", i)
        found = True
        break

if not found:
    print("Element not found in array")

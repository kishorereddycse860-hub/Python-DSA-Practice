"""
Linear Search Algorithm
Time Complexity: O(n)
Space Complexity: O(1)
"""

array = list (map(int,input().split()))
target = int(input("Enter the element to search for: "))
found = False

for i in range(len(array)):
    if target == array[i]:
        print("Element found at index:", i)
        found = True
        break

if not found:
    print("Element not found in array")

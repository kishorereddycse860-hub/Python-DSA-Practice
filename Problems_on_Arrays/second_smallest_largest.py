nums = []
n = int(input("Enter the number of elements: "))
for i in range(n):
    num = int(input("Enter element: "))
    nums.append(num)

# ---- Largest and Second Largest ----
largest = nums[0]
for i in range(1, n):
    if nums[i] > largest:
        largest = nums[i]

slargest = -1
for i in range(n):
    if nums[i] != largest:
        if slargest == -1 or nums[i] > slargest:
            slargest = nums[i]

# ---- Smallest and Second Smallest ----
smallest = nums[0]
for i in range(1, n):
    if nums[i] < smallest:
        smallest = nums[i]

ssmallest = -1
for i in range(n):
    if nums[i] != smallest:
        if ssmallest == -1 or nums[i] < ssmallest:
            ssmallest = nums[i]

print("Largest element is:", largest)
print("Second largest element is:", slargest)
print("Smallest element is:", smallest)
print("Second smallest element is:", ssmallest)

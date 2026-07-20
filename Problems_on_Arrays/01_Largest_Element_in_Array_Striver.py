nums = []
n = int(input("Enter the number of elements: "))
for i in range(n):
    num = int(input("Enter element: "))
    nums.append(num)
largest = nums[0]
for i in range(1, n):
    if nums[i] > largest:
        largest = nums[i]
print("Largest element is:", largest)

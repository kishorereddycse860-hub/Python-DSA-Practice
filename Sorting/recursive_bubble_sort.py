# RECURSIVE BUBBLE SORT - Simple Version (User Input)

def recursive_bubble_sort(arr, n):
    # Base case: if size is 1, array is already sorted
    if n == 1:
        return

    # One pass: push the largest element to the end
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]

    # Recursive call on the reduced array (size n-1)
    recursive_bubble_sort(arr, n - 1)


# ---- MAIN PROGRAM ----
elements = input("Enter numbers separated by space: ")
arr = list(map(int, elements.split()))

recursive_bubble_sort(arr, len(arr))

print("Sorted array:", arr)

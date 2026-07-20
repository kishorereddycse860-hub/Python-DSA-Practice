# RECURSIVE INSERTION SORT - Simple Version (User Input)

def recursive_insertion_sort(arr, n):
    # Base case: if size is 1 (or 0), array is already sorted
    if n <= 1:
        return

    # Step 1: Sort the first n-1 elements first (recursive call)
    recursive_insertion_sort(arr, n - 1)

    # Step 2: Insert the last element (arr[n-1]) into its correct position
    # among the already sorted first n-1 elements
    last = arr[n - 1]
    j = n - 2

    while j >= 0 and arr[j] > last:
        arr[j + 1] = arr[j]   # Shift element to the right
        j -= 1

    arr[j + 1] = last   # Place last element in its correct position


# ---- MAIN PROGRAM ----
elements = input("Enter numbers separated by space: ")
arr = list(map(int, elements.split()))

recursive_insertion_sort(arr, len(arr))

print("Sorted array:", arr)

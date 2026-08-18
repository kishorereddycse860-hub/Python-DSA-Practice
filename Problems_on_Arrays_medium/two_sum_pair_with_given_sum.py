"""
Problem: Two Sum - Check if a pair with given sum exists in Array

Given an array of integers arr[] and an integer target:
    Variant 1: Return YES/NO if there exist two numbers whose sum equals target.
    Variant 2: Return indices [i, j] of the two numbers whose sum equals target.
               If no such pair exists, return [-1, -1].

Approach: Hashing (optimal)
    - Traverse the array once.
    - For each element, check if (target - current_element) already exists in the hashmap.
    - If found -> pair exists, return result immediately.
    - Else -> store current element's value and index in the hashmap, move ahead.

Time Complexity  : O(n)   -> single pass through the array
Space Complexity : O(n)   -> hashmap can store up to n elements in worst case
"""


def two_sum_exists(arr, target):
    """
    Variant 1: Check if a pair with the given sum exists.

    Args:
        arr (list[int]): input array of integers
        target (int): target sum

    Returns:
        str: "YES" if a pair exists, otherwise "NO"
    """
    seen = set()

    for num in arr:
        complement = target - num
        if complement in seen:
            return "YES"
        seen.add(num)

    return "NO"


def two_sum_indices(arr, target):
    """
    Variant 2: Return indices of the pair with the given sum.

    Args:
        arr (list[int]): input array of integers
        target (int): target sum

    Returns:
        list[int]: [i, j] indices of the pair if found, otherwise [-1, -1]
    """
    index_map = {}  # value -> index

    for i, num in enumerate(arr):
        complement = target - num
        if complement in index_map:
            return [index_map[complement], i]
        index_map[num] = i

    return [-1, -1]


def two_sum_brute_force(arr, target):
    """
    Brute Force approach (for reference/comparison).

    Time Complexity  : O(n^2)
    Space Complexity : O(1)

    Args:
        arr (list[int]): input array of integers
        target (int): target sum

    Returns:
        list[int]: [i, j] indices of the pair if found, otherwise [-1, -1]
    """
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == target:
                return [i, j]

    return [-1, -1]


if __name__ == "__main__":
    arr = [2, 6, 5, 8, 11]
    target = 14

    print("Array:", arr)
    print("Target:", target)

    # Variant 1
    print("Variant 1 (YES/NO):", two_sum_exists(arr, target))

    # Variant 2
    print("Variant 2 (Indices - Hashing):", two_sum_indices(arr, target))
    print("Variant 2 (Indices - Brute Force):", two_sum_brute_force(arr, target))

    # Case with no valid pair
    arr2 = [1, 2, 3]
    target2 = 100
    print("Array:", arr2)
    print("Target:", target2)
    print("Variant 1 (YES/NO):", two_sum_exists(arr2, target2))
    print("Variant 2 (Indices):", two_sum_indices(arr2, target2))

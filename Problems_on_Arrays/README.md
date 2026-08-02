# Problems on Arrays

This folder contains my solutions to array-based DSA problems, following Striver's A2Z DSA Sheet. Each file includes the problem statement as a docstring, followed by a working Python solution.

## Problems List

| # | Problem | File | Approach | Time Complexity | Space Complexity |
|---|---------|------|----------|------------------|-------------------|
| 1 | Largest Element in an Array | `01_Largest_Element_in_Array_Striver.py` | Single pass, track max | O(n) | O(1) |
| 2 | Second Smallest and Second Largest Element | `second_smallest_largest.py` | Single/double pass, track candidates | O(n) | O(1) |
| 3 | Check if Array is Sorted | `check_if_array_is_sorted.py` | Single pass comparison | O(n) | O(1) |
| 4 | Remove Duplicates from Array | `remove_duplicates_from_array.py` | Traversal with duplicate check | O(n) or O(n²) | O(n) |
| 5 | Remove Duplicates from Sorted Array | `remove_duplicates_from_sorted_array.py` | Two-pointer (in-place) | O(n) | O(1) |
| 6 | Left Rotate Array by One Position | `left_rotate_array_by_one.py` | Store first element, shift, reinsert | O(n) | O(1) |
| 7 | Right Rotate Array by One Position | `rotate_array_right_by_one.py` | Store last element, shift, reinsert | O(n) | O(1) |
| 8 | Rotate Array by Two Positions | `rotate_array_by_two.py` | Repeated single rotation / extended logic | O(n) | O(1) |
| 9 | Rotate Array by K Positions (Left & Right) | `rotate_array_by_k_left_right.py` | Reversal algorithm / extra array | O(n) | O(1) or O(n) |
| 10 | Move Zeroes to End | `Move_Zeroes_to_End.py` | Two-pointer in-place swap | O(n) | O(1) |
| 11 | Linear Search in Array | `Linear_Search_in_Array.py` | Single pass search | O(n) | O(1) |
| 12 | Union of Two Sorted Arrays | `Union_of_Two_Sorted_Arrays.py` | Duplicate-checked merge + sort | O(n×m) | O(n+m) |
| 13 | Finding Missing Number in a Range | `Finding_Missing_Number_in_a_Range.py` | Sum formula | O(n) | O(1) |
| 14 | Max Consecutive Ones | `Max_Consecutive_Ones.py` | Single pass counter | O(n) | O(1) |
| 15 | Single Number (Brute Force) | `Single_Number_Brute_Force.py` | Nested loop occurrence count | O(n²) | O(1) |
| 16 | Longest Subarray with Sum K (Brute Force) | `Longest_Subarray_with_Sum_K_Brute_Force.py` | Nested loop, running sum | O(n²) | O(1) |
| 17 | Longest Subarray with Sum Zero (Brute Force) | `Longest_Subarray_with_Sum_Zero_Brute_Force.py` | Nested loop, running sum | O(n²) | O(1) |

## Notes

- All solutions currently use direct console input (`input()`) for testing.
- Files marked "Brute Force" have a more optimal approach planned as a follow-up (e.g., Sliding Window, Prefix Sum + Hashing, XOR).
- This folder will be split into `Problems_on_Arrays_Easy`, `Problems_on_Arrays_Medium`, and `Problems_on_Arrays_Hard` as more problems are added.

## Reference

- [Striver's A2Z DSA Sheet](https://takeuforward.org/strivers-a2z-dsa-course-sheet-2/)

## Author

**Kishore Reddy Gayam**
- GitHub: [@kishorereddycse860-hub](https://github.com/kishorereddycse860-hub)
- LinkedIn: [kishore-reddy-gayam](https://linkedin.com/in/kishore-reddy-gayam-867254316)

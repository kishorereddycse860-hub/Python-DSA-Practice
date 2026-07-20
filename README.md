# Sorting Algorithms

This folder contains Python implementations of common sorting algorithms, solved as part of my DSA practice (following Striver's A2Z DSA Sheet).

---

## 📌 Algorithms Covered

### 1. Bubble Sort (`bubble_sort.py`)
- **Idea:** Repeatedly swaps adjacent elements if they are in the wrong order.
- **Time Complexity:** O(n²)
- **Space Complexity:** O(1)
- **Stable:** Yes

### 2. Selection Sort (`selection_sort.py`)
- **Idea:** Selects the minimum element from the unsorted part and places it at the beginning.
- **Time Complexity:** O(n²)
- **Space Complexity:** O(1)
- **Stable:** No

### 3. Insertion Sort (`insertion_sort.py`)
- **Idea:** Builds the sorted array one element at a time by inserting each element into its correct position.
- **Time Complexity:** O(n²)
- **Space Complexity:** O(1)
- **Stable:** Yes

### 4. Merge Sort (`merge_sort.py`)
- **Idea:** Divide and conquer — splits the array into halves, sorts each half, then merges them back together.
- **Time Complexity:** O(n log n)
- **Space Complexity:** O(n)
- **Stable:** Yes

### 5. Quick Sort (`quick_sort.py`)
- **Idea:** Divide and conquer — picks a pivot, partitions the array around it, then recursively sorts both sides.
- **Time Complexity:** O(n log n) average, O(n²) worst case
- **Space Complexity:** O(log n)
- **Stable:** No

### 6. Heap Sort (`heap_sort_simple.py`)
- **Idea:** Builds a Max Heap, then repeatedly extracts the largest element and places it at the end.
- **Time Complexity:** O(n log n)
- **Space Complexity:** O(1)
- **Stable:** No

### 7. Recursive Bubble Sort (`recursive_bubble_sort.py`)
- **Idea:** Same logic as Bubble Sort, but implemented using recursion instead of an outer loop.
- **Time Complexity:** O(n²)
- **Space Complexity:** O(n) (recursion stack)
- **Stable:** Yes

### 8. Recursive Insertion Sort (`recursive_insertion_sort.py`)
- **Idea:** Same logic as Insertion Sort, but implemented using recursion instead of an outer loop.
- **Time Complexity:** O(n²)
- **Space Complexity:** O(n) (recursion stack)
- **Stable:** Yes

---

## 🗂️ Folder Structure

```
Sorting/
│
├── bubble_sort.py
├── selection_sort.py
├── insertion_sort.py
├── merge_sort.py
├── quick_sort.py
├── heap_sort_simple.py
├── recursive_bubble_sort.py
├── recursive_insertion_sort.py
└── README.md
```

---

## ⚙️ How to Run

1. Clone or download this repository
2. Navigate to the `Sorting/` folder
3. Run any file using:
   ```
   python filename.py
   ```
4. Enter the numbers separated by space when prompted

---

## 📊 Complexity Comparison Table

| Algorithm              | Best Case  | Average Case | Worst Case | Space   | Stable |
|------------------------|------------|---------------|------------|---------|--------|
| Bubble Sort            | O(n)       | O(n²)         | O(n²)      | O(1)    | Yes    |
| Selection Sort         | O(n²)      | O(n²)         | O(n²)      | O(1)    | No     |
| Insertion Sort         | O(n)       | O(n²)         | O(n²)      | O(1)    | Yes    |
| Merge Sort             | O(n log n) | O(n log n)    | O(n log n) | O(n)    | Yes    |
| Quick Sort             | O(n log n) | O(n log n)    | O(n²)      | O(log n)| No     |
| Heap Sort              | O(n log n) | O(n log n)    | O(n log n) | O(1)    | No     |
| Recursive Bubble Sort  | O(n)       | O(n²)         | O(n²)      | O(n)    | Yes    |
| Recursive Insertion Sort | O(n)     | O(n²)         | O(n²)      | O(n)    | Yes    |

---

## 🔗 Reference

- [Striver's A2Z DSA Sheet](https://takeuforward.org/strivers-a2z-dsa-course/strivers-a2z-dsa-course-sheet-2/)

---

## 👤 Author

**Kishore Reddy Gayam**
B.Tech CSE (AI/ML), Marwadi University
[GitHub Profile](https://github.com/kishorereddycse860-hub)
[LinkedIn Profile](https://www.linkedin.com/in/kishore-reddy-gayam-867254316/)

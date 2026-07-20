# Searching Algorithms

This folder contains Python implementations of common searching algorithms, solved as part of my DSA practice (following Striver's A2Z DSA Sheet).

---

## 📌 Algorithms Covered

### 1. Linear Search (`linear_search.py`)
- **Idea:** Checks every element one by one, starting from the first, until the target is found or the array ends.
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)
- **Use Case:** Works on both sorted and unsorted arrays.

### 2. Binary Search (`binary_search.py`)
- **Idea:** Repeatedly divides the search range in half by comparing the middle element with the target.
- **Time Complexity:** O(log n)
- **Space Complexity:** O(1) (iterative) / O(log n) (recursive)
- **Use Case:** Only works on a **sorted** array.

---

## 🗂️ Folder Structure

```
Searching/
│
├── linear_search.py
├── binary_search.py
└── README.md
```

---

## ⚙️ How to Run

1. Clone or download this repository
2. Navigate to the `Searching/` folder
3. Run any file using:
   ```
   python filename.py
   ```
4. Enter the numbers separated by space, and the target element to search, when prompted

---

## 📊 Complexity Comparison Table

| Algorithm      | Best Case | Average Case | Worst Case | Space   | Requires Sorted Array |
|----------------|-----------|---------------|------------|---------|------------------------|
| Linear Search  | O(1)      | O(n)          | O(n)       | O(1)    | No                     |
| Binary Search  | O(1)      | O(log n)      | O(log n)   | O(1)    | Yes                    |

---

## 🔗 Reference

- [Striver's A2Z DSA Sheet](https://takeuforward.org/strivers-a2z-dsa-course/strivers-a2z-dsa-course-sheet-2/)

---

## 👤 Author

**Kishore Reddy Gayam**
B.Tech CSE (AI/ML), Marwadi University
[GitHub Profile](https://github.com/kishorereddycse860-hub)
[LinkedIn Profile](https://www.linkedin.com/in/kishore-reddy-gayam-867254316/)

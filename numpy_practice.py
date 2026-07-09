# ================================================
# NumPy Practice — Simon's Data Science Journey
# Topic: NumPy Fundamentals
# ================================================

import numpy as np

# ── ARRAYS ──────────────────────────────────────

# 1D Array
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("1D Array:", a)

# 2D Array
b = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
print("2D Array:\n", b)
print("Shape:", b.shape)
print("Size:", b.size)
print("Dimensions:", b.ndim)

# ── OPERATIONS ──────────────────────────────────

a = np.array([1, 2, 3, 4, 5])
print("\nOriginal:", a)
print("x4:", a * 4)
print("Squared:", a ** 2)
print("+10:", a + 10)

# ── FUNCTIONS ───────────────────────────────────

data = np.array([23, 7, 45, 12, 67, 3, 89])
print("\nSum:", np.sum(data))
print("Mean:", np.mean(data))
print("Max:", np.max(data))
print("Min:", np.min(data))
print("Index of Max:", np.argmax(data))
print("Sorted:", np.sort(data))

# ── BOOLEAN FILTERING ───────────────────────────

a = np.array([15, 3, 22, 8, 41, 7, 19, 33, 5, 28])
print("\nValues > 20:", a[a > 20])
print("Mean of values > 20:", np.mean(a[a > 20]))

# ── INDEXING & SLICING ──────────────────────────

a = np.array([100, 200, 300, 400, 500, 600, 700, 800])
print("\nLast 3:", a[-3:])
print("Every other from index 1:", a[1::2])
print("Reversed:", a[::-1])

b = np.array([[1,  2,  3,  4],
              [5,  6,  7,  8],
              [9, 10, 11, 12]])
print("\nSecond row:", b[1, :])
print("Third column:", b[:, 2])
print("Top-right 2x2:\n", b[0:2, 2:4])
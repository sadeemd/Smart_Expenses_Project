# NumPy Basics 1 (Day 1)

## Overview
This notebook covers fundamental NumPy skills:
- Creating 1D and 2D arrays
- Understanding shapes and dtypes
- Indexing and slicing
- Fancy indexing
- Basic statistics (sum, mean)
- Axis operations (row/column sums)
- Practice problems + a small challenge function

## Files
- `notebook.ipynb` — Full practice and solutions

## Topics Covered
### 1) Arrays
- 1D array and 2D array creation using `np.array()`

### 2) Data Types
- `dtype` examples: `int64`, `float64`, `int16`

### 3) Indexing & Slicing
- Basic indexing: `a1[0]`, `a1[-1]`
- 2D indexing: `a2[row, col]`
- Slicing: `a1[1:4]`, `a1[::2]`

### 4) Fancy Indexing
- Selecting specific elements by index list

### 5) Stats & Axis
- `sum()` and `mean()`
- `axis=1` for rows, `axis=0` for columns

## Challenge
A function to return (avg, max, min) for any array:
- `stats(arr)`

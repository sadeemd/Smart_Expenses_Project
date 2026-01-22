# Week 1 Summary — Python Data Skills (NumPy + Pandas + Matplotlib)

**Week:** 1  
**Dates:** 2026-01-15 → 2026-01-21  
**Focus:** Practical Python + Data handling + Clean documentation

---

## Overview
This week was about building strong foundations in Python for data tasks. I practiced NumPy arrays and operations, worked with CSV files using Pandas, created simple plots using Matplotlib, and finished with a mini project that combines cleaning, analysis, and visualization.

---

## What I learned (1-page summary)
During Week 1, I improved my ability to work with data in Python in a practical way.  
I learned how to create and manipulate NumPy arrays (1D and 2D), control data types, use indexing and slicing, and calculate basic statistics like sum and mean. I also learned how broadcasting works and how vectorized operations can be faster than loops.

With Pandas, I learned how to read CSV files, inspect the dataset using `head()`, `info()`, and `describe()`, and handle missing values in a simple way. I practiced filtering data using conditions, sorting values, grouping by a column, and producing clean summary tables using aggregations such as sum, mean, and count.

In Matplotlib, I learned how to create simple line and bar charts, add titles and labels, enable grid, and save the figure as an image file. Finally, I completed a mini project where I cleaned a dataset, calculated key indicators, filtered results, and visualized one important insight.

By the end of the week, I feel more confident building small data analysis scripts and documenting my work in an organized GitHub-ready format.

---

## Daily Progress

### Day 1 — NumPy Basics 1 (Arrays + dtypes + indexing)
**Tasks:**
- Create 1D and 2D arrays
- Try different `dtype`
- Practice slicing and fancy indexing
- Compute `sum()` and `mean()`

**Deliverable:** `01_numpy_basics/notebook.ipynb`

---

### Day 2 — NumPy Basics 2 (Broadcasting + vectorization)
**Tasks:**
- Broadcasting between `(10,)` and `(10,1)`
- Use `where()`
- Use `clip()`
- Compare loop vs vector speed

**Practice:**
- Convert grades (0–100) into pass/fail using `>= 50`
- Create a small report: success rate

**Deliverable:** `01_numpy_basics/notebook.ipynb`

---

### Day 3 — Pandas Read CSV (read_csv + info/describe)
**Tasks:**
- Read CSV file
- Display `head()`
- Check `info()`
- Use `describe()`
- Handle missing values

**Practice:**
- Summary of `students.csv`
- Print Top 5 and Bottom 5 grades

**Deliverable:** `02_pandas_csv/students.csv + notebook.ipynb`

---

### Day 4 — Pandas Filtering + GroupBy
**Tasks:**
- Filter data by condition
- Sort with `sort_values()`
- Use `groupby()`
- Apply aggregations: sum/mean/count
- Produce a final clean table

**Practice:**
- Total expenses per category
- Compare 3 categories

**Deliverable:** `02_pandas_csv/notebook.ipynb`

---

### Day 5 — Matplotlib Basic Plot
**Tasks:**
- Create line plot from simple data
- Add title, xlabel, ylabel
- Enable grid
- Save `figure.png`

**Practice:**
- Plot expenses for 7 days
- Bar chart by category

**Deliverable:** `03_matplotlib/notebook.ipynb + figure.png`

---

### Day 6 — Mini Project (Quick Analysis)
**Tasks:**
- Choose a dataset (grades/sales/expenses)
- Clean the data
- Calculate indicators
- Apply filtering
- Create one plot

**Practice:**
- Write 5 result lines in `report.txt`
- Add Top 5 table

**Deliverable:** `04_mini_project/data.csv + notebook.ipynb + report.txt`

---

### Day 7 — Review + Documentation
**Tasks:**
- Clean variable names
- Remove repetition
- Reorder notebook cells
- Add Markdown explanations
- Write this README summary

**Deliverable:** `W1_summary/README.md`

---

## Common mistakes I faced (and fixes)

### 1) File path issues (File not found)
✅ **Fix:** Use `pathlib` and a base directory:
```python
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent

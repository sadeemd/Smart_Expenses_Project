# Week 3 — Day 16: Project Expenses (Clean CSV + Weekly Summary)

This task cleans the raw expenses dataset and produces:
1) A clean dataset (`clean_expenses.csv`)
2) A weekly net summary (`weekly_summary.csv`) using a signed amount approach

---

## Folder Structure

Smart_Expenses_Project/
└─ project/
   ├─ data/
   │  ├─ expenses.csv
   │  └─ clean_expenses.csv
   ├─ reports/
   │  └─ weekly_summary.csv
   └─ src/
      └─ Project_Expenses_cleaning.ipynb

---

## What This Notebook Does

### Cleaning
- Parse `date` into a proper datetime column
- Convert `amount` to numeric
- Handle missing values (fill text fields + drop rows missing `date` or `amount`)

### Feature Engineering
- `day_name`: day of the week
- `week`: week index starting from the first date in the dataset (Week 1, Week 2, ...)
- `is_weekend`: True if the day is Saturday/Sunday
- `signed_amount`: income as positive, expense as negative

### Reporting (Optional but included)
- Generate `weekly_summary.csv` with `net_total` per week

---

## How to Run

Open and run the notebook:

- `project/src/Project_Expenses_cleaning.ipynb`

The notebook reads from:
- `project/data/expenses.csv`

And writes outputs to:
- `project/data/clean_expenses.csv`
- `project/reports/weekly_summary.csv`

---

## Outputs

### 1) clean_expenses.csv
A cleaned dataset ready for analysis and dashboards.

### 2) weekly_summary.csv
A simple weekly net total report:
- `week`
- `net_total`

---

## Notes

- The `week` column is **not ISO week**. It is a **relative week index** starting from the first date in the dataset.
- `signed_amount` rule:
  - income → +amount
  - expense → -amount

# Linear Regression 2 — Feature Improvement + Metrics Comparison

## Goal
Improve a Linear Regression model by applying:
1) Simple category encoding (One-Hot Encoding)
2) Optional numeric scaling
3) Retraining the model
4) Comparing metrics before vs after
5) Saving the best model

## Dataset
File: `data.csv`

Required:
- Target column: `amount`
Optional:
- Categorical column: `category`

## Output Files
- `metrics_comparison.csv` (table of results)
- `best_linear_regression_model.joblib` (saved best model)

## Steps in the Notebook
1) Train a baseline Linear Regression model
2) Apply One-Hot Encoding for categorical columns
3) Apply Scaling for numeric columns (optional)
4) Compare MAE, RMSE, and R2 in a single table
5) Save the best-performing model

## How to Run
Open `notebook.ipynb` and run all cells from top to bottom.

## Deliverable
A clear comparison of metrics before/after feature improvements + saved best model.

# Day 9 — Train/Test Split + Metrics (MAE / MSE / R2)

This lab demonstrates the basic machine learning workflow:
1) Split the dataset into **Train** and **Test**
2) Train a simple **baseline model**
3) Train a real model (**Linear Regression**)
4) Evaluate both using **MAE, MSE, and R²**
5) Save results into a CSV file: `metrics.csv`

---

## Folder Contents

- `notebook.ipynb` → full code and outputs
- `metrics.csv` → evaluation results table (baseline vs model)

---

## Concepts Covered

### 1) Features (X) and Target (y)
- **X (Features):** input columns used for prediction  
- **y (Target):** the value we want to predict (label)

Example:
- Features: `day`, `type`
- Target: `amount`

---

### 2) Train/Test Split (80/20)
We split the dataset so the model learns from training data and is evaluated on unseen test data.

- **80% Train**
- **20% Test**

This is done using:

```python
train_test_split(X, y, test_size=0.2, random_state=42)

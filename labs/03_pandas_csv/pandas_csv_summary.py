import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
csv_path = BASE_DIR / "students.csv"

# 1) اقرأ ملف CSV
df = pd.read_csv(csv_path)

print("\n=== 2) head() ===")
print(df.head())

print("\n=== 3) info() ===")
print(df.info())

print("\n=== 4) describe() ===")
print(df.describe(include="all"))

print("\n=== Missing Values (Before) ===")
print(df.isna().sum())

# 5) معالجة missing values بشكل بسيط
# - للأعمدة الرقمية: نعوض بـ median
# - للأعمدة النصية: نعوض بـ mode (الأكثر تكراراً)

num_cols = df.select_dtypes(include="number").columns
cat_cols = df.select_dtypes(exclude="number").columns

for col in num_cols:
    df[col] = df[col].fillna(df[col].median())

for col in cat_cols:
    df[col] = df[col].fillna(df[col].mode().iloc[0])

print("\n=== Missing Values (After) ===")
print(df.isna().sum())

# إنشاء معدل درجات واضح للفرز
subjects = ["math", "english", "science"]
df["avg_score"] = df[subjects].mean(axis=1).round(2)

# طباعة Top 5 و Bottom 5
top5 = df.nlargest(5, "avg_score")[["student_id", "name", "avg_score"]]
bottom5 = df.nsmallest(5, "avg_score")[["student_id", "name", "avg_score"]]

print("\n=== Top 5 Highest avg_score ===")
print(top5.to_string(index=False))

print("\n=== Bottom 5 Lowest avg_score ===")
print(bottom5.to_string(index=False))

# جدول ملخص واضح (Summary Table)
summary = df[subjects + ["avg_score"]].agg(["mean", "min", "max"]).round(2)
print("\n=== Summary Table (mean/min/max) ===")
print(summary)

# حفظ النتائج بملفات
cleaned_path = BASE_DIR / "students_cleaned.csv"
report_path = BASE_DIR / "summary_stats.csv"

df.to_csv(cleaned_path, index=False)
summary.to_csv(report_path)

print("\nSaved:")
print(" -", cleaned_path.name)
print(" -", report_path.name)

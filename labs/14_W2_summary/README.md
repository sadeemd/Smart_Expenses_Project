# Week 2 Summary — Quick Comparison

## Overview
هذا الأسبوع طبّقت:
Prepare X,y → Split → Train → Evaluate → Compare → Save results

---

## Key Results (Numbers)

### Regression 1 (Baseline vs Linear Regression)
- baseline_mean: MAE=12.50, MSE=156.64, R2=-0.0025
- linear_regression: MAE=1.25, MSE=1.953, R2=0.9875
✅ Best: **linear_regression** (أعلى R2 وأقل MAE)

### Regression 2 (Feature Engineering)
- OneHot: MAE=656.98, RMSE=735.83, R2=0.86464
- OneHot + Scaling: MAE=846.70, RMSE=923.75, R2=0.78667
- Baseline (Numeric Only): MAE=1421.88, RMSE=1534.91, R2=0.41101
✅ Best: **OneHot Encoding** (أفضل R2 وأقل أخطاء)

### Classification (Hyperparameters)
- DecisionTree (max_depth=1..6): Accuracy=1.00
- LogisticRegression (C=0.01..100): Accuracy=1.00

---

## Best Picks (Why)
- Regression: **Linear Regression** فاز لأنه حسن النتائج مقارنة بالـ baseline بشكل واضح.
- Feature Engineering: **OneHot** فاز لأنه رفع R2 وخفّض الأخطاء أكثر من Scaling.
- Classification: بما أن النتائج متساوية، نختار الأبسط لتقليل overfitting:
  - DecisionTree max_depth=1 أو LogisticRegression C=0.01

---

## Strengths / Weaknesses (مختصر)
- Linear Regression: سريع وبسيط / يتأثر بالـ outliers وبالعلاقات غير الخطية.
- OneHot: يحسن التعامل مع الـ category / يزيد عدد الأعمدة.
- Decision Tree: قوي لغير الخطي / قد يعمل overfitting إذا العمق كبير.
- Logistic Regression: baseline جيد / يحتاج features مناسبة.

---

## 10-line Evaluation
1) ثبت عندي أساس تجهيز X,y.  
2) تعلمت baseline للمقارنة.  
3) Linear Regression تفوق بوضوح.  
4) OneHot رفع جودة regression.  
5) Scaling مو دائمًا مفيد.  
6) طبقت threshold للتصنيف.  
7) جرّبت hyperparameters.  
8) النتائج المثالية تحتاج تحقق أكبر.  
9) حفظت النتائج بملفات CSV.  
10) صار عندي workflow قابل للتكرار.

---

## Evidence Files
- metrics.csv
- metrics_comparison.csv
- compare.csv

---

## Results Image
ضع صورة واحدة داخل `W2_summary/` باسم `results.png`:
![Week 2 Results](results.png)

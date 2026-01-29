# Smart Expenses Project — CSV Template (Day 15)

This step creates the first data template for the project `expenses.csv`. The goal is to define a clean schema, enforce simple input rules, and keep categories consistent so analysis later becomes easy.

File location
`Smart_Expenses_Projectdataexpenses.csv`

## CSV Columns (Schema)
The CSV must contain these columns (same order)
- `date` (YYYY-MM-DD)
- `type` (`expense` or `income`)
- `category` (one of the fixed categories below)
- `amount` (positive number)
- `payment_method` (`cash`, `card`, `transfer`, `online`)
- `description` (short text)

Header example
`date,type,category,amount,payment_method,description`

## Fixed Categories (5)
Use ONLY these categories (same spelling)
- `Income`
- `Food`
- `Transport`
- `Bills`
- `Shopping`

## Input Rules
- `date` must be in `YYYY-MM-DD` format (example `2026-01-29`)
- `type` only `income` or `expense`
- `category` must match one of the 5 fixed categories
- `amount` positive number (example `15000` or `15000.0`)
- `payment_method` one of `cash`, `card`, `transfer`, `online`
- `description` short and clear (avoid commas if possible to keep CSV simple)

## Example Rows
```csv
date,type,category,amount,payment_method,description
2026-01-01,income,Income,1200000,transfer,Monthly salary
2026-01-02,expense,Food,18000,cash,Grocery items
2026-01-04,expense,Transport,8000,cash,Fuel

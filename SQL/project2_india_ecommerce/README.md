# 📦 SQL Project 2: India E-Commerce Orders Analysis

This project analyzes a large dataset of e-commerce orders from India using **SQL (SQLite)** to uncover meaningful insights such as product demand, shipping delays, and order trends.

> 🔍 **Goal:** Build practical SQL querying skills by answering real business questions using a transactional dataset.

---

## 📂 Dataset Overview

- **Filename:** `orders.csv`
- **Records:** 100,001 rows
- **Source:** Indian e-commerce order management system

| Field        | Description                      |
|--------------|----------------------------------|
| `rec_id`     | Unique row ID                    |
| `order_id`   | Unique identifier for the order  |
| `order_date` | Date when the order was placed   |
| `shipped_at` | Date when the order was shipped  |
| `prod_sku`   | Product SKU                      |
| `prod_qty`   | Quantity of the product ordered  |

---

## 🛠️ Table Schema in SQLite

```sql
CREATE TABLE orders (
    rec_id INTEGER,
    order_id TEXT,
    order_date TEXT,
    shipped_at TEXT,
    prod_sku TEXT,
    prod_qty INTEGER
);
```

---

## 🧠 Business Questions Answered with SQL

### 1️⃣ How many unique orders were placed?
```sql
SELECT COUNT(DISTINCT order_id) AS total_orders FROM orders;
```
**Result:** 99,797 unique orders

---

### 2️⃣ Which products were ordered the most?
```sql
SELECT prod_sku, SUM(prod_qty) AS total_units
FROM orders
GROUP BY prod_sku
ORDER BY total_units DESC
LIMIT 10;
```
**Top 3 Products:**

| Product SKU | Units Ordered |
|-------------|--------------|
| IT-PB11K    | 1182         |
| 1437930     | 942          |
| 1414285     | 840          |

---

### 3️⃣ How many orders were placed each month?
```sql
SELECT 
  STRFTIME('%Y-%m', order_date) AS month,
  COUNT(DISTINCT order_id) AS order_count
FROM orders
GROUP BY month
ORDER BY month;
```
**Insight:** Orders were consistent month-over-month, peaking in Q4.

---

### 4️⃣ What’s the average number of items per order?
```sql
SELECT AVG(items_per_order) AS avg_items
FROM (
  SELECT order_id, SUM(prod_qty) AS items_per_order
  FROM orders
  GROUP BY order_id
);
```
**Result:** 1.26 items/order on average

---

### 5️⃣ What’s the average shipping time?
```sql
SELECT 
  ROUND(AVG(JULIANDAY(shipped_at) - JULIANDAY(order_date)), 2) AS avg_shipping_days
FROM orders
WHERE shipped_at IS NOT NULL AND order_date IS NOT NULL;
```
**Result:** 2.68 days to ship on average

---

## ✅ Key Learnings

- Writing aggregate queries, subqueries, and date-based transformations
- Using `GROUP BY`, `ORDER BY`, and `LIMIT` for summarization
- Handling NULLs and datetime calculations with `JULIANDAY()`

---

## 🧰 Tools Used

- SQLite (via CLI)
- VS Code for development
- Git & GitHub for version control

---

## 👨‍💻 Author

**Tiwari Shivanand**  
🎓 Aspiring Data Analyst | Python • SQL • R  
🔗 [GitHub: @vinnuverse](https://github.com/vinnuverse)  
🔗 [LinkedIn](https://www.linkedin.com/in/tiwari-shivanand-mystore)

---

## 🗂️ Project Status

- ✅ Completed
- 🗃️ Live on GitHub
- 🔄 Ready for LinkedIn post
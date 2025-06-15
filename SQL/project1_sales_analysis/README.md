# 🧾 SQL Project 1: Sales Database Analysis

This SQL project demonstrates retail sales analysis using a small relational database built with **SQLite**. The goal is to analyze customer behavior, product performance, and sales trends.

---

## 🧱 Database Structure 

Data File - [https://docs.google.com/spreadsheets/d/1AwrdP5DyT0oBwiUP8ekNMWP_X7chWMBnvVjj_C1BQMQ/edit?gid=1490785302#gid=1490785302](url)

Three tables were created for this project:

### 1. `customers`

| customer_id | name  | country |
|-------------|-------|---------|
| 1           | Aditi | India   |
| 2           | Raj   | USA     |
| 3           | Emma  | UK      |

### 2. `products`

| product_id | name         | category     | price  |
|------------|--------------|--------------|--------|
| 1          | Laptop       | Electronics  | 60000  |
| 2          | Headphones   | Electronics  | 2000   |
| 3          | Office Chair | Furniture    | 7000   |

### 3. `orders`

| order_id | customer_id | product_id | quantity | order_date |
|----------|-------------|------------|----------|------------|
| 1        | 1           | 1          | 1        | 2024-06-01 |
| 2        | 1           | 2          | 2        | 2024-06-03 |
| 3        | 2           | 3          | 1        | 2024-06-05 |
| 4        | 3           | 1          | 1        | 2024-06-06 |
| 5        | 2           | 2          | 1        | 2024-06-07 |

---

## 📊 Key SQL Queries & Insights

### 1. 💰 Total Revenue by Product

```sql
SELECT 
    p.name AS product,
    SUM(o.quantity * p.price) AS total_revenue
FROM orders o
JOIN products p ON o.product_id = p.product_id
GROUP BY p.name
ORDER BY total_revenue DESC;
2. 🌍 Number of Orders per Country
sql
Copy
Edit
SELECT 
    c.country,
    COUNT(o.order_id) AS total_orders
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
GROUP BY c.country;
3. 👤 Customer Purchase Summary
sql
Copy
Edit
SELECT 
    c.name,
    COUNT(o.order_id) AS orders_count,
    SUM(o.quantity * p.price) AS total_spent
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN products p ON o.product_id = p.product_id
GROUP BY c.name
ORDER BY total_spent DESC;
4. 📅 Monthly Sales Trend
sql
Copy
Edit
SELECT 
    STRFTIME('%Y-%m', order_date) AS month,
    SUM(o.quantity * p.price) AS revenue
FROM orders o
JOIN products p ON o.product_id = p.product_id
GROUP BY month;
5. 📦 Most Popular Product
sql
Copy
Edit
SELECT 
    p.name,
    SUM(o.quantity) AS total_units_sold
FROM orders o
JOIN products p ON o.product_id = p.product_id
GROUP BY p.name
ORDER BY total_units_sold DESC;
🛠️ Tools Used
SQLite3 – local SQL engine

VS Code – code editing

SQLite Extension for VS Code – DB browser

Pure SQL – queries and joins

📌 Author
Tiwari Shivanand
🔗 GitHub
🔗 LinkedIn

💡 Stay tuned for upcoming SQL projects: HR analytics, fraud detection, product behavior, and more!


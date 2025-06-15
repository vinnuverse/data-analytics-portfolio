# 🇮🇳 SQL Project 2: India E-Commerce Orders Analysis

This project analyzes real-world Indian e-commerce order data using **SQLite**. It showcases key metrics like order volume, best-selling SKUs, shipping times, and purchasing behavior across thousands of transactions.

---

## 📦 Dataset Overview

The dataset (`orders.csv`) contains over 100,000+ historical e-commerce order records from India.  
It includes details such as:

| Column       | Description                      |
|--------------|----------------------------------|
| `rec_id`     | Unique row ID                    |
| `order_id`   | Order identifier                 |
| `order_date` | Date the order was placed        |
| `shipped_at` | Date the order was shipped       |
| `prod_sku`   | Product SKU (stock keeping unit) |
| `prod_qty`   | Quantity ordered                 |

---

## 🧱 Database Schema

```sql
CREATE TABLE orders (
    rec_id INTEGER,
    order_id TEXT,
    order_date TEXT,
    shipped_at TEXT,
    prod_sku TEXT,
    prod_qty INTEGER
);

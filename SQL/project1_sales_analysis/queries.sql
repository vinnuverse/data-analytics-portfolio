-- 1. Total Revenue by Product
SELECT 
    p.name AS product,
    SUM(o.quantity * p.price) AS total_revenue
FROM orders o
JOIN products p ON o.product_id = p.product_id
GROUP BY p.name
ORDER BY total_revenue DESC;

-- 2. Number of Orders per Country
SELECT 
    c.country,
    COUNT(o.order_id) AS total_orders
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
GROUP BY c.country
ORDER BY total_orders DESC;

-- 3. Customer Purchase Summary
SELECT 
    c.name,
    COUNT(o.order_id) AS orders_count,
    SUM(o.quantity * p.price) AS total_spent
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN products p ON o.product_id = p.product_id
GROUP BY c.name
ORDER BY total_spent DESC;

-- 4. Monthly Sales Trend
SELECT 
    STRFTIME('%Y-%m', order_date) AS month,
    SUM(o.quantity * p.price) AS revenue
FROM orders o
JOIN products p ON o.product_id = p.product_id
GROUP BY month
ORDER BY month;

-- 5. Most Popular Product by Quantity Sold
SELECT 
    p.name,
    SUM(o.quantity) AS total_units_sold
FROM orders o
JOIN products p ON o.product_id = p.product_id
GROUP BY p.name
ORDER BY total_units_sold DESC;

-- 1. Total Orders
SELECT COUNT(DISTINCT order_id) AS total_orders FROM orders;

-- 2. Top 10 SKUs
SELECT prod_sku, SUM(prod_qty) AS total_units_ordered
FROM orders
GROUP BY prod_sku
ORDER BY total_units_ordered DESC
LIMIT 10;

-- 3. Monthly Order Volume
SELECT STRFTIME('%Y-%m', order_date) AS month, COUNT(DISTINCT order_id) AS orders_count
FROM orders
GROUP BY month
ORDER BY month;

-- 4. Average Items per Order
SELECT AVG(items_per_order) AS avg_items_per_order FROM (
    SELECT order_id, SUM(prod_qty) AS items_per_order
    FROM orders
    GROUP BY order_id
);

-- 5. Average Shipping Time
SELECT ROUND(AVG(JULIANDAY(shipped_at) - JULIANDAY(order_date)), 2) AS avg_shipping_days
FROM orders
WHERE shipped_at IS NOT NULL AND order_date IS NOT NULL;

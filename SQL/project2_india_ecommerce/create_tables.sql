DROP TABLE IF EXISTS orders;

CREATE TABLE orders (
    rec_id INTEGER,
    order_id TEXT,
    order_date TEXT,
    shipped_at TEXT,
    prod_sku TEXT,
    prod_qty INTEGER
);

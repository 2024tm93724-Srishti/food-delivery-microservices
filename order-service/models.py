import sqlite3

conn = sqlite3.connect("orders.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    order_id TEXT,
    customer_id TEXT,
    restaurant_id TEXT,
    item_name TEXT,
    status TEXT
)
""")

conn.commit()
conn.close()

print("Orders DB created!")
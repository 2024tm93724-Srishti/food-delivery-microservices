import sqlite3

conn = sqlite3.connect("payments.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS payments (
    payment_id TEXT,
    order_id TEXT,
    amount INTEGER,
    status TEXT
)
""")

conn.commit()
conn.close()

print("Payments DB created!")
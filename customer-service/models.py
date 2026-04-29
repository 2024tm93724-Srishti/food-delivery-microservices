import sqlite3

conn = sqlite3.connect("customers.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
    customer_id TEXT PRIMARY KEY,
    name TEXT,
    email TEXT,
    phone TEXT
)
""")

conn.commit()
conn.close()

print("Database created successfully!")
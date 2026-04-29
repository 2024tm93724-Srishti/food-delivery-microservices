import sqlite3

conn = sqlite3.connect("restaurant.db")
cursor = conn.cursor()

# Restaurants
cursor.execute("""
CREATE TABLE IF NOT EXISTS restaurants (
    id TEXT,
    name TEXT,
    city TEXT,
    is_open INTEGER
)
""")

# Menu
cursor.execute("""
CREATE TABLE IF NOT EXISTS menu (
    item_id TEXT,
    restaurant_id TEXT,
    name TEXT,
    price INTEGER,
    is_available INTEGER
)
""")

# Sample Data
cursor.execute("INSERT INTO restaurants VALUES ('1','Pizza Hut','Bangalore',1)")
cursor.execute("INSERT INTO restaurants VALUES ('2','Dominos','Bangalore',1)")

cursor.execute("INSERT INTO menu VALUES ('101','1','Margherita Pizza',200,1)")
cursor.execute("INSERT INTO menu VALUES ('102','1','Veg Supreme',300,1)")
cursor.execute("INSERT INTO menu VALUES ('201','2','Cheese Burst',250,1)")

conn.commit()
conn.close()

print("Restaurant DB created!")
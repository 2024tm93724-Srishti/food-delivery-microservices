from flask import Flask, request, jsonify
import sqlite3
import requests
import uuid

app = Flask(__name__)

CUSTOMER_URL = "http://localhost:5001/v1/customers"
RESTAURANT_URL = "http://localhost:5002/v1/menu"

def get_db():
    return sqlite3.connect("orders.db")

# ✅ Place Order
@app.route("/v1/orders", methods=["POST"])
def create_order():
    data = request.json

    customer_id = data.get("customer_id")
    restaurant_id = data.get("restaurant_id")
    item_name = data.get("item_name")

    # 🔍 Validate Customer
    customers = requests.get(CUSTOMER_URL).json()
    if not any(c[0] == customer_id for c in customers):
        return jsonify({"error": "Invalid customer"}), 400

    # 🔍 Validate Menu Item
    menu = requests.get(f"{RESTAURANT_URL}/{restaurant_id}").json()
    item = next((m for m in menu if m[2] == item_name and m[4] == 1), None)

    if not item:
        return jsonify({"error": "Item not available"}), 400

    # ✅ Create Order
    order_id = str(uuid.uuid4())

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO orders VALUES (?,?,?,?,?)",
        (order_id, customer_id, restaurant_id, item_name, "PLACED")
    )

    conn.commit()
    conn.close()

    return jsonify({
        "message": "Order placed",
        "order_id": order_id
    })

# ✅ Get Orders
@app.route("/v1/orders", methods=["GET"])
def get_orders():
    conn = get_db()
    cursor = conn.cursor()

    data = cursor.execute("SELECT * FROM orders").fetchall()
    return jsonify(data)

if __name__ == "__main__":
    app.run(port=5003, debug=True)
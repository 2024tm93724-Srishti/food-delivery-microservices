from flask import Flask, request, jsonify
import sqlite3
import uuid

app = Flask(__name__)

def get_db():
    return sqlite3.connect("customers.db")

@app.route("/v1/customers", methods=["POST"])
def create_customer():
    data = request.json
    conn = get_db()
    cursor = conn.cursor()

    customer_id = str(uuid.uuid4())

    cursor.execute(
        "INSERT INTO customers VALUES (?, ?, ?, ?)",
        (customer_id, data["name"], data["email"], data["phone"])
    )

    conn.commit()

    return jsonify({
        "message": "Customer created",
        "customer_id": customer_id
    })

@app.route("/v1/customers", methods=["GET"])
def get_customers():
    conn = get_db()
    cursor = conn.cursor()

    customers = cursor.execute("SELECT * FROM customers").fetchall()

    return jsonify(customers)

if __name__ == "__main__":
    app.run(port=5001, debug=True)
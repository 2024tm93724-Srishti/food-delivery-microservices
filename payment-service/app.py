from flask import Flask, request, jsonify
import sqlite3
import uuid

app = Flask(__name__)

def get_db():
    return sqlite3.connect("payments.db")

# ✅ Make Payment
@app.route("/v1/payments", methods=["POST"])
def make_payment():
    data = request.json

    order_id = data.get("order_id")
    amount = data.get("amount")

    if not order_id:
        return jsonify({"error": "Order ID required"}), 400

    payment_id = str(uuid.uuid4())

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO payments VALUES (?,?,?,?)",
        (payment_id, order_id, amount, "SUCCESS")
    )

    conn.commit()
    conn.close()

    return jsonify({
        "message": "Payment successful",
        "payment_id": payment_id
    })

# ✅ Get Payments
@app.route("/v1/payments", methods=["GET"])
def get_payments():
    conn = get_db()
    cursor = conn.cursor()

    data = cursor.execute("SELECT * FROM payments").fetchall()
    return jsonify(data)

if __name__ == "__main__":
    app.run(port=5004, debug=True)
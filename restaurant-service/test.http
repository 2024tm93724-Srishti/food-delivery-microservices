from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

def get_db():
    return sqlite3.connect("restaurant.db")

# ✅ Get all restaurants
@app.route("/v1/restaurants", methods=["GET"])
def get_restaurants():
    conn = get_db()
    cursor = conn.cursor()

    data = cursor.execute("SELECT * FROM restaurants").fetchall()
    return jsonify(data)

# ✅ Get menu for restaurant
@app.route("/v1/menu/<restaurant_id>", methods=["GET"])
def get_menu(restaurant_id):
    conn = get_db()
    cursor = conn.cursor()

    data = cursor.execute(
        "SELECT * FROM menu WHERE restaurant_id=?",
        (restaurant_id,)
    ).fetchall()

    return jsonify(data)

if __name__ == "__main__":
    app.run(port=5002, debug=True)
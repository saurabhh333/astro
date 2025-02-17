from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_jwt_extended import JWTManager, create_access_token
import sqlite3
from astrology import calculate_lagna, vimshottari_dasa, kp_astrology
from transits import get_transits

app = Flask(__name__)
CORS(app)
app.config['JWT_SECRET_KEY'] = 'your_secret_key'
jwt = JWTManager(app)

conn = sqlite3.connect("users.db", check_same_thread=False)
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)")
conn.commit()

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    username, password = data["username"], data["password"]
    user = cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password)).fetchone()
    if user:
        return jsonify(access_token=create_access_token(identity=username))
    return jsonify({"msg": "Invalid Credentials"}), 401

@app.route("/lagna_chart", methods=["POST"])
def lagna_chart():
    return jsonify(calculate_lagna(request.json))

@app.route("/vimshottari_dasa", methods=["POST"])
def vimshottari():
    return jsonify(vimshottari_dasa(request.json))

@app.route("/kp_astrology", methods=["POST"])
def kp_chart():
    return jsonify(kp_astrology(request.json))

@app.route("/transits", methods=["POST"])
def transits():
    return jsonify(get_transits(request.json))

if __name__ == "__main__":
    app.run(debug=True)

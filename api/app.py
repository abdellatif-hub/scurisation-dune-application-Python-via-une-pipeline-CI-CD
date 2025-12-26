from flask import Flask, request
import sqlite3
import os
import bcrypt

app = Flask(__name__)

# Secret sécurisé via variable d’environnement
API_KEY = os.getenv("API_KEY")

# ========================
# Auth sécurisé
# ========================
@app.route("/auth", methods=["POST"])
def auth():
    data = request.get_json(force=True)
    username = data.get("username", "")
    password = data.get("password", "")

    if not username or not password:
        return {"error": "Invalid input"}, 400

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
    row = cursor.fetchone()

    if row and bcrypt.checkpw(password.encode(), row[0]):
        return {"status": "authenticated"}
    return {"status": "denied"}

# ========================
# Chiffrement fort
# ========================
@app.route("/encrypt", methods=["POST"])
def encrypt():
    text = request.json.get("text", "")
    hashed = bcrypt.hashpw(text.encode(), bcrypt.gensalt())
    return {"hash": hashed.decode()}

# ========================
# Lecture fichier sécurisée
# ========================
@app.route("/file", methods=["POST"])
def read_file():
    filename = request.json.get("filename", "")
    if ".." in filename or filename.startswith("/"):
        return {"error": "Access denied"}, 403

    if not os.path.exists(filename):
        return {"error": "File not found"}, 404

    with open(filename, "r") as f:
        return {"content": f.read()}

@app.route("/hello", methods=["GET"])
def hello():
    return {"message": "Secure DevSecOps Application"}

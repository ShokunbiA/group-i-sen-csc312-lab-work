"""
Group I - SEN CSC312 Lab Work (Web Application Development)
Flask app: homepage, signup with validation, MySQL, password hashing.

Ayodele Samuel Adebayo: Project setup & Flask init — ensure Flask is installed (see requirements.txt)
and the app is initialised below.
"""

import os
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
import mysql.connector
from mysql.connector import Error

# ---------------------------------------------------------------------------
# Ayodele Samuel Adebayo: Project setup & Flask init — initialise Flask here.
# ---------------------------------------------------------------------------
app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-secret-key-change-in-production")

# ---------------------------------------------------------------------------
# Shokunbi Abdulfatah Ayodele: Flask–MySQL connection — DB config and get_db_connection().
# ---------------------------------------------------------------------------
DB_CONFIG = {
    "host": os.environ.get("MYSQL_HOST", "localhost"),
    "user": os.environ.get("MYSQL_USER", "root"),
    "password": os.environ.get("MYSQL_PASSWORD", ""),
    "database": os.environ.get("MYSQL_DATABASE", "group1_lab_db"),
}


def get_db_connection():
    """Create and return a MySQL connection."""
    try:
        return mysql.connector.connect(**DB_CONFIG)
    except Error as e:
        print(f"Database connection error: {e}")
        return None


@app.route("/")
def index():
    """Homepage."""
    return render_template("index.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    """Signup: GET shows form, POST validates and stores user (hashed password)."""
    if request.method == "GET":
        return render_template("signup.html")

    # -----------------------------------------------------------------------
    # Ukwesa Kelvin: Form validation & signup route — validate request.form.
    # -----------------------------------------------------------------------
    username = request.form.get("username", "").strip()
    password = request.form.get("password", "")

    if not username:
        return render_template("signup.html", error="Username is required."), 400
    if len(username) < 3 or len(username) > 255:
        return render_template("signup.html", error="Username must be 3–255 characters."), 400
    if not password:
        return render_template("signup.html", error="Password is required."), 400
    if len(password) < 8:
        return render_template("signup.html", error="Password must be at least 8 characters."), 400

    # -----------------------------------------------------------------------
    # Adeleke Adegoke: Password hashing — hash before storing in DB.
    # -----------------------------------------------------------------------
    password_hash = generate_password_hash(password, method="scrypt")

    # -----------------------------------------------------------------------
    # Shokunbi Abdulfatah Ayodele: Flask–MySQL connection — insert into tbl_user.
    # -----------------------------------------------------------------------
    conn = get_db_connection()
    if not conn:
        return render_template("signup.html", error="Database unavailable. Try again later."), 503

    try:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO tbl_user (username, password) VALUES (%s, %s)",
            (username, password_hash),
        )
        conn.commit()
        cursor.close()
        conn.close()
        return render_template("signup.html", success=f"Account created for {username}. You can sign in.")
    except Error as e:
        if e.errno == 1062:  # duplicate entry
            return render_template("signup.html", error="Username already taken."), 400
        print(f"Database error: {e}")
        return render_template("signup.html", error="Could not create account. Try again."), 500
    finally:
        if conn and conn.is_connected():
            conn.close()


# ---------------------------------------------------------------------------
# Joshua Asiribo: Integration & testing — run app, test signup flow end-to-end.
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)

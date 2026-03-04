"""
Group I - SEN CSC312 Lab Work (Web Application Development)
Flask app: homepage, signup, MySQL, password hashing.

Ayodele Samuel Adebayo: Project setup & Flask init — ensure Flask is installed (see requirements.txt)
and the app is initialised below.
"""

from flask import Flask, render_template, request, jsonify
from flask_mysqldb import MySQL 
import mysql.connector
from mysql.connector import Error
from flask import current_app
from werkzeug.security import generate_password_hash

# ---------------------------------------------------------------------------
# Ayodele Samuel Adebayo: Project setup & Flask init — initialise Flask here.
# ---------------------------------------------------------------------------
app = Flask(__name__)
app.secret_key = "change-this-in-production"
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = ''
app.config['MYSQL_PORT'] = 3306

# ---------------------------------------------------------------------------
def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host=current_app.config['MYSQL_HOST'],
            user=current_app.config['MYSQL_USER'],
            password=current_app.config['MYSQL_PASSWORD'],
            database=current_app.config['MYSQL_DB'],
            port=current_app.config.get('MYSQL_PORT', 3306),
            autocommit=False
        )

        return connection

    except Error as e:
        print(f"Connection error: {e}")
        return None
    
# Shokunbi Abdulfatah Ayodele: Flask–MySQL connection
# Add: import mysql.connector (and Error from mysql.connector).
# Add: DB config (host, user, password, database) and a function get_db_connection()
# that returns a MySQL connection. Connect Flask to MySQL using mysql.connector.
# ---------------------------------------------------------------------------

@app.route("/")
def index():
    """Homepage — renders index.html."""
    return render_template("index.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    """Signup: GET shows form; POST should validate, hash password, and save to DB."""
    if request.method == "GET":
        return render_template("signup.html")

    # -----------------------------------------------------------------------
    # Ukwesa Kelvin: Form validation & signup route
    # Get username and password from request.form. Validate (e.g. required,
    # min length). If invalid, return render_template("signup.html", error="...")
    # with appropriate status code. Only proceed to DB when valid.
    # -----------------------------------------------------------------------

    # -----------------------------------------------------------------------
    # Adeleke Adegoke: Password hashing
    # Before storing, hash the password using werkzeug.security.generate_password_hash.
    # Store only the hashed value in the database, never the plain password.
    # -----------------------------------------------------------------------

    # -----------------------------------------------------------------------
@app.route("/createuser", methods=["POST"])
def createUser():
    connection = get_db_connection()

    if not connection:
        return jsonify({"error": "Database connection failed"}), 500

    try:
        data = request.json
        username = data.get("username")
        password = data.get("password")

        # Basic validation
        if not username or not password:
            return jsonify({"error": "Username and password are required"}), 400

        cursor = connection.cursor()

        # 1️⃣ Check if user already exists
        cursor.execute(
            "SELECT username FROM tbl_user WHERE username = %s",
            (username,)
        )
        user = cursor.fetchone()

        if user:
            return jsonify({"error": f"{username} already taken"}), 400

        # 2️⃣ Insert new user
        cursor.execute(
            "INSERT INTO tbl_user (username, password) VALUES (%s, %s)",
            (username, generate_password_hash(password))
        )

        connection.commit()  # Commit the transaction

        return jsonify({"message": "User created successfully"}), 201

    except Exception as e:
        if connection:
            connection.rollback()  # Rollback on error
        return jsonify({"error": str(e)}), 500

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
 
    # Shokunbi Abdulfatah Ayodele: Flask–MySQL connection
    # Use get_db_connection() to get a connection, then INSERT into tbl_user
    # (username, password). Use the hashed password. Handle duplicate username
    # (e.g. show "Username already taken"). Close the connection when done.
    # -----------------------------------------------------------------------

    # Placeholder until the above is implemented:
    return render_template(
        "signup.html",
        error="Signup not implemented yet — add validation, hashing, and DB insert (see comments in app.py).",
    ), 501

# ---------------------------------------------------------------------------
# Joshua Asiribo: Integration & testing
# After all members have added their code, run: python app.py
# Test: open homepage, go to signup, submit username and password, confirm
# the user is stored in MySQL (e.g. SELECT * FROM tbl_user;). Fix any bugs.
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True)

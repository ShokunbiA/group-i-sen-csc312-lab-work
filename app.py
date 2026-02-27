"""
Group I - SEN CSC312 Lab Work (Web Application Development)
Flask app: homepage, signup, MySQL, password hashing.

Ayodele Samuel Adebayo: Project setup & Flask init — ensure Flask is installed (see requirements.txt)
and the app is initialised below.
"""

from flask import Flask, render_template, request

# ---------------------------------------------------------------------------
# Ayodele Samuel Adebayo: Project setup & Flask init — initialise Flask here.
# ---------------------------------------------------------------------------
app = Flask(__name__)
app.secret_key = "change-this-in-production"

# ---------------------------------------------------------------------------
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

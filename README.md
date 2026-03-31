# Group I - SEN CSC312 Lab Work

**Web Application Development** 
Flask app with homepage, signup, MySQL, and password hashing.

## Group members

| Name | Matric | Department | Admission type | Task area |
|------|--------|------------|----------------|-----------|
| Shokunbi Abdulfatah Ayodele | 2025/B/SENG/0422 | Software Engineering | Direct Entry | Flask–MySQL connection |
| OMALE JEREMIAH OGWUCHE | 2024/A/SENG/0160 | Software Engineering | UTME | Homepage (index.html) |
| Wisdom Jonathan | 2024/C/SENG/0763 | Software Engineering | Direct Entry | Signup page (signup.html) |
| Ukwesa Kelvin | 2025/A/SENG/0394 | Software Engineering | Direct Entry | Form validation & signup route |
| Ojo Abiola Victoria | 2024/B/SENG/0255 | Software Engineering | Direct Entry | MySQL table creation script |
| Adeleke Adegoke | 2024/B/SENG/0215 | Software Engineering | Direct Entry | Password hashing |
| Joshua Asiribo | 2024/A/SENG/0009 | Software Engineering | UTME | Integration & testing |
| Oluwatobi Ogunfowora | 2024/C/SENG/0735 | Software Engineering | Direct Entry | Documentation & submission (with Johnson) |

## Where to add your work

Each file has comments naming the person and task. Use them as a guide:

| Task | File | Owner |
|------|------|--------|
| Project setup & Flask init | `app.py` (top) | Ayodele Samuel Adebayo |
| Homepage | `templates/index.html` | OMALE JEREMIAH OGWUCHE |
| Signup page | `templates/signup.html` | Wisdom Jonathan |
| Form validation & signup route | `app.py` (signup route) | Ukwesa Kelvin |
| MySQL table script | `database/create_tables.sql` | Ojo Abiola Victoria |
| Flask–MySQL connection | `app.py` (DB config & insert) | Shokunbi Abdulfatah Ayodele |
| Password hashing | `app.py` (signup route) | Adeleke Adegoke |
| Integration & testing | Run app, test signup flow | Joshua Asiribo |
| Documentation & submission | README, final deliverables | Oluwatobi Ogunfowora, Johnson Olakunle Oluwasegun |

## Submission deliverables

- `app.py` — Flask application
- `templates/index.html` — Homepage
- `templates/signup.html` — Signup form
- `database/create_tables.sql` — MySQL table creation script

## Total setup: run and test

Follow these steps in order to get the project running and test it.

### 1. Clone the repository

```bash
git clone <repository-url>
cd group-i-sen-csc312-lab-work
```

Replace `<repository-url>` with your actual repo URL (e.g. `https://github.com/username/group-i-sen-csc312-lab-work.git`). Use your actual folder name if different (e.g. `group-1-sen-csc312-lab-work`).

### 2. Python environment

```bash
python3 -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. MySQL: install, create database, and table

- Install and start MySQL. **Full guide:** [DATABASE_SETUP.md](DATABASE_SETUP.md).
- Create the database and `tbl_user` table:

```bash
mysql -u root -p < database/create_tables.sql
```

(Use `mysql -u root < database/create_tables.sql` if root has no password.) Or run the script in MySQL Workbench.

### 4. Database config (optional)

The app connects with:

- **Host:** `localhost`
- **User:** `root`
- **Password:** *(empty by default)*
- **Database:** `group1_lab_db`

If your MySQL root user has a password, set it before running the app:

```bash
export MYSQL_PASSWORD=yourpassword    # macOS/Linux
# Windows CMD: set MYSQL_PASSWORD=yourpassword
# Windows PowerShell: $env:MYSQL_PASSWORD="yourpassword"
```

To use a different host, user, or database, set: `MYSQL_HOST`, `MYSQL_USER`, `MYSQL_DATABASE`. See [DATABASE_SETUP.md](DATABASE_SETUP.md) for details.

### 5. Run the app

From the project folder (with venv activated):

```bash
python app.py
```

You should see something like: `Running on http://127.0.0.1:5000`.

### 6. Test the project

1. **Homepage:** Open http://127.0.0.1:5000 in a browser. You should see the welcome page and a “Sign Up” link.
2. **Sign up:** Click “Sign Up”, enter a username (e.g. `testuser`) and password (at least 8 characters), then submit.
3. **Success:** You should see a success message (e.g. “Account created for testuser”).
4. **Optional — verify in MySQL:** Check that the user was stored:

   ```bash
   mysql -u root -p -e "USE group1_lab_db; SELECT id, username, created_at FROM tbl_user;"
   ```

   You should see your test user. The password is stored hashed, not in plain text.
5. **Duplicate username:** Try signing up again with the same username; you should see “Username already taken”.
6. **Validation:** Try submitting an empty username or a password shorter than 8 characters; you should see the corresponding error messages.

## Features

- **Homepage:** Bootstrap layout, link to signup.
- **Signup:** Username and password form; validation via `request.form`.
- **Database:** MySQL table `tbl_user` (username, hashed password).
- **Security:** Passwords hashed with Werkzeug (scrypt) before storage.

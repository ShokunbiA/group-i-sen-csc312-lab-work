# Group I - SEN CSC312 Lab Work

**Web Application Development** 
Flask app with homepage, signup, MySQL, and password hashing.

## Group members

| Name | Matric | Department | Admission type | Task area |
|------|--------|------------|----------------|-----------|
| Ayodele Samuel Adebayo | 2023/A/SENG/0086 | Software Engineering | UTME | Project setup & Flask init |
| OMALE JEREMIAH OGWUCHE | 2024/A/SENG/0160 | Software Engineering | UTME | Homepage (index.html) |
| Wisdom Jonathan | 2024/C/SENG/0763 | Software Engineering | Direct Entry | Signup page (signup.html) |
| Ukwesa Kelvin | 2025/A/SENG/0394 | Software Engineering | Direct Entry | Form validation & signup route |
| Ojo Abiola Victoria | 2024/B/SENG/0255 | Software Engineering | Direct Entry | MySQL table creation script |
| Shokunbi Abdulfatah Ayodele | 2025/B/SENG/0422 | Software Engineering | Direct Entry | Flask–MySQL connection |
| Adeleke Adegoke | 2024/B/SENG/0215 | Software Engineering | Direct Entry | Password hashing |
| Joshua Asiribo | 2024/A/SENG/0009 | Software Engineering | UTME | Integration & testing |
| Oluwatobi Ogunfowora | 2024/C/SENG/0735 | Software Engineering | Direct Entry | Documentation & submission |

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
| Documentation & submission | README, final deliverables | Oluwatobi Ogunfowora |

## Submission deliverables

- `app.py` — Flask application
- `templates/index.html` — Homepage
- `templates/signup.html` — Signup form
- `database/create_tables.sql` — MySQL table creation script

## Setup

### 1. Clone the repository

```bash
git clone <repository-url>
cd group-1-sen-csc312-lab-work
```

Replace `<repository-url>` with your actual repo URL (e.g. `https://github.com/username/group-1-sen-csc312-lab-work.git`).

### 2. Python environment

```bash
python3 -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. MySQL

- Install MySQL and start the server.
- **Full guide for the team:** see [DATABASE_SETUP.md](DATABASE_SETUP.md).
- Create the database and table:

```bash
mysql -u root -p < database/create_tables.sql
```

Or run the contents of `database/create_tables.sql` in MySQL Workbench / CLI.

### 4. Run

```bash
python app.py
```

Open http://127.0.0.1:5000 — homepage; use “Sign Up” for registration.

## Features

- **Homepage:** Bootstrap layout, link to signup.
- **Signup:** Username and password form; validation via `request.form`.
- **Database:** MySQL table `tbl_user` (username, hashed password).
- **Security:** Passwords hashed with Werkzeug (scrypt) before storage.

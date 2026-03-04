# Database setup guide (for the team)

## What you're creating

- **Database name:** `group1_lab_db`
- **Table:** `tbl_user` (columns: `id`, `username`, `password`, `created_at`)

The script is in the project: `database/create_tables.sql`.

---

## Step 1: Install MySQL

**macOS (Homebrew):**
```bash
brew install mysql
brew services start mysql
```

**Windows:**  
Download the MySQL installer from https://dev.mysql.com/downloads/installer/ and run it. During setup, set a root password and note it.

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install mysql-server
sudo systemctl start mysql
```

---

## Step 2: (Optional) Set root password

If MySQL asks for a password and you don't have one yet:

**macOS/Linux:** In a terminal:
```bash
mysql -u root
```
Then in the MySQL prompt:
```sql
ALTER USER 'root'@'localhost' IDENTIFIED BY 'your_password';
FLUSH PRIVILEGES;
EXIT;
```
Use the same `your_password` when running the script and in the app (see Step 4).

**Windows:** You set the root password during installer; use that.

---

## Step 3: Create the database and table

### Option A — Command line (any OS)

1. Open a terminal.
2. Go to the project folder:
   ```bash
   cd path/to/miva/group-1-sen-csc312-lab-work
   ```
3. Run the SQL file:
   - **If root has no password:**
     ```bash
     mysql -u root < database/create_tables.sql
     ```
   - **If root has a password:**
     ```bash
     mysql -u root -p < database/create_tables.sql
     ```
     Enter the password when prompted.

### Option B — MySQL Workbench

1. Open MySQL Workbench and connect to your local MySQL (e.g. "Local instance MySQL").
2. Open the file: **File → Open SQL Script** → choose `database/create_tables.sql`.
3. Click the lightning icon (Execute) or press Ctrl+Shift+Enter (Windows/Linux) / Cmd+Shift+Enter (Mac).
4. Confirm there are no errors in the output.

### Option C — Copy-paste in MySQL CLI

1. Run:
   ```bash
   mysql -u root -p
   ```
2. Paste the full contents of `database/create_tables.sql` (all 14 lines).
3. Press Enter, then type `EXIT;` to leave.

---

## Step 4: Database config — tell the Flask app how to connect

The app reads connection settings from environment variables (see `app.py`). Defaults:

| Variable          | Default        | Description   |
|-------------------|----------------|---------------|
| `MYSQL_HOST`      | `localhost`    | MySQL server  |
| `MYSQL_USER`      | `root`         | MySQL user    |
| `MYSQL_PASSWORD`  | *(empty)*      | MySQL password |
| `MYSQL_DATABASE`  | `group1_lab_db`| Database name |

If your MySQL root **has a password**, set it before running the app:

**macOS/Linux (current terminal only):**
```bash
export MYSQL_PASSWORD=your_password
```

**Windows (Command Prompt):**
```cmd
set MYSQL_PASSWORD=your_password
```

**Windows (PowerShell):**
```powershell
$env:MYSQL_PASSWORD="your_password"
```

Then run the app from the project folder:
```bash
python app.py
```

---

## Step 5: Check that it worked

**From command line:**
```bash
mysql -u root -p -e "USE group1_lab_db; SHOW TABLES; DESCRIBE tbl_user;"
```
You should see `tbl_user` and its columns.

**Or in MySQL Workbench:**  
Refresh the left panel under your connection → **Schemas** → `group1_lab_db` → **Tables** → `tbl_user`.

---

## Quick reference

| Task | Command / action |
|------|------------------|
| Run the script | `mysql -u root -p < database/create_tables.sql` |
| Set app password (macOS/Linux) | `export MYSQL_PASSWORD=yourpassword` (then run app) |
| Set app password (Windows CMD) | `set MYSQL_PASSWORD=yourpassword` (then run app) |
| Set app password (Windows PowerShell) | `$env:MYSQL_PASSWORD="yourpassword"` (then run app) |
| Start MySQL (Mac) | `brew services start mysql` |
| Start MySQL (Linux) | `sudo systemctl start mysql` |
| Start MySQL (Windows) | **Services:** Win + R → `services.msc` → find "MySQL" or "MySQL80" → Start. **Or** CMD (Admin): `net start MySQL80` (use your service name if different). |

---

## Run and test

After the database and table exist and (if needed) `MYSQL_PASSWORD` is set:

1. From the project folder with venv activated: `python app.py`
2. Open http://127.0.0.1:5000 — check the homepage and click “Sign Up”
3. Submit a username and password (8+ chars) and confirm you see a success message
4. Optionally verify: `mysql -u root -p -e "USE group1_lab_db; SELECT * FROM tbl_user;"`

For full setup and testing steps, see the README.

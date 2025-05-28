import sqlite3

# Path to your SQLite DB file (adjust if needed)
db_path = "login_attempts.db"

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Query all saved login attempts
cursor.execute("SELECT id, email, password, timestamp FROM login_attempts")
rows = cursor.fetchall()

print("Saved Login Attempts:")
for row in rows:
    print(f"ID: {row[0]}, Email: {row[1]}, Password: {row[2]}, Timestamp: {row[3]}")

conn.close()

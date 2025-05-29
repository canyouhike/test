import psycopg2

# PostgreSQL connection URL
DATABASE_URL = "postgresql://log_db_swpc_user:FaNOI0C3OiMNSkbb9d19h0AwGo1jbg2b@dpg-d0rqkb15pdvs738th5f0-a.oregon-postgres.render.com/log_db_swpc"

# Parse the URL to connection parameters (optional, or just use connect with URL)
conn = psycopg2.connect(DATABASE_URL)
cursor = conn.cursor()

# Query all saved login attempts
cursor.execute("SELECT id, email, password, timestamp FROM login_attempts ORDER BY timestamp DESC;")
rows = cursor.fetchall()

print("Saved Login Attempts:")
for row in rows:
    print(f"ID: {row[0]}, Email: {row[1]}, Password: {row[2]}, Timestamp: {row[3]}")

cursor.close()
conn.close()


# import sqlite3

# # Path to your SQLite DB file (adjust if needed)
# db_path = "login_attempts.db"

# conn = sqlite3.connect(db_path)
# cursor = conn.cursor()

# # Query all saved login attempts
# cursor.execute("SELECT id, email, password, timestamp FROM login_attempts")
# rows = cursor.fetchall()

# print("Saved Login Attempts:")
# for row in rows:
#     print(f"ID: {row[0]}, Email: {row[1]}, Password: {row[2]}, Timestamp: {row[3]}")

# conn.close()

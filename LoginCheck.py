import sys
import mysql.connector

email = sys.argv[1]
password = sys.argv[2]

conn = mysql.connector.connect(
    host="caboose.proxy.rlwy.net",
    user="root",
    password="kSFCjWBLJRtYdCvlbnoGYbrvhiwiBXso",
    database="railway",
    port=33995
)

cursor = conn.cursor()

cursor.execute("SELECT * FROM users WHERE email=%s AND password=%s", (email, password))
user = cursor.fetchone()

if user:
    print("valid")
else:
    print("invalid")

cursor.close()
conn.close()

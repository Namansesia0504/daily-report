import mysql.connector


conn = mysql.connector.connect(
    host="localhost",     
    user="root", 
    password="King#123", 
    database="college" 
)

if conn.is_connected():
    print("Connected to MySQL")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        age INT
    )
""")

cursor.execute("INSERT INTO users (name, age) VALUES (%s, %s)", ("John Doe", 30))
conn.commit()

print("Data inserted successfully")
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="King#123",
    database="college"
)

cursor = conn.cursor()
cursor.execute("SELECT * FROM users")

for row in cursor.fetchall():
    print(row)

cursor.close()
conn.close()

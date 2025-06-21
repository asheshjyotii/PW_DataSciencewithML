import mysql.connector # Importing mysql connector library 

conn = mysql.connector.connect( # Establising connection to the MySQL database, returns a connection object
    database = 'student_management',
    host='localhost',
    user = 'root',
    password = 'root'
)

if conn.is_connected():
    print("Connected to the database successfully!")
else:
    print("Failed to connect to the database.")

# create cursor object
cursor = conn.cursor()

cursor.execute("INSERT INTO students (name, marks) VALUES (%s, %s);", ("Anwesha", 80))
conn.commit()
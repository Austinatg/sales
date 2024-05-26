import sqlite3
import requests
print({{ request.user.username }})

# Connect to the SQLite database
conn = sqlite3.connect('db.sqlite3')

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Query the sqlite_master table to get table names
# cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
cursor.execute('SELECT * FROM home_sales')

# Fetch all table names from the result set
tables = cursor.fetchall()

# Print the table names
for table in tables:
    print(table[6])

# Close the cursor and the connection
cursor.close()
conn.close()

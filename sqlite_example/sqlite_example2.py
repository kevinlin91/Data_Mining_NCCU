import sqlite3


conn = sqlite3.connect('./iris.db')
cursor = conn.cursor()
data = cursor.execute("SELECT * FROM IRIS")

for row in data:
    print row[0]

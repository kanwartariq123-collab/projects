import sqlite3
conn = sqlite3.connect('studentportal.db')
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS monthly_fees (id INTEGER PRIMARY KEY, name TEXT, fee TEXT)")
conn.commit()
conn.close()
print("Table check ho gayi!")
import sqlite3

sqlite_file = 'test.db'
# Connecting to the database file
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

# A) Inserts an ID with a specific value in a second column 
c.execute("INSERT INTO History (coin, mode, ammount, newTotal, date) VALUES ('Quarter', 'addition', 124, '32$', (CURRENT_TIMESTAMP))")
c.execute("INSERT INTO Quarters (Ammount, Value) VALUES (124, '32$')")
conn.commit()
conn.close()
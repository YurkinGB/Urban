import sqlite3

connect = sqlite3.connect('not_telegram1.db')
cursor = connect.cursor()

cursor.execute("DELETE FROM Users WHERE id = ?", (6,))

cursor.execute("SELECT COUNT(*) FROM Users")
users_count = cursor.fetchone()[0]

cursor.execute("SELECT SUM(balance) FROM Users")
balance_sum = cursor.fetchone()[0]

print(round(balance_sum / users_count, 2))

connect.close()

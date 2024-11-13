import sqlite3

connect = sqlite3.connect('not_telegram1.db')
cursor = connect.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL)''')

for i in range(1, 11):
    cursor.execute("INSERT INTO Users(username, email, age, balance) VALUES (?, ?, ?, ?)",
                   (f"user{i}", f"example{i}@gmail.com", i*10, 1000))

for i in range(1, 11):
    if i % 2 == 0:
        cursor.execute("UPDATE Users SET balance = ? WHERE id = ?", (500, i))

for i in range(1, 11):
    if i % 3 == 0:
        cursor.execute("DELETE From Users WHERE id = ?", (i,))

cursor.execute("SELECT *FROM Users WHERE age != 60")
users = cursor.fetchall()

for user in users:
    print(f'Имя: {user[1]} | Почта: {user[2]} | Возраст: {user[3]} | Баланс: {user[4]}')

connect.commit()
connect.close()
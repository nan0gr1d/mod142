#  module_14_2

import sqlite3

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)""")

number_records = 10
for i in range(1, number_records + 1):
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES(?, ?, ?, ?)",
                   (f"User{i}", f"example{i}@gmail.com", f"{i * 10}", "1000"))

for i in range(1, number_records + 1):
    if i % 2 == 1:
        cursor.execute("UPDATE users SET balance = 500 WHERE id = ?", (f"{i}",))

for i in range(1, number_records + 1):
    if i % 3 == 1:
        cursor.execute("DELETE FROM users WHERE id = ?", (f"{i}",))

#  Удалите из базы данных not_telegram.db запись с id = 6.
cursor.execute("DELETE FROM users WHERE id = 6")
connection.commit()

#  Подсчитать общее количество записей.
cursor.execute("SELECT COUNT(*) FROM Users")
total_users = cursor.fetchone()[0]

#  Посчитать сумму всех балансов.
cursor.execute("SELECT SUM(balance) FROM Users")
all_balances = cursor.fetchone()[0]
connection.close()

#  Вывести в консоль средний баланс всех пользователя.
print(all_balances / total_users)

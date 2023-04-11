# import sqlite3
# import cursor
#
# try:
#     conn = sqlite3.connect('accountant.db')
#     cursor = conn.cursor()
#
#     #create user with id 1000
#     cursor.execute("INSERT OR IGNORE INTO 'users' ('users_id') VALUES (?)",(1000,))
#
#     #show all users
#     users = cursor.execute("SELECT * FROM 'users'")
#     print(users.fetchall())
#
#     #complete changes
#     conn.commit()
#
# except sqlite3.Error as error:
#     print("Error",error)
#
# finally:
#     if conn:
#         conn.close()

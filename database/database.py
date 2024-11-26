import sqlite3 as sq
import os

db = sq.connect("tgbot.db")
cur = db.cursor()

def db_start():
    cur.execute("CREATE TABLE IF NOT EXISTS tasks("
                "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                "task_number INTEGER NOT NULL,"
                "img BLOB NOT NULL,"
                "answer TEXT NOT NULL)")
    cur.execute("CREATE TABLE IF NOT EXISTS users("
                "user_id INTEGER,"
                "firstCount INTEGER)")
    # cur.execute("ALTER TABLE tasks ADD COLUMN file BLOB")
    # cur.execute("ALTER TABLE users RENAME COLUMN firstCount TO count")
    # cur.execute("DELETE FROM users WHERE user_id = 1376194255")

    db.commit()



def save_users(user_idd, count):
    sql_check = cur.execute("SELECT * FROM users WHERE user_id = " + str(user_idd)).fetchall()
    if len(sql_check) > 0:
        print("Такой пользователь уже есть")
    else:
        sql_insert_user = """INSERT INTO users (user_id, count) VALUES (?, ?)"""
        data_tuple = (user_idd, count)
        cur.execute(sql_insert_user, data_tuple)


    db.commit()


def read_count(user_idd):
    first_count_query = """SELECT * FROM users WHERE user_id = ?"""
    cur.execute(first_count_query, (user_idd,))
    return cur.fetchone()[1]

def convert(filename):
    with open(filename, 'rb') as file:
        blob_data = file.read()
    return blob_data

def insert_blob(id, task_number, img, answer):
    sql_insert = """INSERT INTO tasks (id, task_number, img, answer) VALUES (?, ?, ?, ?)"""

    emp_img = convert(img)
    data_tuple = (id, task_number, emp_img, answer)
    cur.execute(sql_insert, data_tuple)

    db.commit()

# def insert_data(id, task_number, img, answer):
#     sql_insert = """INSERT INTO tasks (id, task_number, img, answer VALUES (?, ?, ?, ?)"""
#     emp_img = convert(img)
#     data_tuple = (id, task_number, emp_img, answer)
#     cur.execute(sql_insert,  data_tuple)
#
#     db.commit()
#
# lst = []
# for i in range(7, 9):
#     f = open(f"D:/Bot/data_for_db/answer_{i}.txt", "r")
#     lst.append(f.read())
# print(lst)
# for j in range(7, 9):
#     insert_blob(j, 1, f"D:/Bot/data_for_db/img_{j}.png", lst[j - 7])


# insert_blob(1, 1, "../firstImg.png", "23")
# insert_blob(2, 1, "../secondImg.png", "76")


def write_to_file(data, filename):
    with open(filename, 'wb') as file:
        file.write(data)

def write_to_fileStr(data, filename):
    with open(filename, 'w') as file:
        file.write(data)


def read_blob(e_id):
    fetch_blob = """SELECT * FROM tasks WHERE id = ?"""
    cur.execute(fetch_blob, (e_id,))
    record = cur.fetchall()

    for row in record:
        idd = row[0]
        task_number = row[1]
        img = row[2]
        answer = row[3]

        img_path = os.path.join('database/db_data', "img_" + str(idd) + ".png")
        answer_path = os.path.join('database/db_data', "answer_" + str(idd) + ".txt")


        write_to_file(img, img_path)
        write_to_fileStr(answer, answer_path)


# read_blob(1)
# read_blob(2)















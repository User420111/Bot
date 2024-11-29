import sqlite3 as sq
import os

# Подключаемся к БД
db = sq.connect("database/tgbot.db")
cur = db.cursor()


def db_start():  # Создаём таблицы в БД, если их нет
    cur.execute("CREATE TABLE IF NOT EXISTS tasks("
                "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                "task_number INTEGER NOT NULL,"
                "img BLOB NOT NULL,"
                "answer TEXT NOT NULL)")
    cur.execute("CREATE TABLE IF NOT EXISTS users("
                "user_id INTEGER,"
                "count INTEGER)")
    # cur.execute("ALTER TABLE tasks ADD COLUMN file BLOB")
    # cur.execute("ALTER TABLE users RENAME COLUMN firstCount TO count")
    # cur.execute("DELETE FROM users WHERE user_id = 1376194255")

    db.commit()



def save_users(user_idd, count):  # Сохраняем id пользователся, если его нет в БД
    sql_check = cur.execute("SELECT * FROM users WHERE user_id = " + str(user_idd)).fetchall()
    if len(sql_check) > 0:
        print("Такой пользователь уже есть")
    else:
        sql_insert_user = """INSERT INTO users (user_id, count) VALUES (?, ?)"""
        data_tuple = (user_idd, count)
        cur.execute(sql_insert_user, data_tuple)


    db.commit()


def update_users(user_idd, count):  # Сохраням просмотренные пользователем задания
    sql_update = """UPDATE users SET count = ? WHERE user_id = ?"""
    data = (count, user_idd)
    cur.execute(sql_update, data)
    db.commit()

def read_count(user_idd):  # Смотрим, сколько заданий пользователь просмотрел
    first_count_query = """SELECT * FROM users WHERE user_id = ?"""
    cur.execute(first_count_query, (user_idd,))
    return cur.fetchone()[1]

def convert(filename): # Конвертируем картинку в бинарные данные
    with open(filename, 'rb') as file:
        blob_data = file.read()
    return blob_data

def load_blob(id, task_number, img, answer): # Загружаем задание в БД
    sql_insert = """INSERT INTO tasks (id, task_number, img, answer) VALUES (?, ?, ?, ?)"""

    emp_img = convert(img)
    data_tuple = (id, task_number, emp_img, answer)
    cur.execute(sql_insert, data_tuple)

    db.commit()


######## Здесь мы загружали задания в БД

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


# load_blob(1, 1, "../firstImg.png", "23")
# load_blob(2, 1, "../secondImg.png", "76")

# def write_to_fileStr(data, filename):
#     with open(filename, 'w') as file:
#         file.write(data)


def convert_to_img(data, filename):  # Конвертируем BLOB-данные обратно в картинку
    with open(filename, 'wb') as file:
        file.write(data)

def read_blob(e_id): # Загружаем картинку из БД в директорию db_data
    # Как только бот отправит картинку пользователю, картинка удалится из директории
    fetch_blob = """SELECT * FROM tasks WHERE id = ?"""
    cur.execute(fetch_blob, (e_id,))
    record = cur.fetchall()

    for i in record:
        idd = i[0]
        task_number = i[1]
        img = i[2]
        # answer = i[3]

        img_path = os.path.join('database/db_data', "img_" + str(idd) + ".png")
        # answer_path = os.path.join('database/db_data', "answer_" + str(idd) + ".txt")


        convert_to_img(img, img_path)
        # write_to_fileStr(answer, answer_path)

def read_answer(e_id): # Функция для просмотра ответа
    fetch_answer = """SELECT * FROM tasks WHERE id = ?"""
    cur.execute(fetch_answer, (e_id,))
    record = cur.fetchall()
    answer = None
    for j in record:
        answer = j[3]
    return answer




# read_blob(1)
# read_blob(2)















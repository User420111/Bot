import sqlite3 as sq

db = sq.connect('../tg.db')
cur = db.cursor()


def convert_to_binary_data(filename):
    with open(filename, 'rb') as file:
        blob_data = file.read()
    return blob_data

def insert_blob(id, image):
    query = """INSERT INTO tasks (id, image) VALUES (?, ?)"""

    emp_img = convert_to_binary_data(image)

    data_tuple = (id, emp_img)
    cur.execute(query, data_tuple)

    print("Hello")

    db.commit()


def db_start():
    cur.execute("CREATE TABLE IF NOT EXISTS tasks("
                "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                "image BLOB NOT NULL,"
                "answer TEXT)")


    db.commit()

def db_first_task():
    print("Hello")
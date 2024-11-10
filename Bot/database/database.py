import sqlite3 as sq

db = sq.connect('tg.db')
cur = db.cursor()

async def db_start():
    cur.execute("CREATE TABLE IF NOT EXISTS tasks("
                "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                "text TEXT,"
                "image BLOB NOTN NULL"
                "answer TEXT)")
    db.commit()


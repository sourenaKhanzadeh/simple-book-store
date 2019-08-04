import sqlite3

def connect(this, **kwargs):
    conn = sqlite3.connect("books.db")
    row = this(conn, kwargs)
    conn.commit()
    conn.close()
    return row

def mainTable(conn, kwargs):
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY , title text, author text, year integer, isbn integer)")

def insert(conn, kwargs):
    cur = conn.cursor()
    # print((i for i in kwargs.values()))
    cur.execute("INSERT INTO book VALUES (NULL , ?, ?, ?, ?)", [i for i in kwargs.values()])


def view(conn, kwargs):
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    return rows


def search(conn, kwargs):
    cur = conn.cursor()
    cur.execute("SELECT  * FROM book WHERE title =? OR author = ? OR year = ? OR isbn = ?", [i for i in kwargs.values()])
    rows = cur.fetchall()
    return rows


def delete(conn, id):
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE id = ?")


def update(conn, kwargs):
    cur = conn.cursor()
    cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?", [i for i in kwargs.values()])

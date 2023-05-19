from flaskr import app
from flask import render_template ,request,redirect,url_for,g
import sqlite3
DATABASE="database.db"

def recognizedata():
    # データベースに接続
    con=sqlite3.connect(DATABASE)
    conn=con.cursor()
    db_books=conn.execute('SELECT * FROM books').fetchall()

    books=[]
    for row in db_books:
        books.append({"title":row[0],"price":row[1],"arraival_day":row[2]})
        a=print("aa")
    # return render_template(
    #     'recognize.html',
    #     books=db_books
    # )
    return print(books)
recognizedata()
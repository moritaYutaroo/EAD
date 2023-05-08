from flaskr import app
from flask import render_template ,request,redirect,url_for
import sqlite3
DATABASE="database.db"

@app.route('/')
def index():
    con = sqlite3.connect(DATABASE)
    db_books=con.execute('SELECT * FROM books').fetchall()
    con.close()

    books=[]
    for row in db_books:
        books.append({"title":row[0],"price":row[1],"arraival_day":row[2]})

    return render_template(
        'index.html',
        books=books
    )



@app.route('/form')
def form():
    return render_template(
        'form.html'
    )
@app.route('/delete')
def delete():
    return render_template(
        'delete.html'
    )

@app.route('/recognize')
def recognize():
    return render_template(
        'recognize.html'
        )
    
@app.route('/register',methods=['POST'])
def register():
    title = request.form["title"]
    price=request.form["price"]
    arraival_day=request.form["arraival_day"]
    con=sqlite3.connect(DATABASE)
    params=[]
    if title:
        params.append(title)
    if price:
        params.append(price)
    if arraival_day:
        params.append(arraival_day)
    if len(params)<3:
        return redirect(url_for('index'))
    else:
        con.execute('INSERT INTO books VALUES(?, ?, ?)',[title,price,arraival_day])
        con.commit()
        con.close()
    return redirect(url_for('index'))

@app.route('/delete', methods=['DELETE', 'GET','POST'])
def deletedata():
    title = request.form.get("title")
    price = request.form.get("price")
    arraival_day = request.form.get("arrival_day")
    con = sqlite3.connect(DATABASE)
    conn = con.cursor()
    delete_query = "DELETE FROM books WHERE "
    params = []
    if title:
        delete_query += "title = ? AND "
        params.append(title)
    if price:
        delete_query += "price = ? AND "
        params.append(price)
    if arraival_day:
        delete_query += "arrival_day = ? AND "
        params.append(arraival_day)
    delete_query = delete_query.rstrip(" AND ")
    conn.execute(delete_query, params)
    con.commit()
    con.close()
    return redirect(url_for('index'))

@app.route('/recognize', methods=['DELETE', 'GET','POST'])
def recognizedata():
    db_books=con.execute('SELECT * FROM books').fetchall()
    return f"{db_books}"
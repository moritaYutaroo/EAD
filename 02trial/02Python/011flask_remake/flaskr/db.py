import sqlite3

DATABASE="database.db"
def create_books_table():
    con = sqlite3.connect(DATABASE)
    con.execute("CREATE TABLE IF NOT EXISTS books (title,price,arraival_day)")
    
    con.close()

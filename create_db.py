import sqlite3

def create_db():
    conn=sqlite3.connect(database=r'ims.db')
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Employee(eid INTEGER PRIMARY KEY AUTOINCREMENT, name text,email text,gender text,contact text,dob text,doj text,pass text,usrtyp text,address text,salary text)")
    conn.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS Supplier(invoice INTEGER PRIMARY KEY AUTOINCREMENT, name text,contact text,desc text )")
    conn.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS Category(cid INTEGER PRIMARY KEY AUTOINCREMENT, name text)")
    conn.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS Product(pid INTEGER PRIMARY KEY AUTOINCREMENT,category text,supplier text, name text,price text,qty text,status text)")
    conn.commit()

create_db()
import sqlite3
import csv

def aaa ():
    conn = sqlite3.connect('books.db')
    curs = conn.cursor()
    # curs.execute('create table book (title VARCHAR(20) primary key, author VARCHAR(20), year INT)')
    ins = 'insert into book (title, author, year) values(?,?,?)'

    with open('books2.csv') as f:
        csvont = csv.DictReader(f)
        for row in csvont:
            curs.execute(ins, (row["title"],row["author"],row["year"] ))

    conn.commit()

    curs.close()
    conn.close()
    
def bbb ():
    conn = sqlite3.connect('books.db')
    curs = conn.cursor()

    result = curs.execute('select title from book')
    rows = [ i[0] for i in result.fetchall()]
    rows.sort()
    for row in rows:
        print(row)

    curs.close()
    conn.close()

def ccc ():
    conn = sqlite3.connect('books.db')
    curs = conn.cursor()

    result = curs.execute('select * from book')
    rows = sorted(result.fetchall(), key=lambda v: v[2])
    for row in rows:
        print(row)

    curs.close()
    conn.close()
    
def ddd ():
    import sqlalchemy as sa
    conn = sa.create_engine('sqlite:///books.db')
    rows = conn.execute('select title from book')
    sortedRows = sorted([i[0] for i in rows])
    for row in sortedRows:
        print(row)
    rows.close

def fff():
    import redis
    conn = redis.Redis()
    # conn.hmset('test', {'count':1, 'name':'gettter'})
    print(conn.hgetall('test'))
    conn.hincrby('test', 'count')
    conn.close()
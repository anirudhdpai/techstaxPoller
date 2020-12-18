import sqlite3
import getfromct as ct
import getperson as pr

def insertct():
    conn = sqlite3.connect('cocktail.db')
    cur = conn.cursor()
    cur.execute("""CREATE TABLE if not exists cocktails(
                id integer primary key,
                name text,
                inst text,
                img text
    )""")
    x=ct.ctrequest()
    if x[0]!=404:
        cur.execute("INSERT INTO cocktails VALUES(:a,:b,:c,:d)",(x[0],x[1],x[2],x[3]))
    else:
        pass

    conn.commit()
    conn.close()

def insertrp():
    conn=sqlite3.connect("person.db")
    c=conn.cursor()

    c.execute("""CREATE TABLE if not exists user(
                email text,
                usrn text,
                pwd text,
                img text
    )""")
    x=pr.prrequest()
    if x[0]!=404:
        c.execute("INSERT INTO user VALUES(:a,:b,:c,:d)",(x[0],x[1],x[2],x[3]))
    else:
        pass
    c.execute("select * from user")
    print(c.fetchmany(5))

    conn.commit()
    conn.close()

insertrp()
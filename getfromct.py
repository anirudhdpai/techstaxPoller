import requests
import json
import sqlite3

conn=sqlite3.connect("cocktail.db")
c=conn.cursor()

# c.execute("""CREATE TABLE cocktails(      define and exec
#             id integer primary key,
#             email text,
#             usrn text,
#             pwd text,
#             img text
# )""")
c.execute("SELECT * FROM cocktails")
print(c.fetchall())

response = requests.get("https://www.thecocktaildb.com/api/json/v1/1/random.php")
if response.status_code==200:
    dct=response.json()['results'][0]
    print(dct)
    # username=dct['login']['username']
    # password=dct['login']['password']
    # email=dct['email']
    # img_url=dct['picture']['large']
    #c.execute("""INSERT INTO users VALUES(NULL,:a,:b,:c,:d);""",(email,username,password,img_url))
    conn.commit()
else:
    print("Error: Status Code - {}".format(response.status_code))
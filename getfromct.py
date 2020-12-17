import requests
import json
import sqlite3

conn=sqlite3.connect("cocktail.db")
c=conn.cursor()

# c.execute("""CREATE TABLE cocktails(
#             id integer primary key,
#             name text,
#             inst text,
#             img text
# )""")

response = requests.get("https://www.thecocktaildb.com/api/json/v1/1/random.php")
if response.status_code==200:
    dct=response.json()['drinks'][0]
    #print(dct)
    did=dct['idDrink']
    name=dct['strDrink']
    inst=dct['strInstructions']
    url=dct['strDrinkThumb']
    #print(did,name,inst,url)
    try:
        c.execute("INSERT INTO cocktails VALUES(:a,:b,:c,:d)",(did,name,inst,url))
    except:
        pass
    #c.execute("""INSERT INTO users VALUES(NULL,:a,:b,:c,:d);""",(email,username,password,img_url))
    conn.commit()
    # c.execute("SELECT * FROM cocktails")
    # print(c.fetchall())
else:
    print("Error: Status Code - {}".format(response.status_code))
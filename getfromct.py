import requests
import json
import sqlite3

def ctrequest():
    ctail=[]
    response = requests.get("https://www.thecocktaildb.com/api/json/v1/1/random.php")
    if response.status_code==200:
        dct=response.json()['drinks'][0]
        #print(dct)
        ctail.append(dct['idDrink'])
        ctail.append(dct['strDrink'])
        ctail.append(dct['strInstructions'])
        ctail.append(dct['strDrinkThumb'])
        #print(did,name,inst,url)
    else:
        ctail.append(response.status_code)
    return ctail
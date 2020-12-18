import requests
import json
import sqlite3
import asyncio
import aiohttp

def prrequest():
    person=[]
    response = requests.get("https://randomuser.me/api/")
    if response.status_code==200:
        dct=response.json()['results'][0]
        #print(dct)
        person.append(dct['login']['username'])
        person.append(dct['login']['password'])
        person.append(dct['email'])
        person.append(dct['picture']['large'])
    else:
        person.append(response.status_code)
    return person
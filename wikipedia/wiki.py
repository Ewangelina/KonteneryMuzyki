url = 'https://en.wikipedia.org/wiki/Category:Songs_by_year'
top_value = 0

import requests
import wikipediaapi
from pymongo import MongoClient, errors
import random

def find_song(mycol):
  num = random.randrange(0, top_value)
  collection = mycol.find({ "value": { "$lte": num } }).sort("value",-1).limit(1) # for MAX
  for row in collection:
    num = num - row["value"]
    category = row["name"].replace('"','')

    wiki = wikipediaapi.Wikipedia('en')
    song_list = wiki.page(category)
    index = 0
    for song in song_list.categorymembers.values():
      if index == num:
        if song.namespace == wikipediaapi.Namespace.MAIN:
          page = wiki.page(str(song).split('(')[0])
          url = "https://en.wikipedia.org/?curid=" + str(page.pageid)
          print(url)
          return
        else:
          find_song(mycol)
      index = index + 1

#https://en.wikipedia.org/w/api.php?action=query&list=categorymembers&cmtitle=Category:Songs_by_year&cmtype=subcat
wiki = wikipediaapi.Wikipedia('en')
cat = wiki.page('Category:Songs_by_year')

# global variables for MongoDB host (default port is 27017)
DOMAIN = '172.17.0.2'
PORT = 27017

# use a try-except indentation to catch MongoClient() errors
try:
  # try to instantiate a client instance
  client = MongoClient(
    host = [ str(DOMAIN) + ":" + str(PORT) ],
    serverSelectionTimeoutMS = 3000 # 3 second timeout
  )
  mydb = client["wiki"]  
  mycol = mydb["song_cat"]
  
  for p in cat.categorymembers.values():
    if p.namespace == wikipediaapi.Namespace.CATEGORY:
      name = str(p)
      name = '"' + name.split(" (id:")[0] + '"'
      row = { "name": name, "value": top_value }
      mycol.insert_one(row)
      print(len(p.categorymembers))
      top_value = top_value + len(p.categorymembers)
      break

  find_song(mycol)


except errors.ServerSelectionTimeoutError as err:
  # set the client and DB name list to 'None' and `[]` if exception
  client = None
  database_names = []

  # catch pymongo.errors.ServerSelectionTimeoutError
  print ("pymongo ERROR:", err)
except KeyboardInterrupt:
  print("user exit")

    

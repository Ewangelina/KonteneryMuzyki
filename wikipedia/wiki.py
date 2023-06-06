url = 'https://en.wikipedia.org/wiki/Category:Songs_by_year'
top_value = 0

import requests
import wikipediaapi
from pymongo import MongoClient, errors
import random
import socket

HOST = "172.17.0.2"  # The server's hostname or IP address
HOST_PORT = 7777  # The port used by the server

def find_song(mycol):
  num = random.randrange(0, top_value)
  print(num)
  collection = mycol.find({ "value": { "$lte": num } }).sort("value",-1).limit(1) # for MAX
  for row in collection:
    num = num - row["value"]
    print(num)
    category = row["name"].replace('"','')
    print(category)

    wiki = wikipediaapi.Wikipedia('en')
    song_list = wiki.page(category)
    index = 0
    for song in song_list.categorymembers.values():
      if index == num:
        if song.namespace == wikipediaapi.Namespace.MAIN:
          page = wiki.page(str(song).split('(')[0])
          url = "https://en.wikipedia.org/?curid=" + str(page.pageid)
          return url
        else:
          return find_song(mycol)
      index = index + 1

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, HOST_PORT))


#https://en.wikipedia.org/w/api.php?action=query&list=categorymembers&cmtitle=Category:Songs_by_year&cmtype=subcat
wiki = wikipediaapi.Wikipedia('en')
cat = wiki.page('Category:Songs_by_year')

# global variables for MongoDB host (default port is 27017)
DOMAIN = '172.17.0.4'
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
      

  while (True):
    data = s.recv(1024)
    if data == str.encode("request"):
      url = find_song(mycol)
      s.sendall(str.encode(url)) #turn to bytes
    if data == str.encode("quit"):
      break
except errors.ServerSelectionTimeoutError as err:
  # set the client and DB name list to 'None' and `[]` if exception
  client = None
  database_names = []

  # catch pymongo.errors.ServerSelectionTimeoutError
  print ("pymongo ERROR:", err)

    

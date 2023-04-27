url = 'https://en.wikipedia.org/wiki/Category:Songs_by_year'

import requests
import wikipediaapi
#pip install wikipedia-api


wiki = requests.get(url).text
body = wiki.split('id="mw-content-text"')
content = body[1].split('class="mw-category mw-category-columns"')
content = content[1].split("(previous page)")[0]
content_groups = content.split('class="mw-category-group"')[1:4]
song_entry_list = []
link_list = []
no_songs = []

#https://en.wikipedia.org/w/api.php?action=query&list=categorymembers&cmtitle=Category:Songs_by_year&cmtype=subcat

#class="CategoryTreeItem"

for i in range(len(content_groups)):
    individual = content_groups[i].split('class="CategoryTreeSection"')
    for j in range(1, len(individual) - 1):
        song = str(j) + str(i)
        try:
            song = individual[j].split('<a href="')[1]
            song = song.split('" dir="ltr">')[0]
        except:
            print(i, j)

        try:
            songs = song.split(', ')
            for k in songs:
                if k[0] == '/':
                    song_entry_list.append(k.split('/wiki/')[1])
        except:
            print(j)

        if song[0] == '/':
            song_entry_list.append(song.split('/wiki/')[1])

link_list.append('/wiki/Category:Year_of_song_unknown')

    
for i in range(0, len(song_entry_list),2):
    try:
        link_list.append(song_entry_list[i].split('"')[0])
    except:
        print(song_entry_list[i])

last_number = 0
try:
    last_number = song_entry_list[i].split('" title="Category:')[1]
    last_number = int(last_number.split(' ')[0])
except:
    last_number = 1971

for i in range(last_number, 2023):
    link = 'Category:' + str(i) + '_songs'
    link_list.append(link)

print(link_list[48])

wiki = wikipediaapi.Wikipedia('en')
cat = wiki.page(link_list[48])
for p in cat.categorymembers.values():
  if p.namespace == wikipediaapi.Namespace.CATEGORY:
    # it is category, so you have to make decision
    # if you want to fetch also text from pages that belong
    # to this category
    print(p)
  elif p.namespace == wikipediaapi.Namespace.MAIN:
    # it is page => we can get text
    print(p)

    

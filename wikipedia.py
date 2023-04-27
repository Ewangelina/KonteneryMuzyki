url = 'https://en.wikipedia.org/wiki/Category:Songs_by_year'

import requests


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
                    song_entry_list.append(k)
        except:
            print(j)

        if song[0] == '/':
            song_entry_list.append(song)
    
for i in range(2, len(song_entry_list)):
    try:
        link_list.append(song_entry_list[i].split('"')[0])
        number = song_entry_list[i].split('" title="Category:')[1]
        no_songs.append(int(number.split(' ')[0]))
    except:
        print(song_entry_list[i])

#print(len(link_list))


#print(x.text)
#looping through the iterator:
#for c in x.iter_lines():
  #print(str(c))

    

url = 'https://en.wikipedia.org/wiki/Category:Songs_by_year'

import requests


wiki = requests.get(url).text
body = wiki.split('id="mw-content-text"')
content = body[1].split('class="mw-category mw-category-columns"')
content = content[1].split("(previous page)")[0]
print(content)



#print(x.text)
#looping through the iterator:
#for c in x.iter_lines():
  #print(str(c))

    

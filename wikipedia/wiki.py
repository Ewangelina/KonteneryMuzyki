url = 'https://en.wikipedia.org/wiki/Category:Songs_by_year'

import requests
import wikipediaapi
#pip install wikipedia-api

#https://en.wikipedia.org/w/api.php?action=query&list=categorymembers&cmtitle=Category:Songs_by_year&cmtype=subcat


wiki = wikipediaapi.Wikipedia('en')
cat = wiki.page('Category:Songs_by_year')
for p in cat.categorymembers.values():
  if p.namespace == wikipediaapi.Namespace.CATEGORY:
    name = str(p)
    name = name.split(" (id:")[0]
    #print(name)
    #print(len(p.categorymembers))
    #print('')
  elif p.namespace == wikipediaapi.Namespace.MAIN:
    print(p)

    

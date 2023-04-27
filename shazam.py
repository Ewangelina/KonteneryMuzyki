base_url = 'https://www.shazam.com/en/track/'

import requests
import random

while (True):
    num = random.randrange(10000000, 99999999)
    url = base_url + str(num)
    response = requests.get('https://w3schools.com').text
    if 'error-page panel-landing' not in response:
        print(url)
        break

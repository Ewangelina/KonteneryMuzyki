import requests
import random
import socket

HOST = "172.17.0.2"  # The server's hostname or IP address
PORT = 7777  # The port used by the server
base_url = 'https://www.shazam.com/pl/track/'

def get_url():
    while (True):
        num = random.randrange(10000000, 99999999)
        url = base_url + str(num)
        response = requests.get(url).text
        if 'error-page panel-landing' not in response:
            return url

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    data = s.recv(1024)
    print(data)
    if data == str.encode("request"):
        url = get_url()
        print(url)
        s.sendall(str.encode(url)) #turn to bytes
   



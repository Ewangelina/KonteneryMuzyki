import socket

HOST = "localhost"  # The server's hostname or IP address
PORT = 8080  # The port used by the server
base_url = 'https://www.shazam.com/pl/track/'


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print("Press enter to recieve a song")
    while (True):
    	line = input()
    	if line == "quit":
    		s.sendall(str.encode("quit"))
    		break
    	s.sendall(str.encode("request"))
    	data = s.recv(1024)
    	print(str(data))
    	
   



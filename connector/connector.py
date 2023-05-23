import socket
import random
IN_PORT = 7777  # Port to listen on (non-privileged ports are > 1023)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
HOST = (str)(s.getsockname()[0])
s.close()
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
  server_socket.bind((HOST,IN_PORT))
  server_socket.listen()
  print("Wait for shazam")
  shazam_connection, shazam_addr = server_socket.accept()
  print("Wait for wikipedia")
  wikipedia_connection, wikipedia_addr = server_socket.accept()
  print("Wait for ui")
  outside_connection, outside_addr = server_socket.accept()
  print("FULLY CONNECTED")

  while(True):
    data = outside_connection.recv(1024)
    if data == str.encode("quit"):
      shazam_connection.sendall(str.encode("quit"))
      break
    
    if data == str.encode("request"):
      num = random.randrange(1, 3)
      if num == 1:
        shazam_connection.sendall(str.encode("request"))
        url = shazam_connection.recv(1024)
        outside_connection.sendall(url)
      else:
        wikipedia_connection.sendall(str.encode("request"))
        url = wikipedia_connection.recv(1024)
        outside_connection.sendall(url)


  server_socket.close()

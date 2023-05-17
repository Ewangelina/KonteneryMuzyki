import socket

HOST = "127.0.0.77"  # Standard loopback interface address (localhost)
PORT = 7777  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.bind((HOST, PORT))
  s.listen()
  conn, addr = s.accept()
  with conn:
    #connect other two
    print(f"Connected by {addr}")
    conn.sendall("request")
    data = conn.recv(1024)
    print(data)


import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
HOST = (str)(s.getsockname()[0])
s.close()


PORT = 7777  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.bind((HOST, PORT))
  s.listen()
  conn, addr = s.accept()
  with conn:
    #connect other two
    print(f"Connected by {addr}")
    message = "request"
    conn.sendall(str.encode(message))
    data = conn.recv(1024)
    print(data)


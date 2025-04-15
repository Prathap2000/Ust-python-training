import socket
s=socket.socket()
s.connect(('127.0.0.1',1000))
print(s.recv(1024))
s.close()
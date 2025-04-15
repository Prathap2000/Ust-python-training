import socket
s=socket.socket()
s.bind(('127.0.0.1',1000))
s.listen(5)
while True:
    c,addr=s.accept()
    print('got connection',addr)
    c.send(bytes('thanks for connecting','utf-8'))
    c.close()
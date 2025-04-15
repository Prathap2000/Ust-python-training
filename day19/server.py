import socket
s=socket.socket() #creatig socket object
s.bind(('127.0.0.1',800))# ip and port
s.listen(5) #number of connection
while True:
    c,addr=s.accept() # connection establish with client
    print('got connection',addr)
    c.send(bytes('thanks for connecting','utf-8'))
    c.close() #close the connection
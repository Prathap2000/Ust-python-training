import socket
s=socket.socket() #creatig socket object
s.bind(('127.0.0.1',800))# ip and port
s.listen(5) #number of connection
while True:
    c,addr=s.accept() # connection establish with client
    print('got connection',addr)
    c.send(bytes('thanks for connecting','utf-8')) # to send the text throght the socket it need to convert to the bytes
    c.close() #close the connection
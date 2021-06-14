import socket 

c= socket.socket()

c.connect(("localhost",9999)


msg = c.recv(1024)
print(msg.decode('utf-8'))



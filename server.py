import socket 

s= socket.socket()

s.bind(("localhost",9999))
s.listen(5)

while True:
    client, address = s.accept()
    print(f"conection form {address} has been esablished")
    client.send(bytes("Hi how are you??","utf-8"))

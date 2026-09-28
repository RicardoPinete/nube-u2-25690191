import socket
c = socket.socket()
c.bind(("localhost", 5000))
c.send(b"hola")
print(c.recv(1024))
# b'eco: hola'
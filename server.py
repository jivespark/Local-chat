import socket

server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 9999))

server.listen(1)

while True:
    client, addr = server.accept()
    while True:
        print(client.recv(1024).decode())
        message=input("Type a message: ")
        client.send(message.encode())
    #client.send('server test'.encode())
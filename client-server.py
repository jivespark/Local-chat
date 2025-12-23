import socket
import threading
import time

user_in=None
def input_thread():
    global user_in
    while True:
        user_in=input()
threading.Thread(target=input_thread, daemon=True).start()

server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 9999))
server.listen(1)

client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("If you would want to connect to an address please type connect")
while True:
    client2, addr=server.accept()
    client2.setblocking(False)
    if(client2):
        while True:
            try:
                data=client2.recv(1024)
                if data:
                    print(data.decode())
            except BlockingIOError:
                pass
            if user_in is not None:
                client2.send(user_in.encode())
                user_in=None
            time.sleep(0.01)

    elif user_in=='connect':
        locIP=input("IP adress to connect to: ")
        client.connect((locIP, 9999))
        client.setblocking(False)
        while True:
            if user_in is not None:
                client.send(user_in.encode())
                user_in=None
            try:
                data=client.recv(1024)
                if data:
                    print(data.decode())
            except BlockingIOError:
                pass
            time.sleep(0.01)
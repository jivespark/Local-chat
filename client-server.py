import socket
import threading
import time

print("Welcome to my direct messaging system over lan!")
print("If you want to exit the current chat you are in type /exit")
print("If you would want to connect to an address please type connect")

user_in=None
def input_thread():
    global user_in
    while True:
        user_in=input()
threading.Thread(target=input_thread, daemon=True).start()

server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 9999))
server.listen(1)
server.setblocking(False)

client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)


while True:
    try:
        client2, addr=server.accept()
    except BlockingIOError:
        client2=None
    if client2:
        client2.setblocking(False)
        print("Client connected")
        while True:
            try:
                data=client2.recv(1024)
                if data:
                    if data.decode()=='/exit':
                        print("Connection closed")
                        break
                    else:
                        print(data.decode())
            except BlockingIOError:
                pass
            if user_in is not None:
                if user_in == '/exit':
                    client2.send(user_in.encode())
                    user_in=None
                    print("Connection closed")
                    break
                else:
                    client2.send(user_in.encode())
                    user_in=None
            time.sleep(0.01)

    elif user_in=='connect':
        print("IP adress to connect to: ")
        user_in=None
        while user_in is None:
            time.sleep(0.01)
        locIP=user_in
        user_in=None
        client.setblocking(False)
        try:
            client.connect((locIP, 9999))
        except BlockingIOError:
            pass
        while True:
            if user_in is not None:
                if(user_in=='/exit'):
                    client.send(user_in.encode())
                    user_in=None
                    print("Connection closed")
                    break
                client.send(user_in.encode())
                user_in=None
            try:
                data=client.recv(1024)
                if data:
                    if(data.decode()=='/exit'):
                        print("Connection closed")
                        break
                    else:
                        print(data.decode())
            except BlockingIOError:
                pass
            time.sleep(0.01)
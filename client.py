import socket
import threading
import time

user_input= None
def input_thread():
    global user_input
    while True:
        user_input=input()
threading.Thread(target=input_thread, daemon=True).start()

client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 9999))
client.setblocking(False)

while True:
    if user_input is not None:
        client.send(user_input.encode())
        user_input=None
    try:
        data=client.recv(1024)
        if data:
            print(data.decode())
    except BlockingIOError:
        pass
    time.sleep(0.01)
    
# Local-chat
Here is a chatting application that allows you to chat over your local LAN using sockets

## Features
- Send and receive messages over LAN.
- /exit to exit the chat
- Host a chat or connect to another device
- simple text based interface

## Requirements
- Python 3
- Supports all 3 major operating systems(Windows, Linux, macOS)
- No external library required

## Setting up
1. Run client-server.py
2. Find the local IP of the computer you are trying to message
    - Windows (terminal):`ipconfig`
    - Linux (terminal): `ip a`
    - macOS (Terminal): `ifconfig`)
3. On the computer initiating the chat type `connect`, hit enter, then type the local IP of the other computer.
4. You are ready! You can type something and the other person will be able to see it too.
5. To exit thechat type `/exit`. This will close the connection on both sides.
#!/usr/bin/env python

import socket
import Main

TCP_ADDRESS = ('localhost',2223)
BUFFER_SIZE = 1024

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(TCP_ADDRESS)
server.listen(10)

conn,addr = server.accept()

print("accepted")

while True:
    print("connection from : ", addr)
    data = conn.recv(BUFFER_SIZE).decode()
    print(data)

server.close()

#!/usr/bin/env python3

import socket
import sys

HOST = sys.argv[1] or '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = sys.argv[2] or 65432        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(f'Received data: {data}')
            if data == b'Hello, world':
                conn.sendall(b'Hello yourself')
            else:
                conn.sendall(b'Woaahhhh')


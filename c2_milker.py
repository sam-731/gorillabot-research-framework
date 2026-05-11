# client.py

import socket
import hashlib

SERVER = "127.0.0.1"
PORT = 38242

def authenticate(challenge, key):
    data = challenge + key
    return hashlib.sha256(data).hexdigest()

sock = socket.socket()

try:
    sock.connect((SERVER, PORT))

    sock.send(b"01")

    challenge = sock.recv(4)

    response = authenticate(challenge, b"research_key")

    sock.send(response.encode())

    print("[+] Auth completed")

except Exception as e:
    print(e)

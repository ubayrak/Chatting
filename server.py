import socket

host = '10.96.7.207'
port = 2323
FORMAT = 'utf-8'
EXIT = 'exit'
AD = (host, port)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# socket created with IPv4 and TCP features
s.bind(AD)


def chat(conn, addr):
    connected = True
    while connected:
        msg = conn.recv(1024).decode(FORMAT)
        print(f"[{addr}] : {msg}")

        if msg == EXIT:
        	connected = False

    conn.close()
        
s.listen()
print(f"[LISTENING] Server is listening on {host}:{port}")

client, addr = s.accept()
print(f"[NEW CONNECTION] {addr} connected.")
client.send("WELCOME MAN!!! PLEASE WRITE SOMeTHING".encode(FORMAT))
chat(client, addr)


import socket

host = '10.96.4.57'
port = 2323
FORMAT = 'utf-8'
EXIT = 'exit'
AD = (host, port)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# socket created with IPv4 and TCP features
s.bind(AD)


def rx(conn, addr):
    msg = conn.recv(1024).decode(FORMAT)
    print(f"[{addr}] : {msg}")
    return msg


def tx(conn):
    mesaj = input()
    conn.send(mesaj.encode(FORMAT))


#Program Starts
s.listen()
print(f"[LISTENING] Server is listening on {host}:{port}")
#Connection acceptance
client, addr = s.accept()
print(f"[NEW CONNECTION] {addr} connected.")
client.send("Welcome to the session".encode(FORMAT))


connection = True
while connection:
    msg = rx(client, addr)
    if msg == EXIT:
        connection = False
    

client.close()

import socket
import threading
import time

host = '10.96.7.207'
port = 2323
FORMAT = 'utf-8'
EXIT = 'exit'
AD = (host, port)
list_of_clients = []

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


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    conn.send("Welcome to this chatroom!".encode(FORMAT))
    
    flag = True
    while flag:
        mesaj = rx(conn, addr)
        broadcast(mesaj,conn)
        if mesaj == EXIT:
            flag = False
    conn.close()


def broadcast(message, connection):
    for clients in list_of_clients:
        if clients!=connection:
                clients.send(message)


def remove(connection):
    if connection in list_of_clients:
        list_of_clients.remove(connection)


#Program Starts
s.listen()
print(f"[LISTENING] Server is listening on {host}:{port}")
#Connection acceptance

while True:
    client, addr = s.accept()
    list_of_clients.append(client)
    thread = threading.Thread(target=handle_client, args=(client, addr))
    thread.start()
    print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")
    # name = client.recv(1024).decode(FORMAT)
    # print(f"{name} is in")
"""
her biri ismini gondersin, sonra da thread ve broadcast calis..
"""

# connection = True
# while connection:
#     msg = rx(client, addr)
#     if msg == EXIT:
#         connection = False
    

# client.close()

import socket
import select
import sys

host = '10.96.7.207'
port = 2323
FORMAT = 'utf-8'
EXIT = "exit"
AD = (host, port)

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect(AD)


s_message = c.recv(1024).decode(FORMAT)
print(s_message)


def tx(conn):
    mesaj = input()
    conn.send(mesaj.encode(FORMAT))
    return mesaj

while True:
    tx(c)

# connection = True
# while connection:
# 	tx_message = tx(c)
# 	if tx_message == EXIT:
# 		connection = False

# c.close

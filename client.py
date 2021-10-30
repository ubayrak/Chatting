import socket

host = '10.96.4.57'
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


connection = True
while connection:
	tx_message = tx(c)
	if tx_message == EXIT:
		connection = False

c.close

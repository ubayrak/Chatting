import socket

host = '10.96.7.207'
port = 2323
FORMAT = 'utf-8'
EXIT = "exit"
AD = (host, port)

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect(AD)

s_message = c.recv(1024).decode(FORMAT)
print(s_message)


# def send(msg):
# 	message = msg.encode(FORMAT)
# 	c.send(message)

while True:
	mesaj = input()
	emesaj = mesaj.encode(FORMAT)
	c.send(emesaj)



# send("Hello World!")
# input()
# send(EXIT)
# s_message = c.recv(1024).decode(FORMAT)
# print(s_message)









import socket

PORT = 5050 #above 1024
IP = "172.20.132.172"
FILE_NAME = "Cyber.jpg"

file = open(FILE_NAME,"rb")
file_content = file.read()

print(file_content)

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # DGARM - UDP || STREAM -TCP
server.bind((IP,PORT))
server.listen()
print(" waiting for clients")
conn,addr = server.accept()
print(addr)

conn.send(FILE_NAME.encode())
print(conn.recv(1024).decode())
conn.send(file_content)
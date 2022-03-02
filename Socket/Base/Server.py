import socket

PORT = 4444 #above 1024
IP = "172.20.147.166"


server = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # DGARM - UDP || STREAM -TCP
server.bind((IP,PORT))
server.listen()
print(" waiting for clients")
conn,addr = server.accept()
print(addr)

msg = conn.recv(1024).decode()
print(msg)

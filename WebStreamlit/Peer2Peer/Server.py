
import socket

PORT = 4444
SERVER = "172.20.129.27"

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind((SERVER,PORT))
server.listen()

print("SERVER is waiting for clients")

conn_obj, conn_address = server.accept()

print (f" The IP of Client is {conn_address}")

while True :
    data_receive = conn_obj.recv(1024).decode()
    print(f" the data received {data_receive}")

    #data_send = input("write text to send \n")
    conn_obj.send("OK".encode())



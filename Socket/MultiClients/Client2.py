
import socket

PORT = 5050
SERVER = "172.20.133.160"

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect((SERVER,PORT))

while True:
    data_receive = client.recv(1024).decode()
    print(f" the data received {data_receive}")


    client.send("Client2 received".encode())

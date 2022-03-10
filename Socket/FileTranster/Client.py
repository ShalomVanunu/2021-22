import socket

PORT = 5050
IP = "172.20.132.172"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((IP,PORT))

FILE_NAME =client.recv(1024).decode()

client.send("File name received".encode())

file = FILE_NAME.split(".")[0]

with open(file+"Copy.jpg","wb") as file:
    while True:
        data = client.recv(1024)
        if not data : # when data is exist
            break
        file.write(data)

client.close()


import socket

PORT = 4444
IP = "172.20.129.27"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((IP,PORT))
msg = input(" Enter Message :")
client.send(msg.encode())
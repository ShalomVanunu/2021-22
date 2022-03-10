import socket

PORT = 4444
IP = "172.20.132.172"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((IP,PORT))
msg = input(" Enter Message :")
client.send(msg.encode())
import socket

PORT = 5050 #above 1024
IP = "172.20.132.172"


server = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # DGARM - UDP || STREAM -TCP
server.bind((IP,PORT))
server.listen()
print(" waiting for clients")
conn,addr = server.accept()
print(f"The Client {addr} is Connected")

while True:
    msg = conn.recv(1024).decode()
    print(msg)
    if msg == "bye":
        break
    send_msg = input("Enter Msg :")
    conn.send(send_msg.encode())

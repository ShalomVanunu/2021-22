
import socket
import threading

PORT = 5050
SERVER = "172.20.133.160"
list_of_obj_clients = []
list_of_ip_clients = []

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind((SERVER,PORT))
server.listen()
print("SERVER is waiting for clients")

def connection():
    data_send = input(" write test to send to ALL clients \n")
    for conn_obj in list_of_obj_clients:
        conn_obj.send(data_send.encode())
        data_recieve = conn_obj.recv(1024).decode()
        print(f"{data_recieve}")

while True:
    conn_obj, conn_address = server.accept()
    list_of_ip_clients.append(conn_address)
    list_of_obj_clients.append(conn_obj)
    print(list_of_ip_clients)
    conn_thread = threading.Thread(target=connection)
    conn_thread.start()

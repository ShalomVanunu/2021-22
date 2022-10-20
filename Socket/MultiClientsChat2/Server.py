import socket
import threading

SERVER_IP = socket.gethostbyname(socket.gethostname())
PORT = 6060
clients_objects = []
usernames = []


def socket_init():
    server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM )
    server_socket.bind((SERVER_IP,PORT))
    server_socket.listen()
    print("Server is Waiting for Clients....")
    return server_socket

def thread_client_handle(client_object):
    while True:
        data_receive = client_object.recv(1024).decode()
        index = clients_objects.index(client_object)
        for client in clients_objects:
            if client != client_object:
                client.send(data_receive.encode())


def main():
    server_socket = socket_init() #return of socket object
    while True:
        client_object, client_ip = server_socket.accept()
        clients_objects.append(client_object)
        client_object.send("Welcome to Server".encode())
        usernames.append(client_object.recv(1024).decode())
        client_thread = threading.Thread(target=thread_client_handle ,args=(client_object,usernames))
        client_thread.start()

main()
import socket
import threading

SERVER_IP = "172.20.129.27"
PORT  = 6060

def client_socket_init():
    client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM )
    client_socket.connect((SERVER_IP,PORT))
    return client_socket

def receive(client_socket):
    print(client_socket.recv(1024).decode())

def send(client_socket):
    client_socket.send(input("Enter a message : ").encode())


def main():
    client_socket = client_socket_init()
    print(client_socket.recv(1024).decode())
    client_socket.send(input("Enter Username : ").encode())
    while True:
        client_socket.send(input("Enter a message : ").encode())
        print(client_socket.recv(1024).decode())
       # th_receive = threading.Thread(target=receive , args=(client_socket,))
       # th_receive.start()
       # th_send = threading.Thread(target=send , args=(client_socket,))
       # th_send.start()


main()

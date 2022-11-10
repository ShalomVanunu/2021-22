import socket

def socket_init():
    global client
    PORT = 4444
    IP = "172.20.129.27"

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((IP,PORT))
    return client

def send_data(data):
    client.send(data.encode())

def recv():
    return client.recv(1024).decode()

if __name__ == "__main__":
    socket_init()
    while True:
        msg = input(" Enter Message :")
        send_data(msg)
        print(recv())
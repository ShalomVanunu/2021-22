import streamlit as st
import socket

PORT = 4444
SERVER = "172.20.129.27"

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect((SERVER,PORT))


data = st.text_input("text")
click = st.button("Send")
#data_send = input("write text to send \n")
if click:
    print(data)
    client.send(data.encode())
data_receive = client.recv(1024).decode()
print(f" the data received {data_receive}")




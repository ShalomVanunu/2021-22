import threading

from flask import Flask, render_template,request, url_for, redirect
import Client
import threading
import socket

#th = threading.Thread(target=socket_init)
#th.start()

app = Flask(__name__) # open object of flask


def socket_init():
    global client
    PORT = 4444
    IP = "172.20.129.27"

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((IP,PORT))
    return client





@app.route("/",methods = ['GET','POST'] )
def main():
    client = threading.Thread(target=socket_init)
    client.start()

    if request.method =="POST":
        data = request.form["data"]
        client.send(data.encode())
        print(data)
        print(client)
        return render_template("Chat.html")
    else:
        return render_template("Chat.html")





if __name__ == "__main__":
    app.run(port =80, host="0.0.0.0",debug=True)
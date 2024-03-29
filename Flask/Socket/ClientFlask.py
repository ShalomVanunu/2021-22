from flask import Flask, render_template,request, url_for, redirect
import Client
import threading
import socket



th = threading.Thread(target=Client.socket_init)
th.start()

app = Flask(__name__) # open object of flask

@app.route("/",methods = ['GET','POST'] )
def main():
    global client

    if request.method =="POST":
        data = request.form["data"]
        Client.send_data(data)
        msg = Client.recv()
        print(msg)
        return render_template("Chat.html", content=msg)
    else:
        return render_template("Chat.html")





if __name__ == "__main__":
    app.run(port =80, host="172.20.129.27")
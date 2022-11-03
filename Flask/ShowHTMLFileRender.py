
from flask import Flask, render_template

app = Flask(__name__) # open object of flask

@app.route("/")
def sport():
    return render_template("Sport.html")

@app.route("/welcome")
def welcome():
    return "<h1> Welcome </h1>"

if __name__ == "__main__":
    app.run(port =80, host="0.0.0.0", debug=True)


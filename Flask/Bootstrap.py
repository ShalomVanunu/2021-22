
from flask import Flask, render_template

app = Flask(__name__) # open object of flask

@app.route("/")
def sport():
    return render_template("Input.html")

if __name__ == "__main__":
    app.run(port =80, host="0.0.0.0", debug=True)


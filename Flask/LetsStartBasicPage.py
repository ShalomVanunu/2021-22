from flask import Flask

app = Flask(__name__) # open object of flask

@app.route("/sport")
def sport():
    return "<h1> Hello Page Sport</h1>"

@app.route("/")
def home():
    return "<h1> Hello Class. Got to /sport</h1>"

if __name__ == "__main__":
    app.run(port =8080, host="0.0.0.0")


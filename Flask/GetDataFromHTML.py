
from flask import Flask, render_template,request

app = Flask(__name__) # open object of flask

@app.route("/", methods=['GET', 'POST'])
def sport():
    if request.method == "POST":
        print(request.form["user"])
        return render_template("Input.html")
    else:
        return render_template("Input.html")

if __name__ == "__main__":
    app.run(port =80, host="0.0.0.0", debug=True)


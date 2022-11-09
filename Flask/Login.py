from flask import Flask, render_template,request, url_for, redirect


app = Flask(__name__) # open object of flask

@app.route("/",methods = ['GET','POST'] )
def main():
    if request.method =="POST":
        username = request.form["username"]
        password = request.form["password"]
        if username == 'shalomv' and password=='Password1':
            #return redirect(url_for('success'))
            return render_template("Success.html")
        else:
            return render_template("Login.html")

    else:
        return render_template("Login.html")


@app.route("/success")
def success():
    return "<h1> Login Success </h1>"



if __name__ == "__main__":
    app.run(port =80, host="0.0.0.0",debug=True)


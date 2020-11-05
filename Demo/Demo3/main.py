from flask import Flask
from flask import render_template

app = Flask ("Hello world")


@app.route("/index")
def index ():
    return render_template("index.html")


@app.route("/index1")
def index1 ():
    return render_template("index.html")


if __name__ == "__main__":
 app.run(debug=True, port=5000)

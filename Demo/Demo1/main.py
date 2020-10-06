from flask import Flask, render_template

app = Flask("Hello World")


@app.route('/index')
def hello_world():
    return render_template("index.html", name = "Vincent")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
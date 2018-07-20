from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("inherit.html")

@app.route("/more")
def more():
    return render_template("more.html")

@app.route("/dynamic")
def dynamic():
    return render_template("dynamic.html")

@app.route("/hello", methods=["GET", "POST"])
def hello():
    if request.method == "GET":
        return render_template("hello1.html")
    else:
        name = request.form.get("name")
        return render_template("hello.html", name=name)

if __name__ == '__main__':
    app.run(debug=True)

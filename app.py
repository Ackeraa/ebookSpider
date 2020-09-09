from flask import Flask, redirect, render_template, request

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def search():
    if request.method == "GET":
        return render_template("index.html") 
    else:
        keywords = request.form.get("keywords")
        return render_template("result.html", keywords = keywords)

@app.route("/add", methods = ["GET", "POST"])
def add():
    if request.method == "GET":
        return render_template("add.html")
    else:
        return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)



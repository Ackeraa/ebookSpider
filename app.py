from flask import Flask, redirect, render_template, request
from Crawler import Crawler

app = Flask(__name__)

crawler = Crawler()

@app.route("/", methods = ["GET", "POST"])
def search():
    global crawler
    if request.method == "GET":
        return render_template("index.html") 
    else:
        keywords = request.form.get("keywords")
        books = crawler.craw(keywords)
        return render_template("result.html", books = books)

@app.route("/download", methods = ["GET", "POST"])
def download():
    global crawler
    link = crawler.download(request.args.get("link"))
    return render_template("preview.html", link = link)

if __name__ == '__main__':
    app.run(debug=True)


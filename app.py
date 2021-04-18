from flask import Flask, redirect, render_template, request
from Spider import Spider

app = Flask(__name__)

spider = Spider()

@app.route("/", methods = ["GET", "POST"])
def search():
    global spider
    if request.method == "GET":
        return render_template("index.html") 
    else:
        keywords = request.form.get("keywords")
        books = spider.craw(keywords)
        return render_template("result.html", books = books)

@app.route("/preview", methods = ["GET", "POST"])
def preview():
    global spider
    link = spider.download(request.args.get("link"))
    return render_template("preview.html", link = link)

@app.route("/download", methods = ["GET", "POST"])
def download():
    global spider
    link = spider.download(request.args.get("link"))
    print("*******************", link, "*******************")
    return render_template("preview.html", link = link)

if __name__ == '__main__':
    app.run(debug=True)


from flask import Flask, render_template
import scraper
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", data=scraper.news())


if __name__ == "__main__":
    app.run(debug=True)
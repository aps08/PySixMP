from flask import Flask, render_template
import scraper
app = Flask(__name__)


@app.route("/")
def index():
    """ This API is responsible for showing the first page and populating the page with data from scraper file.

    Returns:
        return a html template when anyone triggers the root of the server.
    """
    return render_template("index.html", data=scraper.news())


if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template, redirect, url_for, flash
from forms import BookmarkForm

app = Flask(__name__)
app.config['SECRET_KEY'] = b'\xae\xb3\xc5\xbb\x8f\xb3\xea\x1a\xcd\xc4\xd1De=\x1b\xfb'
bookmarks = [
    {
        "user": "Bridget Jones's Diary",
        "url": "2001",
        "description": "Sharon Maguire"
    },
    {
        "user": "Schindler's List",
        "url": "1993",
        "description": "Steven Spielberg"
    },
    {
        "user": "Serial Bad Weddings",
        "url": "2014",
        "description": "Philippe de Chauveron"
    }
]


def get_latest_bookmarks(limit):
    return bookmarks[:limit]


@app.route("/")
@app.route("/index2")
def index():
    return render_template("index.html", bookmarks=get_latest_bookmarks(5))


@app.route("/add", methods=['GET', 'POST'])
def add():
    form = BookmarkForm()
    if form.validate_on_submit():
        url = form.url.data
        description = form.description.data
        bm = {
            "user": "The Polar Express",
            "url": url,
            "description": description
        }
        bookmarks.append(bm)
        flash(f"Stored {description}")
        return redirect(url_for('index'))
    return render_template('add.html', form=form)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500


if __name__ == "__main__":
    app.run(debug=True)

from datetime import date
from flask import Flask, abort, render_template, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('FLASK_KEY')
ckeditor = CKEditor(app)
Bootstrap5(app)

godina = date.today().year
print(godina)

@app.route('/')
def home():
    return render_template("index.html", godina=godina)

@app.route("/about")
def about():
    return render_template("about.html", godina=godina)


@app.route("/contact")
def contact():
    return render_template("contact.html", godina=godina)


if __name__ == "__main__":
    app.run(debug=True, port=5002)
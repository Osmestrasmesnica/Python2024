from flask import Flask, render_template
import datetime
import requests

app = Flask(__name__)
blog_data_url = "https://gist.githubusercontent.com/gellowg/389b1e4d6ff8effac71badff67e4d388/raw/fc31e41f8e1a6b713eafb9859f3f7e335939d518/data.json"
response = requests.get(blog_data_url)
posts = response.json()

current_year = datetime.date.today().year

@app.route('/')
def get_all_posts():
    return render_template("index.html", current_year=current_year, all_posts = posts)

@app.route("/about")
def about():
    return render_template("about.html", current_year=current_year)

@app.route("/contact")
def contact():
    return render_template("contact.html", current_year=current_year)

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
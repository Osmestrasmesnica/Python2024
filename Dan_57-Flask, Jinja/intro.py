from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)



@app.route('/')
def home():
    random_number = random.randint(1, 10)
    current_year = datetime.date.today().year
    username = "WLQ Innovations"
    return render_template('index.html', num=random_number, current_year=current_year, name = username)

@app.route("/guess/<name>")
def api_data(name):
    agify_url = f"https://api.agify.io?name={name}"
    genderfy_url = f"https://api.genderize.io?name={name}"
    responese = requests.get(agify_url)
    age_data = responese.json()
    age = age_data["age"]
    response2 = requests.get(genderfy_url)
    gender_data = response2.json()
    gender = gender_data["gender"]
    return render_template('agify.html', name = name, age = age, gender = gender)

@app.route("/blog/<number>")
def get_blog(number):
    print(number)
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template('blog.html', posts = all_posts)

if __name__ == "__main__":
    app.run(debug=True)



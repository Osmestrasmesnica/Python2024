from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
import os
from dotenv import load_dotenv

load_dotenv()

TMDB_MOVIE_API_READ_ACCESS_TOKEN = os.getenv("TMDB_MOVIE_API_READ_ACCESS_TOKEN")
TMDB_MOVIE_API_KEY = os.getenv("TMDB_MOVIE_API_KEY")

MOVIE_DB_IMAGE_URL = "https://image.tmdb.org/t/p/original"

url = "https://api.themoviedb.org/3/search/movie"
url_with_id = "https://api.themoviedb.org/3/movie"

# Determine the base directory of your application
base_dir = os.path.abspath(os.path.dirname(__file__))

# Specify the relative path to the directory where you want to store the database
db_dir = os.path.join(base_dir, 'instances')

# Ensure that the directory exists, if not create it
os.makedirs(db_dir, exist_ok=True)

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# CREATE DB
class Base(DeclarativeBase):
    pass

# Set the URI with the relative path
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(db_dir, 'top10-filmovi.db')}"

# Create the extension
db = SQLAlchemy(model_class=Base)

# Initialise the app with the extension
db.init_app(app)

# CREATE TABLE
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year:Mapped[int] = mapped_column(Integer, nullable=False)
    description:Mapped[str] = mapped_column(String(500), nullable=False)
    rating:Mapped[float] = mapped_column(Float, nullable=True)
    ranking:Mapped[int] = mapped_column(Integer, nullable=True)
    review:Mapped[str] = mapped_column(String(250), nullable=True)
    img_url:Mapped[str] = mapped_column(String(250), nullable=False )

# Create table schema in the database. Requires application context.
with app.app_context():
    db.create_all()

# new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )
    
# second_movie = Movie(
#     title="Avatar The Way of Water",
#     year=2022,
#     description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
#     rating=7.3,
#     ranking=9,
#     review="I liked the water.",
#     img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
# )

# with app.app_context():
#     db.session.add(new_movie)
#     db.session.commit()

class RateMovieForm(FlaskForm):
    rating = StringField("Your Rating Out of 10 e.g. 7.5")
    review = StringField("Your Review")
    submit = SubmitField("Done")

class AddMovieForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")

@app.route("/")
def home():
    result = db.session.execute(db.select(Movie).order_by(Movie.rating))
    movies = result.scalars().all() #TODO proveri sto se stavlja ovde all, radilo je i bez njega ok
    #info .all() prevara result.scalars() u listu tak oda mozemo kasnije da koristim indeksiranje ili count,len..
    for i in range(len(movies)):
        movies[i].ranking = len(movies) - i
    return render_template("index.html", movies=movies)

@app.route("/edit", methods=["GET", "POST"])
def edit():
    form = RateMovieForm()
    movie_id = request.args.get('id')
    movie = db.get_or_404(Movie, movie_id)
    if form.validate_on_submit():
        movie.rating = float(form.rating.data)
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", form=form, movie=movie)

@app.route("/delete", methods=["GET", "POST"])
def delete():
    movie_id = request.args.get('id')
    movie_to_delete = db.get_or_404(Movie, movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))

# @app.route("/add", methods=["GET", "POST"])
# def add():
#     form = AddMovieForm()
#     if form.validate_on_submit():
#         title = form.title.data
#         headers = {
#             "accept": "application/json",
#             "Authorization": f"Bearer {TMDB_MOVIE_API_READ_ACCESS_TOKEN}"
#         }

#         parameters = {
#             "query": title,
#             "api_key": TMDB_MOVIE_API_KEY,
#             "include_adult": True,
#             "page": 1
#         }

#         response = requests.get(url, params=parameters, headers=headers)
#         data = response.json()["results"]

#         print(response.text)
#         return redirect(url_for("select", films=data))  # Redirect to the home page after successful form submission
#     return render_template("add.html", form=form)  # Render the form template

@app.route("/add", methods=["GET", "POST"])
def add_movie():
    form = AddMovieForm()
    
    if form.validate_on_submit():
        movie_title = form.title.data
        response = requests.get(url, params={"api_key": TMDB_MOVIE_API_KEY, "query": movie_title, "include_adult": False})
        data = response.json()["results"]
        return render_template("select.html", options=data)
      
    return render_template("add.html", form=form)

@app.route("/select")
def select():
    films = request.args.get('films')
    return render_template("select.html", films=films)

@app.route("/find")
def find_movie():
    movie_api_id = request.args.get("id")
    if movie_api_id:
        movie_api_url = f"{url_with_id}/{movie_api_id}"
        response = requests.get(movie_api_url, params={"api_key": TMDB_MOVIE_API_KEY, "language": "en-US"})
        data = response.json()
        new_movie = Movie(
            title=data["title"],
            year=data["release_date"].split("-")[0],
            img_url=f"{MOVIE_DB_IMAGE_URL}{data['poster_path']}",
            description=data["overview"],
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for("edit", id=new_movie.id))




if __name__ == '__main__':
    app.run(debug=True)

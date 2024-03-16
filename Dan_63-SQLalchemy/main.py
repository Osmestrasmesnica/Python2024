from flask import Flask, render_template, redirect, url_for, request
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap5
from wtforms import StringField, SubmitField
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
import os

# Determine the base directory of your application
base_dir = os.path.abspath(os.path.dirname(__file__))

# Specify the relative path to the directory where you want to store the database
db_dir = os.path.join(base_dir, 'instances')

# Ensure that the directory exists, if not create it
os.makedirs(db_dir, exist_ok=True)

app = Flask(__name__)


app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

##CREATE DATABASE
class Base(DeclarativeBase):
    pass

# Set the URI with the relative path
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(db_dir, 'knjige.db')}"

# Create the extension
db = SQLAlchemy(model_class=Base)

# Initialise the app with the extension
db.init_app(app)

##CREATE TABLE
class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

# Create table schema in the database. Requires application context.
with app.app_context():
    db.create_all()

class AddBookForm(FlaskForm):
    book_name = StringField("Book Name", validators=[DataRequired()])
    book_author = StringField("Book Author", validators=[DataRequired()])
    book_rating = StringField("Book Rating", validators=[DataRequired()])
    submit = SubmitField('Add Book')

@app.route('/')
def home():
    ##READ ALL RECORDS
    # Construct a query to select from the database. Returns the rows in the database
    result = db.session.execute(db.select(Book))
    # Use .scalars() to get the elements rather than entire rows from the database
    all_books = list(result.scalars())    
    # # Determine if the list of books is empty
    # is_empty = len(list(all_books)) == 0
    return render_template ("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddBookForm()
    if form.validate_on_submit():

        # CREATE RECORD
        new_book = Book(
            title=form.book_name.data,
            author=form.book_author.data,
            rating=form.book_rating.data,
        )

        db.session.add(new_book)
        db.session.commit()

        return redirect(url_for("home"))  # Redirect to the home page after successful form submission
    return render_template("add.html", form=form)  # Render the form template

#note ako se ne koristi AddBookForm vec forma koja postoji onda je ovo kod ok ispod
# @app.route("/add", methods=["GET", "POST"])
# def add():
#     if request.method == "POST":
#         new_book = {
#             "title": request.form["title"],
#             "author": request.form["author"],
#             "rating": request.form["rating"]
#         }
#         all_books.append(new_book)
        
#         #: You can use the redirect method from flask to redirect to another route 
#         # e.g. in this case to the home page after the form has been submitted.
#         return redirect(url_for('home'))
      
#     return render_template("add.html")

@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        #UPDATE RECORD
        book_id = request.form["id"]
        book_to_update = db.get_or_404(Book, book_id)
        book_to_update.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for('home'))
    book_id = request.args.get('id')
    book_selected = db.get_or_404(Book, book_id)
    return render_template("edit_rating.html", book=book_selected)

@app.route("/delete", methods=["GET", "POST"])
def delete():
    book_id = request.args.get('id')
    # DELETE A RECORD BY ID
    book_to_delete = db.get_or_404(Book, book_id)
    # Alternative way to select the book to delete.
    # book_to_delete = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)


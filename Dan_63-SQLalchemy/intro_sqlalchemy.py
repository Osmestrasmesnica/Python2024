from flask import Flask
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

##CREATE DATABASE
class Base(DeclarativeBase):
    pass

# Set the URI with the relative path
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(db_dir, 'nove_knjige.db')}"

# Set the URI with the relative path
# app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///nove_knjige.db"


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

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'


# Create table schema in the database. Requires application context.
with app.app_context():
    db.create_all()

# # CREATE RECORD
# with app.app_context():
#     new_book = Book(id=3, title="Murder on the Orient Express", author="Agatha Christie", rating=7)
#     db.session.add(new_book)
#     db.session.commit()

#! CRUD

# #! Create A New Record
# with app.app_context():
#     new_book = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3)
#     db.session.add(new_book)
#     db.session.commit()
# #NOTE: When creating new records, the primary key fields is optional. you can also write and the id field will be auto-generated.
# new_book = Book(title="Harry Potter", author="J. K. Rowling", rating=9.3)


# #! Read All Records
# with app.app_context():
#     result = db.session.execute(db.select(Book).order_by(Book.title))
#     all_books = result.scalars()
#     for book in all_books:
#         print(book.title, book.author, book.rating)
# # To read all the records we first need to create a "query" to select things from the database. When we execute a query during a database session we get back the rows in the database (a Result object). We then use scalars() to get the individual elements rather than entire rows.

# #! Read A Particular Record By Query
# with app.app_context():
#     book = db.session.execute(db.select(Book).where(Book.title == "Harry Potter")).scalar()
#     print(book.title, book.author, book.rating)
# # To get a single element we can use scalar() instead of scalars().

# #! Update A Particular Record By Query
# with app.app_context():
#     book_to_update = db.session.execute(db.select(Book).where(Book.title == "Harry Potter 2")).scalar()
#     book_to_update.rating = 10
#     db.session.commit() 
    
# #! Update A Record By PRIMARY KEY
# book_id = 1
# with app.app_context():
#     book_to_update = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
#     # or book_to_update = db.get_or_404(Book, book_id)  
#     book_to_update.rating = 10
#     db.session.commit()  
# # Flask-SQLAlchemy also has some handy extra query methods like get_or_404() that we can use. Since Flask-SQLAlchemy version 3.0 the previous query methods like Book.query.get() have been deprecated
    
# #! Delete A Particular Record By PRIMARY KEY
# book_id = 1
# with app.app_context():
#     book_to_delete = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
#     # or book_to_delete = db.get_or_404(Book, book_id)
#     db.session.delete(book_to_delete)
#     db.session.commit()
# # You can also delete by querying for a particular value e.g. by title or one of the other properties. Again, the get_or_404() method is quite handy.
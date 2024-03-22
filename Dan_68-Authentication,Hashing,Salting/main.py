from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'

# Determine the base directory of your application
base_dir = os.path.abspath(os.path.dirname(__file__))

# Specify the relative path to the directory where you want to store the database
db_dir = os.path.join(base_dir, 'instance')

# Ensure that the directory exists, if not create it
os.makedirs(db_dir, exist_ok=True)

# CREATE DATABASE
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(db_dir, 'users.db')}"
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# Configure Flask-Login's Login Manager
login_manager = LoginManager()
login_manager.init_app(app)

# Create a user_loader callback
@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)

# CREATE TABLE IN DB with the UserMixin
class User(UserMixin, db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(100))
 
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    # Passing True or False if the user is authenticated. 
    return render_template("index.html", logged_in=current_user.is_authenticated)


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form.get('email')
        result = db.session.execute(db.select(User).where(User.email == email))
        # Note, email in db is unique so will only have one result.
        user = result.scalar()
        if user:
            # User already exists
            flash("You've already signed up with that email, log in instead!")
            return redirect(url_for('login'))

        new_user = User(
            email=request.form.get('email'),
            name=request.form.get('name'),
            # Hashing and salting the password entered by the user
            password=generate_password_hash(request.form.get('password'), method="pbkdf2:sha256", salt_length=8)
        )
        
        db.session.add(new_user)
        db.session.commit()
        
        # Log in and authenticate user after adding details to the database
        login_user(new_user)

        return render_template("secrets.html", user = new_user.name)

    return render_template("register.html", logged_in=current_user.is_authenticated)


@app.route('/login', methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        # Find user by email entered.
        # user = User.query.filter_by(email=email) #note --> more common and convenient way to query data using SQLAlchemy ORM (Object-Relational Mapping)
        result = db.session.execute(db.select(User).where(User.email==email))
        user = result.scalar() #note --> is more suitable for cases where you need to write custom SQL queries or handle complex database operations.

        # Email doesn't exist or password incorrect.
        if not user:
            flash("That email does not exist, please try again or register.")
            return redirect(url_for('login'))
        elif not check_password_hash(user.password, password):
            flash('Password incorrect, please try again.')
            return redirect(url_for('login'))
        else:
            login_user(user)
            return redirect(url_for('secrets'))
        
    return render_template("login.html", logged_in=current_user.is_authenticated)

# Only logged-in users can access the route
@app.route('/secrets')
@login_required
def secrets():
    print(current_user.name)
    # Passing the name from the current_user
    return render_template("secrets.html", user=current_user.name, logged_in=True)

@app.route('/logout')
def logout():
    logout_user()
    return render_template("index.html")

# Only logged-in users can down download the pdf
@app.route('/download')
@login_required
def download():
    return send_from_directory("static", path="files/cheat_sheet.pdf")



if __name__ == "__main__":
    app.run(debug=True)

from datetime import date
from flask import Flask, abort, render_template, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from flask_gravatar import Gravatar
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text, ForeignKey
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
import os
# Import your forms from the forms.py
from forms import CreatePostForm, RegisterForm, LoginForm, CommentForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap5(app)

# TODO: Configure Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)

# Create a user_loader callback
@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)

# Determine the base directory of your application
base_dir = os.path.abspath(os.path.dirname(__file__))

# Specify the relative path to the directory where you want to store the database
db_dir = os.path.join(base_dir, 'instance')

# Ensure that the directory exists, if not create it
os.makedirs(db_dir, exist_ok=True)

# CREATE DATABASE
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(db_dir, 'posts.db')}"
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CONFIGURE TABLES
class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    # author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

    # Create Foreign Key, "users.id" the users refers to the tablename of User.
    author_id: Mapped[int] = mapped_column(Integer, db.ForeignKey("users.id"))
    # author_id: Mapped[int] = mapped_column(ForeignKey('users.id') )
    # Create reference to the User object. The "posts" refers to the posts property in the User class.
    author = relationship("User", back_populates="posts")

    #Parent Relationship
    comments = relationship("Comment", back_populates="parent_post")

# TODO: Create a User table for all your registered users. 
class User(UserMixin, db.Model):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(100), nullable=False)

    #This will act like a List of BlogPost objects attached to each User. 
    #The "author" refers to the author property in the BlogPost class.
    posts = relationship("BlogPost", back_populates="author")
    # posts: Mapped[List[BlogPost]] = relationship("BlogPost", back_populates="author", lazy="dynamic")

    # Add parent relationship 
    #"comment_author" refers to the comment_author property in the Comment class.
    comments = relationship("Comment", back_populates="comment_author")
    # comments: Mapped[List["Comment"]] = relationship("Comment", back_populates="comment_author")

# TODO: Create a Comment table.
class Comment(db.Model):
    __tablename__ = "comments"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    text: Mapped[str] = mapped_column(Text, nullable=False)

    # Add child relationship
    #"users.id" The users refers to the tablename of the Users class.
    #"comments" refers to the comments property in the User class.
    author_id: Mapped[int] = mapped_column(Integer, db.ForeignKey("users.id"))
    comment_author = relationship("User", back_populates="comments")

    #Child Relationship
    post_id: Mapped[int] = mapped_column(Integer, db.ForeignKey("blog_posts.id"))
    parent_post = relationship("BlogPost", back_populates="comments")



with app.app_context():
    db.create_all()

godina = date.today().year
print(godina)

# For adding profile images to the comment section
gravatar = Gravatar(app,
                    size=100,
                    rating='g',
                    default='retro',
                    force_default=False,
                    force_lower=False,
                    use_ssl=False,
                    base_url=None)

#Create admin-only decorator
def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        #If id is not 1 and if no one is logged in then return abort with 403 error
        if current_user.is_authenticated and current_user.id == 1:
            return f(*args, **kwargs)
        #Otherwise continue with the route function
        return abort(403)        
    return decorated_function

# TODO: Use Werkzeug to hash the user's password when creating a new user.
@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        email = form.email.data
        username = form.username.data
        password_to_hash = form.password.data

        # Check if user already exists (email or username).
        existing_user = User.query.filter((User.email == email) | (User.username == username)).first()

        if existing_user:
            if existing_user.email == email:
                # User already registered with this email
                flash("You've already signed up with that email, log in instead!", "error")
                return redirect(url_for('login', godina=godina))
            elif existing_user.username == username:
                # Username already in use
                flash("This username is already taken. Please choose a different one.", "error")
                return redirect(url_for('register', godina=godina))

        # Create new user
        new_user = User(
            username=username,
            email=email,
            password=generate_password_hash(password_to_hash, method="pbkdf2:sha256", salt_length=8)
        )

        # Adding new user to the database
        db.session.add(new_user)
        db.session.commit()

        # Log in and authenticate user with Flask-Login after adding details to the database
        login_user(new_user)

        flash("Registration successful!", "success")
        return redirect(url_for("get_all_posts", godina=godina))

    return render_template("register.html", form=form, godina=godina, logged_in=current_user.is_authenticated)



# TODO: Retrieve a user from the database based on their email. 
@app.route('/login', methods = ["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        result = db.session.execute(db.select(User).where(User.email == email))
        # Note, email in db is unique so will only have one result.
        user = result.scalar()
        
        # Email doesn't exist
        if not user:
            flash("That email does not exist, please try again.")
            return redirect(url_for('login'))
        # Password incorrect
        elif not check_password_hash(user.password, password):
            flash('Password incorrect, please try again.')
            return redirect(url_for('login'))
        else:
            login_user(user)
            return redirect(url_for('get_all_posts'))
        
    return render_template("login.html", form=form, logged_in=current_user.is_authenticated)


@app.route('/logout', methods = ["GET", "POST"])
def logout():
    logout_user()
    return redirect(url_for('get_all_posts'))


@app.route('/')
def get_all_posts():
    result = db.session.execute(db.select(BlogPost).order_by(BlogPost.date))
    posts = result.scalars().all()
    return render_template("index.html", all_posts=posts, godina=godina, logged_in=current_user.is_authenticated)
#note Everytime you call render_template(), you pass the current_user over to the template.
#note This will mean the nav bar will always show the correct options.
#note current_user.is_authenticated will be True if they are logged in/authenticated after registering.
#note You can check for this is header.html

# TODO: Allow logged-in users to comment on posts
@app.route("/post/<int:post_id>", methods = ["GET", "POST"])
def show_post(post_id):
    form = CommentForm()
    requested_post = db.get_or_404(BlogPost, post_id)
    if form.validate_on_submit():
        if not current_user.is_authenticated:
            flash("You must be logged in to comment!", "error")
            return redirect(url_for("login"))
        
        new_comment = Comment(
            text=form.comment_text.data,
            comment_author=current_user,
            parent_post=requested_post
        )

        db.session.add(new_comment)
        db.session.commit()

    return render_template("post.html", form=form, post=requested_post, godina=godina, logged_in=current_user.is_authenticated, current_user=current_user)


# TODO: Use a decorator so only an admin user can create a new post
@app.route("/new-post", methods=["GET", "POST"])
@admin_only
def add_new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=form.img_url.data,
            author=current_user,
            date=date.today().strftime("%B %d, %Y")
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts", godina=godina))
    return render_template("make-post.html", form=form, godina=godina, logged_in=current_user.is_authenticated)


# TODO: Use a decorator so only an admin user can edit a post
@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
@admin_only
def edit_post(post_id):
    post = db.get_or_404(BlogPost, post_id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body
    )
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.author = current_user
        post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id, godina=godina))
    return render_template("make-post.html", form=edit_form, is_edit=True, godina=godina, logged_in=current_user.is_authenticated)


# TODO: Use a decorator so only an admin user can delete a post
@app.route("/delete/<int:post_id>")
@admin_only
def delete_post(post_id):
    post_to_delete = db.get_or_404(BlogPost, post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


@app.route("/about")
def about():
    return render_template("about.html", godina=godina, logged_in=current_user.is_authenticated)


@app.route("/contact")
def contact():
    return render_template("contact.html", godina=godina, logged_in=current_user.is_authenticated)


if __name__ == "__main__":
    app.run(debug=True, port=5002)

from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date
import os
import bleach
 
## strips invalid tags/attributes
def strip_invalid_html(content):
    allowed_tags = ['a', 'abbr', 'acronym', 'address', 'b', 'br', 'div', 'dl', 'dt',
                    'em', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'hr', 'i', 'img',
                    'li', 'ol', 'p', 'pre', 'q', 's', 'small', 'strike',
                    'span', 'sub', 'sup', 'table', 'tbody', 'td', 'tfoot', 'th',
                    'thead', 'tr', 'tt', 'u', 'ul']
 
    allowed_attrs = {
        'a': ['href', 'target', 'title'],
        'img': ['src', 'alt', 'width', 'height'],
    }
 
    cleaned = bleach.clean(content,
                           tags=allowed_tags,
                           attributes=allowed_attrs,
                           strip=True)
 
    return cleaned
 
# ## use strip_invalid_html-function before saving body
# body=strip_invalid_html(article.body.data)

app = Flask(__name__)

app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
# Initialise the CKEditor so that you can use it in make_post.html
ckeditor = CKEditor(app)
Bootstrap5(app)

# Determine the base directory of your application
base_dir = os.path.abspath(os.path.dirname(__file__))

# Specify the relative path to the directory where you want to store the database
db_dir = os.path.join(base_dir, 'instance')

# Ensure that the directory exists, if not create it
os.makedirs(db_dir, exist_ok=True)

# CREATE DATABASE
class Base(DeclarativeBase):
    pass
# Set the URI with the relative path
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(db_dir, 'posts.db')}"
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()
    
godina = date.today().year
print(godina)

##WTForm ovo moze da stoji i u posebnom .py pa da se importuje
class NewBlog(FlaskForm):
    title = StringField("Blog Title", validators=[DataRequired()])
    subtitle = StringField("Blog Subtitle", validators=[DataRequired()])
    author = StringField("Blog Author", validators=[DataRequired()])
    bg_url = StringField("Background Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Body", validators=[DataRequired()])
    submit = SubmitField("Submit")


@app.route('/')
def get_all_posts():
    # TODO: Query the database for all the posts. Convert the data to a python list.
    result = db.session.execute(db.select(BlogPost).order_by(BlogPost.date))
    posts = result.scalars().all()
    return render_template("index.html", all_posts=posts, godina=godina)

# TODO: Add a route so that you can click on individual posts.
@app.route('/post/<int:post_id>')
def show_post(post_id):
    # TODO: Retrieve a BlogPost from the database based on the post_id
    requested_post = db.get_or_404(BlogPost, post_id)
    return render_template("post.html", post=requested_post, godina=godina)

# TODO: add_new_post() to create a new blog post
@app.route("/new-post", methods=['GET', 'POST'])
def add_new_post():
    form = NewBlog()
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=strip_invalid_html(form.body.data),
            img_url=form.bg_url.data,
            author=form.author.data,
            date=date.today().strftime("%B %d, %Y")
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts", godina=godina))
    return render_template("make-post.html", form=form, godina=godina)

# TODO: edit_post() to change an existing blog post
@app.route("/edit-post/<int:id>", methods=['GET', 'POST'])
def edit_post(id):
    post = db.get_or_404(BlogPost, id)
    edit_form = NewBlog(
        title=post.title,
        subtitle=post.subtitle,
        author=post.author,
        bg_url=post.img_url,
        body=post.body
    )
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.author = edit_form.author.data
        post.img_url = edit_form.bg_url.data
        post.body = strip_invalid_html(edit_form.body.data)
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id, godina=godina))
    return render_template("make-post.html", form=edit_form, is_edit=True, godina=godina)

# TODO: delete_post() to remove a blog post from the database
@app.route("/delete-post/<int:id>")
def delete_post(id):
    post_to_delete = db.get_or_404(BlogPost, id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for("get_all_posts", godina=godina))

# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html", godina=godina)


@app.route("/contact")
def contact():
    return render_template("contact.html", godina=godina)


if __name__ == "__main__":
    app.run(debug=True, port=5003)

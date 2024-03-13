from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,EmailField,SubmitField
from wtforms.validators import DataRequired, Length, Email
from flask_bootstrap import Bootstrap5

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''
app = Flask(__name__)
bootstrap = Bootstrap5(app) # initialise bootstrap-flask
app.secret_key = "any-string-you-want-just-keep-it-secret"

class LoginForm(FlaskForm):
    email = EmailField(label='Email', validators=[DataRequired(), Length(min=5), Email(message="Niste uneli ispravan mail")])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label='Log in')

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    adresa = login_form.email.data
    lozinka = login_form.password.data
    if login_form.validate_on_submit():
        if login_form.email.data == "admin@email.com" and login_form.password.data == "12345678":
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=login_form)

if __name__ == '__main__':
    app.run(debug=True)

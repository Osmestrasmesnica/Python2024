from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,SelectField, URLField,TimeField
from wtforms.validators import DataRequired, URL
import csv

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
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------

coffee_choices = [('0', '✘')] + [(str(i), '☕️' * i) for i in range(1, 6)]
wifi_choices = [('0', '✘')] + [(str(i), '💪' * i) for i in range(1, 6)]
power_choices = [('0', '✘')] + [(str(i), '🔌' * i) for i in range(1, 6)]

class CafeForm(FlaskForm):
    cafe = StringField('Naziv Kafića', validators=[DataRequired()])
    location = StringField('Lokacija Kafića Na Google Maps (URL)', validators=[DataRequired(), URL()])
    open_time = TimeField('Otvarnaje', validators=[DataRequired()])
    closing_time = TimeField('Zatvaranje', validators=[DataRequired()])
    coffee_rating = SelectField("Kvalitet Kafe", choices=["☕️", "☕☕", "☕☕☕", "☕☕☕☕", "☕☕☕☕☕"], validators=[DataRequired()])
    wifi_rating = SelectField("Jačina Wifi Signala", choices=["✘", "💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"], validators=[DataRequired()])
    power_outlet_rating = SelectField("Dostnost Utičnice", choices=["✘", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"], validators=[DataRequired()])
    submit = SubmitField('Submit')

# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")

#TODO OVO NEKADA POGLEDATI STA SI OVO BRLJAO I STO SI GA TOLIKO ISKOMPLIKOVAO
# @app.route('/add', methods=['GET', 'POST'])
# def add_cafe():
#     form = CafeForm()
#     if form.validate_on_submit():
#         # Extract data from form fields
#         #! ne zaboraviti da se izbaci submit dugme field.name != 'submit'
#         # data = [getattr(form, field.name).data for field in form if field.name != 'submit']
#         data = []
#         for field in form:
#             # Skip the submit button
#             if field.name == 'submit':
#                 continue
            
#             # Format data based on field type
#             if isinstance(field, SelectField):
#                 rating = int(field.data)  # Convert rating to integer
#                 if rating == 0:
#                     emoji = '✘'
#                     data.append(emoji)
#                 elif field.name == 'coffee_rating':
#                     emoji = '☕️'
#                     data.append(emoji * rating)
#                 elif field.name == 'wifi_rating':
#                     emoji = '💪'
#                     data.append(emoji * rating)
#                 elif field.name == 'power_outlet_rating':
#                     emoji = '🔌'
#                     data.append(emoji * rating)
#             else:
#                 data.append(field.data)
        
#         print(data)           
#         try:
#         # Write form data to CSV file
#             with open("Dan_62-WTForms, Flask, Bootstrap and CSV - Coffee & WiFI/cafe-data.csv", "a", newline="", encoding="utf-8") as csv_file:
#                 writer = csv.writer(csv_file)
#                 #note moze i ovako ali ako ih imas previse bolje je for petljai data da se koristi
#                 # writer.writerow([
#                 #     form.cafe.data,
#                 #     form.location.data,
#                 #     form.open_time.data,
#                 #     form.closing_time.data,
#                 #     form.coffee_rating.data,
#                 #     form.wifi_rating.data,
#                 #     form.power_outlet_rating.data,
#                 #     ])
#                 writer.writerow(data)
#                 # csv_file.write("\n")
#                 print('Cafe added successfully!', 'success')
#             return redirect(url_for('cafes'))
#             # return render_template('cafes.html')
#         except Exception as e:
#             print('An error occurred while adding the cafe: {}'.format(str(e)), 'error')
#     return render_template('add.html', form=form)

@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open("Dan_62-WTForms, Flask, Bootstrap and CSV - Coffee & WiFI/cafe-data.csv", mode="a", encoding='utf-8') as csv_file:
            csv_file.write(f"\n{form.cafe.data},"
                           f"{form.location.data},"
                           f"{form.open_time.data.strftime('%H:%M')},"
                           f"{form.closing_time.data.strftime('%H:%M')},"
                           f"{form.coffee_rating.data},"
                           f"{form.wifi_rating.data},"
                           f"{form.power_outlet_rating.data}")
        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    try:
        with open('Dan_62-WTForms, Flask, Bootstrap and CSV - Coffee & WiFI/cafe-data.csv', newline='', encoding='utf-8') as csv_file:
            csv_data = csv.reader(csv_file, delimiter=',')
            list_of_rows = []
            for row in csv_data:
                list_of_rows.append(row)
            header = list_of_rows[0]
        return render_template('cafes.html', cafes=list_of_rows, header = header)
    except Exception as e:
        print('No cafes found!', 'info', e)
        return render_template('cafes.html', cafes=list_of_rows, header = header)


if __name__ == '__main__':
    app.run(debug=True)

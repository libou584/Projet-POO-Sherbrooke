from flask import Flask, render_template, request, redirect, url_for
from urllib.parse import quote as url_quote
from flask_wtf import FlaskForm
from wtforms import DateField, SubmitField
from wtforms.validators import DataRequired

from models.Application import Application
from models.Employee import Employee


app = Flask(__name__)
app.secret_key = 'iozufe4hf6FSVgt6erg-some-secret-key'

application = Application()
# employee = Employee(0, 'John', 'Doe', 'john.doe@udes.ca')
# application.login(employee)


class BookingForm(FlaskForm):
    date = DateField('Select a Date (format mm/dd/yyy)', format='%Y-%m-%d', validators=[DataRequired()])
    submit = SubmitField('Book Day Off')


@app.route('/', methods=['GET', 'POST'])
def index():
    if not application.user:
        return redirect(url_for('login'))
    form = BookingForm()
    if form.validate_on_submit():
        date = form.date.data.strftime('%Y-%m-%d')
        application.user.book_day(date)
        return redirect(url_for('index'))
    return render_template("pages/index.html", user=application.user, form=form, booked_days=application.user.booked_days)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        employee = Employee(0, first_name, last_name, email)
        application.login(employee)
        return redirect(url_for('index'))
    return render_template("pages/login.html")


@app.route('/logout')
def logout():
    application.logout()
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
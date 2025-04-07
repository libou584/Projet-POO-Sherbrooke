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


class BookingForm(FlaskForm):
    date = DateField('Select a Date (format mm/dd/yyy)', format = '%Y-%m-%d', validators = [DataRequired()])
    submit = SubmitField('Book Day Off')


@app.route('/', methods = ['GET', 'POST'])
def index():
    if not application.user:
        return redirect(url_for('login'))
    form = BookingForm()
    if form.validate_on_submit():
        date = form.date.data.strftime('%Y-%m-%d')
        res = application.repository_facade.add_booked_day(application.user.id, date)
        if res:
            application.day_off_approval_strategy.approve(application.user.id, date)
            application.user.refresh()
        return redirect(url_for('index'))
    return render_template("pages/index.html", user = application.user, form = form, booked_days = application.user.booked_days)


@app.route('/new_user', methods=['GET', 'POST'])
def new_user():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        age = request.form['age']
        role = request.form['role']
        if role == 'employee':
            user_id = application.repository_facade.new_employee(first_name, last_name, age)
        # elif role == 'hr':
        #     user_id = application.repository_facade.new_hr(first_name, last_name, age)
        application.login(application.repository_facade.get_user_by_id(user_id))
        return redirect(url_for('index'))
    return render_template("pages/new_user.html")


@app.route('/login', methods=['GET'])
@app.route('/login/<int:user_id>', methods=['GET'])
def login(user_id = None):
    if user_id is not None:
        user = application.repository_facade.get_user_by_id(user_id)
        application.login(user)
        return redirect(url_for('index'))
    return render_template("pages/login.html", users = application.repository_facade.get_all_users())


@app.route('/logout')
def logout():
    application.logout()
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
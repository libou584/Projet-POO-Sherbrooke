from flask import Flask, render_template, request, redirect, url_for
from urllib.parse import quote as url_quote
from flask_wtf import FlaskForm
from wtforms import DateField, SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__)
app.secret_key = 'iozufe4hf6FSVgt6erg-some-secret-key'

booked_days: list[str] = []

def sort_dates():
    booked_days.sort(key=lambda x: tuple(map(int, x.split('-'))))


class BookingForm(FlaskForm):
    date = DateField('Select a Date (format mm/dd/yyy)', format='%Y-%m-%d', validators=[DataRequired()])
    submit = SubmitField('Book Day Off')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = BookingForm()
    if form.validate_on_submit():
        date = form.date.data.strftime('%Y-%m-%d')
        if date not in booked_days:
            booked_days.append(form.date.data.strftime('%Y-%m-%d'))
            sort_dates()
            return redirect(url_for('index'))
    return render_template("pages/index.html", form=form, booked_days=booked_days)

if __name__ == '__main__':
    app.run(debug=True)

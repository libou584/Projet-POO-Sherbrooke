from flask import Flask, render_template, request, redirect, url_for
from urllib.parse import quote as url_quote
from flask_wtf import FlaskForm
from wtforms import DateField, SubmitField
from wtforms.validators import DataRequired

from models.Application import Application
from models.Users.Employee import Employee
from models.Users.Hr import Hr
from models.Observers.EmployeeNotificationObserver import EmployeeNotificationObserver
from models.Observers.HrNotificationObserver import HrNotificationObserver
from models.ReportGenerator.ReportFactoryProvider import ReportFactoryProvider
from models.DayOffApproval.ApprovalStrategyProvider import ApprovalStrategyProvider


app = Flask(__name__)
app.secret_key = 'iozufe4hf6FSVgt6erg-some-secret-key'

application = Application()
HrNotificationObserver(application)
EmployeeNotificationObserver(application)


class BookingForm(FlaskForm):
    date = DateField('Séléctionner un jour (format mm/dd/yyy)', format = '%Y-%m-%d', validators = [DataRequired()])
    submit = SubmitField('Demander')


@app.route('/', methods = ['GET'])
def index():
    if not application.user:
        return redirect(url_for('login'))
    if isinstance(application.user, Employee):
        return redirect(url_for('index_employee'))
    if isinstance(application.user, Hr):
        return redirect(url_for('index_hr'))
    return redirect(url_for('login'))


@app.route('/index_employee', methods = ['GET', 'POST'])
def index_employee():
    if not application.user:
        return redirect(url_for('login'))
    form = BookingForm()
    if form.validate_on_submit():
        date = form.date.data.strftime('%Y-%m-%d')
        res = application.repository_facade.add_booked_day(application.user.id, date)
        if res:
            application.approve_day_off(application.user.id, date)
            application.user.refresh()
        return redirect(url_for('index'))
    return render_template("pages/index_employee.html", user = application.user, form = form, booked_days = application.user.booked_days)


@app.route('/index_hr', methods=['GET', 'POST'])
def index_hr():
    if not isinstance(application.user, Hr):
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        strategy = request.form.get('strategy')
        application.day_off_approval_strategy = ApprovalStrategyProvider.get_approval_strategy(strategy)
    
    employees = application.repository_facade.get_all_employees()
    return render_template("pages/index_hr.html", user=application.user, employees=employees, current_strategy=application.day_off_approval_strategy)


@app.route('/hr_dashboard/<int:employee_id>', methods = ['GET'])
def hr_dashboard(employee_id):
    if not application.user:
        return redirect(url_for('login'))
    employee = application.repository_facade.get_user_by_id(employee_id)
    booked_days = application.repository_facade.get_booked_days_by_employee_id(employee_id)
    
    return render_template(
        "pages/hr_dashboard.html",
        booked_days = booked_days,
        user = application.user,
        employee = employee,
    )


@app.route('/approve_day_off/<int:employee_id>/<string:date>/<int:hr_id>', methods=['POST'])
def approve_day_off(employee_id: int, date: str, hr_id: int):
    if not isinstance(application.user, Hr):
        return redirect(url_for('login'))
    
    action = request.form.get('action')
    if action == 'approve':
        application.repository_facade.approve_day_off(employee_id, date, hr_id)
        application.notify_observers("employee", employee_id, f"Votre demande de jour de congé le {date} a été approuvée par {application.user.first_name} {application.user.last_name}.")
    elif action == 'reject':
        application.repository_facade.reject_day_off(employee_id, date, hr_id)
        application.notify_observers("employee", employee_id, f"Votre demande de jour de congé le {date} a été refusée par {application.user.first_name} {application.user.last_name}.")
    
    return redirect(url_for('hr_dashboard', employee_id = employee_id))


@app.route('/report/<string:report_type>/<int:employee_id>', methods=['GET'])
def report(report_type: str, employee_id: int):
    if not isinstance(application.user, Hr):
        return redirect(url_for('login'))
    
    ReportFactoryProvider.get_report_factory(report_type).create_report(employee_id)
    
    return redirect(url_for('hr_dashboard', employee_id = employee_id))


@app.route('/new_user', methods=['GET', 'POST'])
def new_user():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        age = request.form['age']
        role = request.form['role']
        if role == 'employee':
            user_id = application.repository_facade.new_employee(first_name, last_name, age)
        elif role == 'hr':
            user_id = application.repository_facade.new_hr(first_name, last_name, age)
        if user_id is not None:
            application.login(application.repository_facade.get_user_by_id(user_id))
            return redirect(url_for('index'))
    return render_template("pages/new_user.html")


@app.route('/login', methods = ['GET'])
@app.route('/login/<int:user_id>', methods = ['GET'])
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
    app.run(debug = True)
from booknetwork import app
from flask import render_template, redirect, flash, url_for
from flask_login import login_user, current_user, logout_user
from booknetwork.forms import RegistrationForm, LoginForm
from werkzeug.security import generate_password_hash, check_password_hash
from booknetwork.models import User
from booknetwork import db



@app.route('/')
def index():
    return render_template('index.html', title='Book Review Network Home')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        check_user = User.query.filter_by(email=form.email.data).first()
        if check_user and check_password_hash(check_user.password, form.password.data):
            login_user(check_user, remember=form.remember.data)
            flash('You have been logged in!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data)
        check_user = User.query.filter_by(username=form.username.data).first()
        check_email = User.query.filter_by(email=form.email.data).first()
        if check_email:
            flash(f'{check_email.email} has already been taken', 'warning')
            return redirect(url_for('register'))
        if check_user:
            flash(f'{check_user.username} has already been taken', 'warning')
            return redirect(url_for('register'))
        else:
            new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            flash(f'Account created for {form.username.data}!', 'success')
            return redirect(url_for('index'))
    return render_template('register.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/account')
def account():
    pass

@app.route('/search', methods=['POST'])
def search():
    pass

@app.route('/search_results')
def search_results():
    pass

    
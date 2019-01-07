from booknetwork import app
from flask import render_template, redirect, flash, url_for
from booknetwork.forms import RegistrationForm, LoginForm
from werkzeug.security import generate_password_hash, check_password_hash
from booknetwork.models import User
from booknetwork import db


@app.route('/')
def index():
    return render_template('index.html', title='Book Review Network Home')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@email.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('login'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data)
        new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('index'))
    return render_template('register.html', form=form)

    
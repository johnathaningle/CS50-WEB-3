from flask import Flask, render_template, url_for, flash, jsonify, request, session, redirect
from flask_login import user_logged_in, login_user, logout_user, current_user
from booknetwork import app, db, login_manager
from booknetwork.forms import LoginForm, RegisterForm
from booknetwork.models import User, Book, Review

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id) ##may conflict with sqlachemy or flask_sqlalchemy????

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    form = LoginForm()
    if form.validate_on_submit():
        uname = form.username.data
        passwd = form.password.data
        user = db.execute(f"SELECT * FROM users WHERE username = '{uname}' AND password='{passwd}'").fetchone()
        if user is not []:
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password')
            return redirect(url_for('login'))
    return render_template('login.html', form=form)

@app.route("/register")
def register():
    pass

@app.route("/dashboard")
def dashboard():
    return render_template('dashboard.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

    
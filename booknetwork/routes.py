from flask import Flask, render_template, url_for, flash, jsonify, request, session, redirect
from booknetwork import app, db
from booknetwork.forms import LoginForm, RegisterForm

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        uname = form.username.data
        passwd = form.password.data
        result = db.execute(f"SELECT * FROM users WHERE username = '{uname}' AND password='{passwd}'").fetchall()
        if result is not []:
            return redirect(url_for('dashboard'))
    return render_template('login.html', form=form)

@app.route("/register")
def register():
    pass

@app.route("/dashboard")
def dashboard():
    return render_template('dashboard.html')

    
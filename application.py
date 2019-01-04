import os
from flask import Flask, render_template, redirect
from forms import RegistrationForm, LoginForm
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'efs2@$$2f0-pl,<'

@app.route('/')
def index():
    return render_template('index.html', title='Book Review Network Home')

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', form=form)

@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)
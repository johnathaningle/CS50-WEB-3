from booknetwork import app, db, GOODREADS_KEY
from flask import render_template, redirect, flash, url_for, request, jsonify, session
from flask_login import login_user, current_user, logout_user
from booknetwork.forms import RegistrationForm, LoginForm
from werkzeug.security import generate_password_hash, check_password_hash
from booknetwork.models import User, Review
import requests, json



@app.route('/', methods=['GET','POST'])
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

@app.route('/search/<search_text>', methods=['GET','POST'])
def search(search_text):
    text = search_text
    print(f"Text: {text}")
    result = db.session.execute(
        "SELECT * FROM book WHERE (LOWER(isbn) LIKE LOWER(:text)) OR (LOWER(title) LIKE LOWER(:text)) OR (author LIKE LOWER(:text)) LIMIT 10",
        { "text": '%' + text + '%'} 
    ).fetchall()
    data = []
    for row in result:
        data.append(dict(row)) 
    print(data)
    return jsonify({ 'data': data })

@app.route('/book/<isbn>', methods=['GET', 'POST'])
def book_page(isbn):
    if request.method == 'GET':
        if current_user.is_authenticated:
            result = db.session.execute("SELECT * FROM book WHERE isbn='{}'".format(isbn)).fetchone()
            reviews = db.session.execute(f"SELECT * FROM review WHERE book_id={result[0]}")
            review_list = []
            if reviews:
                for i in reviews:
                    print(i)
                    review = {}
                    review["title"] = i[1]
                    review["rating"] = i[2]
                    review["content"] = i[3]
                    review_list.append(review)
            if result:
                review_data = requests.get(f"https://www.goodreads.com/book/review_counts.json?key={GOODREADS_KEY}&isbns={isbn}")
                if review_data:
                    review_dict = json.loads(review_data.text)
                    review_count = review_dict['books'][0]['ratings_count']
                    review_rating = review_dict['books'][0]['average_rating']
                else:
                    review_count = "N/A"
                    review_rating = "N/A"
                if review_list:
                    print("in review")
                    return render_template('book.html', title=result[2], isbn=result[1], author=result[3], year=result[4], rating=review_rating, reviews=review_list)
                return render_template('book.html', title=result[2], isbn=result[1], author=result[3], year=result[4], rating=review_rating)
            else:
                return redirect(url_for('index'))
        else:
            return redirect(url_for('index'))
    # if the review form was submitted
    else:
        if current_user.is_authenticated:
            result = db.session.execute("SELECT * FROM book WHERE isbn='{}'".format(isbn)).fetchone()
            title = request.form['title']
            rating = request.form['rating']
            content = request.form['content']
            r = Review(title=title, rating=rating, content=content, user_id=session["user_id"], book_id=result[0])
            db.session.add(r)
            db.session.commit()
            result = db.session.execute("SELECT * FROM book WHERE isbn='{}'".format(isbn)).fetchone()
            reviews = db.session.execute(f"SELECT * FROM review WHERE book_id={result[0]}")
            review_list = []
            if reviews:
                for i in reviews:
                    review = {}
                    review["title"] = i[1]
                    review["rating"] = i[2]
                    review["content"] = i[3]
                    review_list.append(review)
            print(review_list)
            if result:
                review_data = requests.get(f"https://www.goodreads.com/book/review_counts.json?key={GOODREADS_KEY}&isbns={isbn}")
                if review_data:
                    review_dict = json.loads(review_data.text)
                    review_count = review_dict['books'][0]['ratings_count']
                    review_rating = review_dict['books'][0]['average_rating']
                else:
                    review_count = "N/A"
                    review_rating = "N/A"
                if review_list:
                    print("in review")
                    flash('Review successfully added!', 'success')
                    return render_template('book.html', title=result[2], isbn=result[1], author=result[3], year=result[4], rating=review_rating, reviews=review_list)
                return render_template('book.html', title=result[2], isbn=result[1], author=result[3], year=result[4], rating=review_rating)
        # current user is not authenticated
        else:
            return redirect(url_for('index'))


    
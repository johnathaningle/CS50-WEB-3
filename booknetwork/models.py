import os
from booknetwork import app
from sqlalchemy import Column, ForeignKey, String, Integer
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)
    user_reviews = db.relationship("Review")
    
    def add_review(self, title):
        r = Review(title=title, user_id=self.id)
        db.session.add(r)
        db.session.commit()

class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.String)
    title = db.Column(db.String)
    author = db.Column(db.String)
    year_published = db.Column(db.Integer)

class Review(db.Model):
    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer)
    content = db.Column(db.String)
    user_id = db.Column(db.Integer, ForeignKey('users.id')) ##may need to change to user.id!
    book_id = db.Column(db.Integer, ForeignKey('books.id'))
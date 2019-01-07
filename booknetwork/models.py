from sqlalchemy import Column, ForeignKey, String, Integer
from sqlalchemy.orm import relationship
from flask_login import UserMixin
from booknetwork import db



class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String)
    user_reviews = db.relationship("Review", backref='author', lazy=True)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.String)
    title = db.Column(db.String)
    author = db.Column(db.String)
    year_published = db.Column(db.Integer)
    book_review = db.relationship('Review', backref='bookreview', lazy=True)

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    rating = db.Column(db.Integer)
    content = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) ##may need to change to user.id!
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
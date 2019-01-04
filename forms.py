from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email, ValidationError
from models import User
from app import db

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')

class RegisterForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()])
    
    def validate_username(self, username):
        user = db.execute(f"SELECT * FROM users WHERE username='{username}'").fetchone()
        if user is not None:
            raise ValidationError('Choose a different username')
    def validate_email(self, email):
        user = db.execute(f"SELECT * FROM users WHERE email='{email}'").fetchone()
        if user is not None:
            raise ValidationError('Choose a different email')
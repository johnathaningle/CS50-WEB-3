import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SECRET_KEY'] = 'efs2@$$2f0-pl,<'
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")

db =SQLAlchemy(app)


from booknetwork import routes

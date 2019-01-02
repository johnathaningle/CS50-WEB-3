from flask import Flask, render_template, url_for, flash, jsonify, request, session, redirect
from booknetwork import app, db

@app.route("/")
def index():
    return render_template('index.html')

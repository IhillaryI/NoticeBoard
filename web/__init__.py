#!/usr/bin/python3
from os import environ
from flask import (Flask, render_template, request, jsonify, session, url_for, g, flash, redirect)
from flask_cors import CORS
from models import storage
from models.user import User
from models.notice import Notice
import hashlib
from hashlib import md5
from sqlalchemy.exc import IntegrityError

def create_app():
    app = Flask(__name__)
    cors = CORS(app, resources={r"/*": {"origins": "*"}})
    app.config.from_mapping(
        SECRET_KEY='secret',
    )

    @app.errorhandler(404)
    def not_found(error):
        return render_template('404.html')

    @app.route('/', strict_slashes=False)
    def index():
        return render_template('index.html')

    @app.route('/login', strict_slashes=False, methods=["POST"])
    def login():
        ssession = storage.session()

        email = request.form['email']
        password = request.form['password']

        user = ssession.query(User).where(User.email == email).first()
        if user is None:
           error = "User doesn't exist"
           flash(error)
           return redirect(url_for("index"))
    
        password = md5(password.encode('utf-8')).hexdigest()

        if user.password != password:
            error = "Password Incorrect"
            flash(error)
            return redirect(url_for("index"))

        session['user_id'] = user.id

        return redirect(url_for("dashboard"))

    @app.route('/register', strict_slashes=False, methods=["POST"])
    def register():
        email = request.form["email"]
        password = request.form["password"]
        print(password)
    
        try:
            data = dict(request.form)
            user = User(**data)
            user.save()
            session["user_id"] = user.id
        except IntegrityError as e:
            error = "User already exists try another email"
            flash(error)
            return redirect(url_for("index"))

        return redirect(url_for("dashboard"))


    @app.route('/guest', strict_slashes=False, methods=["POST"])
    def guest():
        ssession = storage.session()
        user = ssession.query(User).where(User.email == request.form["email"]).first()

        session['user_id'] = user.id

        return redirect(url_for("dashboard"))

    @app.route('/dashboard', strict_slashes=False, methods=["GET"])
    def dashboard():
        user_id = session.get("user_id")
        print('user_id '*8, user_id)

        if user_id is None:
            return redirect(url_for("index"))

        return render_template("dash.html")
        

    @app.route('/logout', strict_slashes=False, methods=["GET"])
    def logout():
        session['user_id'] = None
        storage.close()
        return redirect(url_for("index"))
        

    return app

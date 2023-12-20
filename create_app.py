from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


db = SQLAlchemy()
bcrypt = Bcrypt()


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Kipo7as22nirem!@localhost/audiobooks'
    app.config['SECRET_KEY'] = 'uHGdGgMZt4a6yk!'

    db.init_app(app)
    bcrypt.init_app(app)

    return app, db, bcrypt

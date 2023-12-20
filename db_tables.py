from flask_login import UserMixin
from create_app import db


class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(10), nullable=False)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.TEXT, nullable=False)
    fullname = db.Column(db.TEXT, nullable=False)
    messages = db.relationship('Message', backref='user')


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    message = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f"Message {self.id} from User {self.user_id}: {self.message}"

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Transactions(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    date_of_transction = db.Column(db.DateTime, nullable=False)
    amount = db.Column(db.Float, nullable=False)
    details = db.Column(db.String, nullable=False)
    uuid = db.Column(db.String, nullable=False)
    user_uuid = db.Column(db.String, nullable=False)
    fraud = db.Column(db.Boolean, nullable=True)

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_uuid = db.Column(
        db.String,
        nullable=False,
        unique=True
    )
    email = db.Column(db.String, nullable=False)
    password_hash = db.Column(db.String, nullable=False)

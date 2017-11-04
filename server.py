import os
from uuid import uuid4

from flask import Flask, render_template, flash, request, redirect
from flask_login import LoginManager, login_required
from flask_sqlalchemy import SQLAlchemy
from supports.database import db, Transactions, User

from supports.crypto import verify, make_hash

app = Flask(__name__)

login_manager = LoginManager()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///main.db'

db.init_app(app)
login_manager.init_app(app)

# db = SQLAlchemy()
def create_app():
    db.init_app(app)
    return app


def find_user(email):
    user = User.query.filter_by(email=email).first()
    return user if user is not None else None


@app.route('/register', methods=['POST'])
def register():
    email = request.form.get('email')
    password = request.form.get('password')
    if find_user(email) is None:
        new_user = User(
            user_uuid=str(uuid4()),
            email=email,
            password_hash = make_hash(password))
        db.session.add(new_user)
        db.session.commit()
        return redirect('/dashboard')
    else:
        flash("Email is already registered.")


@login_manager.user_loader
def user_loader(email):
    return find_user(email)

@login_manager.request_loader
def request_loader(request):
    email = request.form.get('email')
    user = find_user(email)

    if user is None: return None

    user.is_authenticated = verify(
        request.form.get('password'), user.password_hash
    )

    return user


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = find_user(email)
        if user is not None and verify(password, user.password_hash):
            flask_login.login_user(user)
            return flask.redirect('/dashboard')

    flash('Incorrect username or password.')

@app.route('/dashboard', methods=['GET'])
@login_required
def dashboard():
    user = flask_login.current_user.uuid
    transactions = User.query.filter_by(user_uuid=user.uuid).all()
    return render_template('dashboard.html', transactions=transactions)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return flask.redirect('/')

@app.route('/api/addTransaction', methods=['POST'])
def add_transaction():
    data = request.get_json()
    new_transaction = Transactions(
        date_of_transaction=data.get('date_of_transaction')
        amount=data.get('amount')
        details=data.get('details')
        uuid=str(uuid4())
        user_uuid=data.get('user_uuid')
    )

    db.session.add(new_transaction)
    db.session.commit()

if __name__ == "__main__":
    app.run(
        host='0.0.0.0',
        port=4000,
    )

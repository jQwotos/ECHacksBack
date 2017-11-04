import json

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

# from supports.database import User

app = Flask(__name__)

db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///main.db'
# from supports.database import db

db.init_app(app)

class User(db.Model):
    user_uuid = db.Column(
        db.String,
        nullable=False,
        unique=True
    )
    email = db.Column(db.String, nullable=False)
    password_hash = db.Column(db.String, nullable=False)

@app.route('/product', methods=['POST'])
def createTransaction():
    if request.is_json:
    # fetch user and transaction from the request
        user = request.get_json()["user"]
        transaction = request.get_json()["transaction"]
        print(user)
        print(transaction)
        row = row(user=user, transaction=transaction) #prepare query statement

    curr_session = mysql.session #open database session
    try:
        curr_session.add(row) #add prepared statement to opened session
        curr_session.commit() #commit changes
    except:
        curr_session.rollback()
        curr_session.flush() # for resetting non-commited .add()

    userID = user.id #fetch last inserted id
    data = Products.query.filter_by(id=userId).first() #fetch our inserted product
    config.read('rating_db.conf')
    result = [data.name, data.rate] #prepare visual data
    return jsonify(session=result)
    return json.dumps({
        'status': 'Success!'
    })

if __name__ == "__main__":
    app.run()

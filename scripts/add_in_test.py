import requests

BASE_URL = 'http://127.0.0.1:4000'
INSERT_URL = '%s/api/addTransaction' % BASE_URL

user_uuid = '36fe18b8-9795-40ac-94e5-63a88c838b63'

def submit():
    data = {
        'date_of_transaction': 'Jul 2, 2018',
        'amount': '50',
        'user_uuid': user_uuid,
        'details': 'Winners Halifax, NS',
        'train': True
    }

    print(requests.post(INSERT_URL, json=data).content)

if __name__ == "__main__":
    submit()

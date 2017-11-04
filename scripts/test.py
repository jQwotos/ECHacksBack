import requests

BASE_URL = 'http://localhost:4000'
ADD_URL = '%s/api/addTransaction' % BASE_URL

data = {
    'date_of_transaction': 'Dec 31, 2018',
    'amount': '10.1',
    'details': 'Canadian Tire Ottawa, ON',
    'user_uuid': '33409f08-5089-4b8f-af60-02293e8caac1',
}

def send():
    return requests.post(ADD_URL, json=data)

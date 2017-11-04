import csv
import requests

user_uuid = '33409f08-5089-4b8f-af60-02293e8caac1'

def get_data():
    with open('test_cases.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        data = []
        for row in reader:
            data.append(row)
    return data

def submit(data):
    for point in data:
        data = {
            'date_of_transaction': point[0],
            'amount': point[1],
            'details': point[2],
            'user_uuid': user_uuid}
        print(requests.post('http://127.0.0.1:4000/api/addTransaction', json=data).content)

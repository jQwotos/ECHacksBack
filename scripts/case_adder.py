import csv
import requests

user_uuid = 'ce66622f-8c17-4d20-abad-f866809f4c90'

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

if __name__ == "__main__":
    submit(get_data())

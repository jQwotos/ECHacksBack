import requests

BASE_URL = 'http://127.0.0.1:4000'
INIT_PREDICT_URL = "%s/initPredict" % BASE_URL

def test_init_predict():
    data = {
        'user_uuid': 'ce66622f-8c17-4d20-abad-f866809f4c90'
    }

    r = requests.post(INIT_PREDICT_URL, json=data)
    print(r.content)

if __name__ == "__main__":
    test_init_predict()

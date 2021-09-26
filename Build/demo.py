from flask import Flask
from flask_healthz import healthz
import requests
import urllib3
from flask_healthz import HealthError
app = Flask(__name__)


RINO = ('https://api.coinbase.com/v2/prices/spot?currency=USD')

@app.route('/healthz/live', methods=['GET'])
def healthz_live():
    return 'ok\n'


@app.route('/healthz/ready', methods=['GET'])
def healthz_ready():

    try:
        requests.get(RINO).json()
    except Exception:
        raise HealthError("Can't connect to COINBASE")
    return 'ok\n'


def query_api(cur):
    try:

        API_URL = ('https://api.coinbase.com/v2/prices/spot?currency=' + cur )
        print(API_URL)
        data = requests.get(API_URL.format(cur)).json()
        print(data)
    except Exception as exc:
        print(exc)
        data = None
    return data

@app.route('/coinbase/<cur>')
def result(cur):
    resp = query_api(cur)
    try:
        text = str(resp["data"]["currency"]) + "-" +  str(resp["data"]["base"]) + "-" +  str(resp["data"]["amount"])
        text = resp
    except:
        text = "There was an error"
    return text




if __name__ == '__main__':
    app.run(debug=True)

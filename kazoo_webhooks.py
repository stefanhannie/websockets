from flask import Flask
from flask import request
from flask import json

app = Flask(__name__)

def parse_request(req):
    """
    Parses application/json request body data into a Python dictionary
    """
    return json.dumps(req.json)

@app.route('/')
def api_root():
    return 'Welcome guys'

@app.route('/test')
def test():
    return "hello this is a test"

@app.route('/github', methods=['POST', 'GET'])
def api_gh_message():
    payload = parse_request(request)
    if payload == 'null':
        return "Welcome to GitHub."
    else:
        if request.headers['Content-Type'] == 'application/json':
            get_info = json.dumps(request.json)
            print(get_info)
            return get_info

@app.route('/kazoo', methods=['POST'])
def api_kz_hook():
    payload = parse_request(request)
    print(payload)
    if request.headers['Content-Type'] == 'application/json':
        info = json.dumps(request.json)
        print(info)
        return info


if __name__ == '__main__':
    app.run(debug=True)




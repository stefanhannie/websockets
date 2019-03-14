from flask import Flask
from flask import request
from flask import json

app = Flask(__name__)


@app.route('/')
def api_root():
    return 'Welcome guys'

# @app.route('/github', methods=['POST'])
# def api_gh_message():
#     if request.headers['Content-Type'] == 'application/json':
#         get_info = json.dumps(request.json)
#         print(get_info)
#         return get_info


@app.route('/kazoo', methods=['POST'])
def api_kz_hook():
    if request.headers['Content-Type'] == 'application/json':
        info = json.dumps(request.json)
        print(info)
        return info


if __name__ == '__main__':
    app.run(debug=True)




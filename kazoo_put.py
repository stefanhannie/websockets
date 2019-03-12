import requests
import json as j

server = 'http://18.218.219.1'


def get_response():
    headers = {
        'Content-Type': 'application/json',
    }

    data = '{"data":{"credentials":"92b5841ef89f79c5b359226f24d194a4","account_name":"master"}}'

    _response = requests.put(server + ':8000/v2/user_auth', headers=headers, data=data)

    return _response


def get_auth_token():
    key = get_response()
    key = key.json()
    auth_token = key['auth_token']

    return auth_token


def get_acc_id():
    _key = get_response()
    _key = _key.json()
    y = _key['data']['account_id']

    return y


def get_socket_id():
    auth = get_auth_token()
    acc_id = get_acc_id()
    headers = {'X-Auth-Token': auth,
               }
    ids = requests.get(server + ':8000/v2/accounts/' + acc_id + '/websockets', headers=headers)

    return ids


def get_web_sockets():

    websockets = requests.get(server + ':8000/v2/websockets')

    return websockets


def create_account():
    auth = get_auth_token()
    headers = {
        'X-Auth-Token': auth,
        'Content-Type': 'application/json',
    }

    data = '{"data":{"name":"send_message"}}'

    new = requests.put(server + ':8000/v2/accounts', headers=headers, data=data)

    return new


def get_socket1_id():
    auth = get_auth_token()
    acc_id = get_acc_id()
    headers = {'X-Auth-Token': auth,
               }
    ids = requests.get(server + ':8000/v2/accounts/' + acc_id + '/websockets', headers=headers)

    return ids


def create_user():
    auth = get_auth_token()
    acc_id = get_acc_id()
    headers = {
        'X-Auth-Token': auth,
        'Content-Type': 'application/json',
    }

    data = '{"data":{"first_name":"Sarah", "last_name":"Brown"}}'

    # data = '{"data":{"first_name":' + f_name + ',"last_name":' + l_name + '}}'
    # data = j.dumps(data)

    new = requests.put(server + ':8000/v2/accounts/' + acc_id + '/users', headers=headers, data=data)

    return new


if __name__ == '__main__':

    get = create_user().text

    parsed = j.loads(get)

    # #print(parsed)
    print(j.dumps(parsed, indent=2, sort_keys=True))





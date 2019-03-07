import requests
import hashlib as h

server = 'http://18.218.219.1'
username = 'superadmin:somepassword'
user_md5 = h.md5(username.encode())


def get_user():
    headers = {
        'Content-Type': 'application/json',
    }

    data = '{"data":{"credentials":"92b5841ef89f79c5b359226f24d194a4","account_name":"master"}}'

    _response = requests.put(server + ':8000/v2/user_auth', headers=headers, data=data)

    return _response


def get_auth_token():
    key = get_user()
    key = key.json()
    auth_token = key['auth_token']

    return auth_token


def get_acc_id():
    _key = get_user()
    _key = _key.json()
    y = _key['data']['account_id']

    return y


def get_socket_id():
    auth = get_auth_token()
    acc_id = get_acc_id()
    headers = {'X-Auth-Token': auth

               }

    ids = requests.get(server + ':8000/v2/accounts/' + acc_id + '/websockets', headers=headers)

    return ids


# def get_accounts():
#     auth = get_auth_token()
#     acc_id = get_acc_id()
#     headers = {'X-Auth-Token': auth
#
#                }
#
#     ids = requests.get(server + ':8000/v2/accounts/' + acc_id + '/websockets', headers=headers)
#
#     return ids


if __name__ == '__main__':
    print(get_socket_id().json())

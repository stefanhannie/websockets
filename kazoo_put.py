import requests
import json as j

server = 'http://18.218.219.1'


# get more information on data from websocket by requesting for more details
def get_items(item_type, account_id, item_id):
    response = requests.get(
        f'{server}:8000/v2/accounts/{account_id}/{item_type}s/{item_id}', headers=get_headers())
    return response.json()


# custom headers for requests
def get_headers():
    return {
        'X-Auth-Token': get_auth_token(),
        'Content-Type': 'application/json',
    }


# Get the auth_token from crossbar
def get_response():

    data = '{"data":{"credentials":"92b5841ef89f79c5b359226f24d194a4","account_name":"master"}}'

    _response = requests.put(
        server + ':8000/v2/user_auth', headers=get_headers(), data=data)

    return _response


# Parse json file to get auth_token
def get_auth_token():
    key = get_response()
    key = key.json()
    auth_token = key['auth_token']

    return auth_token


# Parse json file for account id
def get_acc_id():
    _key = get_response()
    _key = _key.json()
    y = _key['data']['account_id']

    return y


# Request available socket ids
def get_socket_id():
    auth = get_auth_token()
    acc_id = get_acc_id()
    headers = {'X-Auth-Token': auth,
               }
    ids = requests.get(server + ':8000/v2/accounts/' +
                       acc_id + '/websockets', headers=headers)

    return ids


# Get all available websocket bindings
def get_web_sockets():

    wesockets = requests.get(server + ':8000/v2/websockets')

    return wesockets


# create an acoount
def create_account():
    auth = get_auth_token()
    headers = {
        'X-Auth-Token': auth,
        'Content-Type': 'application/json',
    }

    data = '{"data":{"name":"send_message"}}'

    new = requests.put(server + ':8000/v2/accounts',
                       headers=headers, data=data)

    return new


# create user
def create_user():
    auth = get_auth_token()
    acc_id = '43b5a09e9000fbfc9fd16b78c98b1057'
    headers = {
        'X-Auth-Token': auth,
        'Content-Type': 'application/json',
    }

    data = '{"data":{"first_name":"Win", "last_name":"Win"}}'

    new = requests.put(server + ':8000/v2/accounts/' + acc_id + '/users', headers=headers, data=data)

    return new



if __name__ == '__main__':

    get = get_socket_id().text

    parsed = j.loads(get)

    # #print(parsed)
    print(j.dumps(parsed, indent=2, sort_keys=True))

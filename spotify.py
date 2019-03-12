import requests
from requests.auth import HTTPBasicAuth

server = '18.218.219.1'

# r = requests.get('http://18.218.219.1/websockets')


p = requests.put('http://18.218.219.1:8000/v2/master', auth=HTTPBasicAuth('superadmin', 'somepassword'))

print(p)
if __name__ == '__main__':
    print('OK')




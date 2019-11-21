import requests
import json

#base_url = 'http://192.168.100.71:3000'
base_url = 'https://hockey-api.lappis.rocks'

class Api:
        
    def login(self):
        #TODO remove hardcoded username and password
        email = 'raspberry@email.com'
        password = '123456'
        obj = {'email': email, 'password': password}
        url = base_url + '/login'
        r = requests.post(url, data = obj)
        print('Credential approved!')
        json_obj = json.loads(r.text)
        return json_obj['auth_token']

    def debit(self, auth_token, public_id):
        obj = {'operation': {'value': -2, 'public_id': public_id[:-2] } }
        url = base_url + '/operations'
        header = {'Authorization': auth_token}
        r = requests.post(url, json = obj, headers = header)
        print(r.status_code, r.text)
        if r.status_code == 201:
            return True
        else:
            return False

from .utils import verify_phone, request_to_api
from json import dumps
from datetime import datetime
from .Exceptions import AuthException

class Services():

    url = ''
    api_key = ''


    def __init__(self, url, api_key):
        super().__init__()
        self.url = url
        self.api_key = api_key
        self.auth_key = self.get_auth_key(api_key)

    def get_auth_key(self, api_key):
        headers = {
            'Content-Type': 'application/json',
            'Token': self.api_key
        }
        url = self.url + '/session_login/'
        payload = {
            'attributes' : self.api_key,
        }
        r = request_to_api(url, "POST", headers, payload)
        if('auth_token' in r):
            self.auth_date = datetime.now()
            return r['auth_token']
        raise AuthException()


    def get_headers(self, ):
        headers = {
            'Content-Type': 'application/json',
            'Token': self.api_key,
            'Auth': self.auth_key
        }
        return headers
    
    def send_campaing(self, typ, service_id, webhook, template, name, attributes):
        headers = self.get_headers()
        url = self.url + '/create_campaing/'
        payload = {
            'attributes' : attributes,
            'type' : typ,
            'service_id' : service_id,
            'webhook' : webhook,
            'template' : template,
            'name' : name
        }
        r = request_to_api(url, "POST", headers, payload)
        return r

    def send_message(self, to, content, sender = ''):
        to = verify_phone(to)
        url = self.url + '/service/'
        headers = self.get_headers()
        payload = {
            'tel': to,
            'msj': content
        }
        r = request_to_api(url, "POST", headers, payload)
        return r
    

    def single_recharge(self, type_id,  phone):
        url = self.url + '/recharge/'
        headers = self.get_headers()
        payload = {
            'recharge_type_id': type_id,
            'phone': phone,
            'should_wait_time' : 5
        }
        r = request_to_api(url, "POST", headers, payload)
        return r
    
    def get_recharge_types(self,):
        url = self.url + '/recharge_types/'
        headers = self.get_headers()
        r = request_to_api(url, "GET", headers)
        return r
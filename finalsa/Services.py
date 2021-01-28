from .utils import verify_phone, request_to_api
from json import dumps
from datetime import datetime, timedelta
from .Exceptions import AuthException


class Services():

    url = ''
    api_key = ''

    def __init__(self, url, api_key):
        super().__init__()
        self.url = url
        self.api_key = api_key
        self.auth_key = ''
        self.auth_date = datetime.now()

    def get_auth_key(self, api_key):
        headers = {
            'Content-Type': 'application/json',
            'Token': self.api_key
        }
        url = self.url + '/session_login/'
        payload = {
            'attributes': self.api_key,
        }
        r = request_to_api(url, "POST", headers, payload)
        if('auth_token' in r):
            self.auth_date = datetime.now()
            return r['auth_token']
        raise AuthException()

    def get_headers(self, ):
        auth_date = self.auth_date + timedelta(hours = 23, minutes= 59)
        if(self.auth_key == '' or auth_date < datetime.now()):
            self.auth_key =  self.get_auth_key(self.api_key)
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
            'attributes': attributes,
            'type': typ,
            'service_id': service_id,
            'webhook': webhook,
            'template': template,
            'name': name
        }
        r = request_to_api(url, "POST", headers, payload)
        return r

    def call_service(self, service_id, payload):
        url = self.url + '/service/{}'.format(str(service_id))
        headers = self.get_headers()
        r = request_to_api(url, "POST", headers, payload)
        return r

    def send_sms(self, to, message):
        url = self.url + '/sms/'
        headers = self.get_headers()
        payload = {
            'to' : to,
            'message' : message
        }
        r = request_to_api(url, "POST", headers, payload)
        return r

    def send_call(self, payload):
        url = self.url + '/call/'
        headers = self.get_headers()
        r = request_to_api(url, "POST", headers, payload)
        return r

    def single_recharge(self, type_id,  phone, should_wait_time = 5, url = '', data = {} ):
        url = self.url + '/recharge/'
        headers = self.get_headers()
        payload = {
            'recharge_type_id': type_id,
            'phone': phone,
            'url' : url,
            'data' : data,
            'should_wait_time': should_wait_time,
        }
        r = request_to_api(url, "POST", headers, payload)
        return r

    def get_recharge_types(self,):
        url = self.url + '/recharge_types/'
        headers = self.get_headers()
        r = request_to_api(url, "GET", headers)
        return r

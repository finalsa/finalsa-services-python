import requests
from .utils import verify_phone
from json import dumps

class Services():

    url = ''
    api_key = ''

    def __init__(self, url, api_key):
        super().__init__()
        self.url = url
        self.api_key = api_key
    
    def send_campaing(self, typ, service_id, webhook, template, name, attributes):
        headers = {
            'Content-Type': 'application/json',
            'Token': self.api_key
        }
        url = self.url + '/create_campaing/'
        payload = {
            'attributes' : attributes,
            'type' : typ,
            'service_id' : service_id,
            'webhook' : webhook,
            'template' : template,
            'name' : name
        }
        response = requests.request(
            "POST",
            url,
            headers=headers,
            data=dumps(payload),
        )
        return response.json()

    def send_message(self, to, content, sender = ''):
        to = verify_phone(to)
        files = []
        url = self.url + '/service/'
        headers = {
            'Content-Type': 'application/json',
            'Token': self.api_key
        }
        payload = {
            'tel': to,
            'msj': content
        }
        try:
            response = requests.request(
                "POST",
                url,
                headers=headers,
                data=dumps(payload),
                files=files
            )
            return response.json()
        except Exception as e:
            print(e)
            return {}
    

    def single_recharge(self, type_id,  phone):
        files = []
        url = self.url + '/recharge/'
        headers = {
            'Content-Type': 'application/json',
            'Token': self.api_key
        }
        payload = {
            'recharge_type_id': type_id,
            'phone': phone,
            'should_wait_time' : 5
        }
        try:
            response = requests.request(
                "POST",
                url,
                headers=headers,
                data=dumps(payload),
                files=files
            )
            r  =  response.json()
            print(r)
            return r
        except Exception as e:
            print(e)
            return {}
    
    def get_recharge_types(self,):
        files = []
        url = self.url + '/recharge_types/'
        headers = {
            'Content-Type': 'application/json',
            'Token': self.api_key
        }
        payload = {
        }
        try:
            response = requests.request(
                "GET",
                url,
                headers=headers,
                data=dumps(payload),
                files=files
            )
            return response.json()
        except Exception as e:
            print(e)
            return []

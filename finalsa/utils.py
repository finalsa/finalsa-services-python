import requests
from json import dumps
from .Exceptions import ServicesApiException

def verify_phone(phone):
    res = ''
    if(len(phone) == 10):
        res += '+52' + phone
    return res


def call_service(url, headers, service_name, payload):
    _url = url + '/service/{}'.format(service_name)
    r = request_to_api(_url, "POST", headers, payload)
    return r

def request_to_api(url, method,  headers={}, params={}, files=[], timeout=3000, exception=ServicesApiException, debug=False):
    try:
        response = requests.request(
            method,
            url,
            headers=headers,
            data= dumps(params),
            files=files,
            timeout=timeout
        )
        d = response.json()
        return d
    except Exception as ex:
        if(debug):
            print(ex)
        raise exception()

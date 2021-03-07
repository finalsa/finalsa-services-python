class Webhook():
    url = ""
    id = ""
    time_to_wait = 2
    data = {}

    def __init__(self, url, id = '', data = {}, time_to_wait = 2):
        self.url = url
        self.id = id
        self.data = data

    def to_dict(self, ):
        return{
            'url' : self.url,
            'id' : self.id,
            'data': self.data
        }
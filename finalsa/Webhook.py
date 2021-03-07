class Webhook():
    url = ""
    id = ""
    data = {}

    def to_dict(self, ):
        return{
            'url' : self.url,
            'id' : self.id,
            'data': self.data
        }
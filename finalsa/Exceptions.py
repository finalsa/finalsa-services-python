class ServicesApiException(Exception):

    def __init__(self, message="Exepction calling services-api"):
        self.message = message
        super().__init__(self.message)


class AuthException(Exception):

    def __init__(self, message="Excepction calling auth-api"):
        self.message = message
        super().__init__(self.message)

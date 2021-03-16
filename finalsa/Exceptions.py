class ServicesApiException(Exception):

    def __init__(self, message="Exception calling services-api"):
        self.message = message
        super().__init__(self.message)


class AuthException(Exception):

    def __init__(self, message="Exception calling auth-api"):
        self.message = message
        super().__init__(self.message)


class ServiceException(Exception):

    def __init__(self, message="Exception calling auth-api"):
        self.message = "Service return an  Exception: " + message
        super().__init__(self.message)

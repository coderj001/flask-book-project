class BaseConfig:
    HOST = "0.0.0.0"
    PORT = 8080
    DEBUG = False


class Development(BaseConfig):
    PORT = 5100
    MONGODB_URL = "mongodb://mongodb/dev"
    DEBUG = True


class Testing(BaseConfig):
    MONGODB_URL = "mongodb://mongodb/test"


class Prod(BaseConfig):
    MONGODB_URL = "mongodb+srv://rj:lDkH8c6FC6lJjpqA@cluster0.xy5dn.mongodb.net/?retryWrites=true&w=majority"

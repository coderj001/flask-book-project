import os
from flask import Flask
from flask_restx import Api
from mongoengine import connect
from config import *
from v1.resources.routes import initialize_routes

env = os.environ.get('ENV', None) 
app = Flask(__name__)
config = globals()[env if env else 'Prod']
app.config.from_object(config)
connect('app', host="mongodb+srv://rj:lDkH8c6FC6lJjpqA@cluster0.xy5dn.mongodb.net/")
api = Api(app)

initialize_routes(api)

if __name__ == "__main__":
    app.run(host=config.HOST, port=config.PORT)

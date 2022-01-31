from flask import Flask 

from .main.routes import main
from .extensions import mongo

def create_app():
    app = Flask(__name__)
    
    app.config['MONGO_URI'] = 'mongodb+srv://admin:12345@cluster0.2rvh0.mongodb.net/mydb?retryWrites=true&w=majority'

    mongo.init_app(app)

    app.register_blueprint(main)

    return app
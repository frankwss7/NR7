from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
from flask_jwt_extended import JWTManager 
from flask_cors import CORS 
from config.config import Config 
 
db = SQLAlchemy() 
jwt = JWTManager() 
 
def create_app(): 
    app = Flask(__name__) 
    app.config.from_object(Config) 
    db.init_app(app) 
    jwt.init_app(app) 
    CORS(app) 
    return app 

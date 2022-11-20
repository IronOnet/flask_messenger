from flask import Flask 


def create_app(config_file): 
    app = Flask(__name__) 
    app.config.from_object(config_file) 

    from models.base import db 
    db.init_app(app) 

    # Import API blueprints here  



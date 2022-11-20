from datetime import datetime
from marshmallow import Schema, fields, pre_load 
from marshmallow import validate 

from flask_marshmallow import Marshmallow 
from passlib.apps import custom_app_context as password_context 

from models.base_resource import AddUpdateDelete
from models.base import db 




class User(db.Model, AddUpdateDelete): 
    id = db.Column(db.Integer, primary_key=True) 
    first_name = db.Column(db.String(50), nullable=False) 
    last_name = db.Column(db.String(50), nullable=False) 
    email = db.Column(db.String(50), nullable=False) 
    phone_number = db.Column(db.String(15), nullable=False) 
    address = db.Column(db.String(200), nullable=True) 
    last_login = db.Column(db.DateTime()) 
    created_on = db.Column(db.DateTime(), default=datetime.now) 
    updated_on = db.Column(db.DateTime(), default=datetime.now, onupdate=datetime.now) 

    def last_login(): 
        pass 



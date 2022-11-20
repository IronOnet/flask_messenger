from datetime import datetime

from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow

from models.base_resource import AddUpdateDelete
from models.users import User  
from models.base import db 



ma = Marshmallow() 

class Message(db.Model, AddUpdateDelete): 
    id = db.Column(db.Integer, primary_key=True) 
    content = db.Column(db.String(250), unique=True, nullable=False) 
    message_from = db.Column(db.Integer(), db.ForeignKey('users.id')) 
    message_to = db.Column(db.Integer(), db.ForeignKey('users.id')) 
    created_at = db.Column(db.DateTime(), default=datetime.now)


class GroupMessage(db.Model, AddUpdateDelete): 
    id = db.Column(db.Integer, primary_key=True) 
    content = db.Column(db.String(250), unique=True, nullable=False) 
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'))
    created_at = db.Column(db.DateTime(), default=datetime.now)
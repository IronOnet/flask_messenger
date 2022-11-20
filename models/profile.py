from datetime import datetime

 
from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow 

from models.base_resource import AddUpdateDelete
from models.base import db 

 

class Profile(db.Model, AddUpdateDelete): 
    id = db.Column(db.Integer(), primary_key=True, nullable=False)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'), nullable=False) 
    profile_bio = db.Column(db.Text(30), nullable=True)
    created_at = db.Column(db.DateTime(), default=datetime.now) 
    updated_at = db.Column(db.DateTime(), default=datetime.now, updatenow=datetime.now)


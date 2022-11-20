from datetime import date, datetime 

from flask_sqlalchemy import SQLAlchemy 

from base_resource import AddUpdateDelete 
from base import db



class Channel(db.Model, AddUpdateDelete): 
    id = db.Column(db.Integer(), primary_key=True)  
    channel_name = db.Column(db.Text(30), nullable=False)
    messages = db.relationship('GroupMessage', backref='channel') 
    members = db.relationship('User', backref='channel')  
    created_at = db.Column(db.DateTime(), default=datetime.now) 
    updated_at = db.Column(db.DateTime(), default=datetime.now ,updatenow=datetime.now)

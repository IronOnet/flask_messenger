from flask_marshmallow import Marshmallow 
from flask_sqlalchemy import SQLAlchemy 

from base import db 



class AddUpdateDelete(): 
    def add(self, resource): 
        db.session.add(resource) 
        return db.session.commit() 

    def update(self): 
        return db.session.commit() 

    def delete(self, resource): 
        db.session.delete(resource) 
        return db.session.commit() 

    
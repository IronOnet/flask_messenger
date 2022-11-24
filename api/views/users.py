from flask import Flask 
from flask_restful import abort, Api, fields, marshal_with, reqparse, Resource 
from pytz import utc 

from datetime import datetime 
from api.models.users import User as UserModel  

import api.status as status 


class UserManager: 
    last_id = 0 
    def __init__(self): 
        self.messages = {} 

    def insert_message(self, message): 
        self.__class__.last_id += 1 
        

user_fields = {

}
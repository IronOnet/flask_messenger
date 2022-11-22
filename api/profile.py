from datetime import datetime

from flask import Flask  
from flask_restful import abort, Api, fields,  marshal_with, reqparse, Resource 
from pytz import utc 

from models.profile import Profile as ProfileModel 
import status 

class ProfileManager(): 
    last_id = 0 
    def __init__(self):
        self.profiles = {}

    def insert_profile(self, profile):
        self.__class__.last_id += 1 
        profile.id = self.__class__.last_id 
        self.profiles[self.__class__.last_id] = profile 

    def get_profile(self, id):
        return self.profiles[id]

    def delete_profile(self, id): 
        del self.profiles[id] 


profile_fields = {
    'id': fields.Integer, 
    'uri': fields.Url('message_endpoint'),  
    'user_id': fields.Integer, 
    'profile_bio': fields.String, 
    'profile_picture': fields.String, 
    'created_at': fields.DateTime, 
    'updated_at': fields.DateTime
}

profile_manager = ProfileManager() 

class ProfileResource(Resource): 
    def abort_if_profile_doesnt_exist(self, id):
        if id not in profile_manager.profiles: 
            abort(
                status.HTTP_404_NOT_FOUND, 
                message=f"Message {id} doesn't exist"
            )
    
    @marshal_with(profile_fields) 
    def get(self, id): 
        self.abort_if_profile_doesnt_exist(id) 
        return profile_manager.get_profile(id) 

    def delete(self, id): 
        self.abort_if_profile_doesnt_exist(id) 
        profile_manager.delete_profile(id) 
        return '', status.HTTP_204_NO_CONTENT 

    def patch(self, id): 
        self.abort_if_profile_doesnt_exist(id) 
        profile = profile_manager.get_profile(id) 
        parser = reqparse.RequestParser() 
        parser.add_argument('profile_id', type=int) 
        parser.add_argument('profile_bio', type=str)  
        parser.add_argument('profile_picture', type=str)
        
        args = parser.parse_args() 
        
        if 'profile_id' in args: 
            profile.profile_id = args['profile_id'] 
        if 'profile_bio' in args: 
            profile.profile_bio = args['profile_bio'] 

        if 'profile_picture' in args: 
            profile.profile_picture = args['profile_picture']

        return profile 

class ProfileListResource(Resource): 
    @marshal_with(profile_fields) 
    def get(self): 
        return [v for v in profile_manager.profiles.values()]  

    @marshal_with(profile_fields) 
    def post(self): 
        parser = reqparse.RequestParser() 
        parser.add_argument('profile_bio', required=False, help='User profile bio') 
        parser.add_argument('profile_picture', required=False, help='User profile picture') 

        args = parser.parse_args() 
        profile = ProfileModel(
            profile_bio=args['profile_bio'], 
            profile_picture = args['profile_picture']
        )

        profile_manager.insert_profile(profile) 
        return profile, status.HTTP_201_CREATED

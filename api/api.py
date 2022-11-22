from flask import Flask 
from flask_restful import abort, Api, fields, marshal_with, reqparse, Resource 
from datetime import datetime
from api.channels import ChannelListResource, ChannelResource
from api.message import MessageListResource, MessageResource
from api.profile import ProfileListResource, ProfileResource 

from models.messages import Message, GroupMessage 
from models.channels import Channel 
from models.profile import Profile 
from models.users import User 


app = Flask(__name__) 
api = Api(app) 

# Add resources here and their routes 
api.add_resource(MessageListResource, '/api/messages') 
api.add_resource(MessageResource, 'api/message/<int:id>', endpoint='message_endpoint') 
api.add_resource(ProfileListResource, 'api/profiles') 
api.add_resource(ProfileResource, 'api/profile/<int:id>', endpoint='profile_endpoint')
api.add_resource(ChannelResource, '/api/channels') 
api.add_resource(ChannelListResource, 'api/channel/<int:id>', endpoint='channel_endpoint')


if __name__ == '__main__': 
    app.run(host='0.0.0.0', debug=True)
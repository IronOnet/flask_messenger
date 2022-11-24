from datetime import datetime 

from flask_restful import abort, fields, marshal_with, reqparse, Resource 
from pytz import utc 

from api.models.channels import Channel as ChannelModel  
from api.views.message import message_fields
from api.views.users import user_fields
import api.status as status 

class ChannelManager(): 
    last_id = 0 
    def __init__(self): 
        self.channels = {} 

    def insert_channel(self, channel): 
        self.__class__.last_id += 1 
        channel.id = self.__class__.last_id 
        self.channels[self.__class__.last_id] = channel 

    def get_channel(self, id): 
        return self.channels[id] 

    def delete_channel(self, id): 
        del self.channels[id] 

channel_fields = {
    'id': fields.Integer, 
    'uri': fields.Url('channel_endpoint'), 
    'channel_name': fields.String, 
    'messages': fields.List(fields.Nested(message_fields)),
    'members': fields.List(fields.Nested(user_fields))
}

channel_manager = ChannelManager() 

class ChannelResource(Resource): 
    def abort_if_channel_doesnt_exist(self, id): 
        if id not in channel_manager.channels: 
            abort(
                status.HTTP_404_NOT_FOUND, 
                message="Channel {0} doesn't exist".format(id)
            )

    @marshal_with(message_fields) 
    def get(self, id): 
        self.abort_if_channel_doesnt_exist(id) 
        return channel_manager.get_channel(id) 

    def delete(self, id): 
        self.abort_if_channel_doesnt_exist(id) 
        channel_manager.delete_channel(id) 
        return '', status.HTTP_204_NO_CONTENT 

    @marshal_with(channel_fields) 
    def patch(self, id): 
        self.abort_if_channel_doesnt_exist(id) 
        channel = channel_manager.get_channel(id) 
        parser = reqparse.RequestParser() 
        parser.add_argument('uri', type=str) 
        parser.add_argument('channel_name', type=str) 
        parser.add_argument('messages', type=list) 
        parser.add_argument('members', type=list) 
        args = parser.parse_args() 

        if 'uri' in args:
            channel.uri = args['channel'] 
        if 'channel_name' in args: 
            channel.name = args['channel_name'] 
        if 'messages' in args: 
            channel.messages = args['messages'] 
        if 'members' in args: 
            channel.members = args['members'] 
        return channel 

class ChannelListResource(Resource): 
    @marshal_with(channel_fields) 
    def get(self): 
        return [v for v in channel_manager.channels.values()] 

    @marshal_with(message_fields) 
    def post(self): 
        parser = reqparse.RequestParser() 
        parser.add_argument('channel_uri', type=str, required=False, help="Channel URI") 
        parser.add_argument('channel_name', type=str, required=True, help="Channel name cannot be empty") 
        parser.add_argument('messages', type=list, required=False, help="List of messages in this channel") 
        parser.add_argument('members', type=list, required=False, help="List of members in this channel") 
        args = parser.parse_args() 
        channel = ChannelModel(
            channel_name= args['channel_name'], 
            messages = args['messages'], 
            members = args['members'], 
        )
        channel_manager.insert_channel(channel) 
        return channel, status.HTTP_201_CREATED
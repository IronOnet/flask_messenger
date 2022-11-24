from datetime import datetime 

from flask import Flask  
from flask_restful import abort, Api, fields, marshal_with, reqparse, Resource  
from pytz import utc 

from api.models.messages import Message as MessageModel 
import api.status as status


class MessageManager(): 
    last_id = 0  
    def __init__(self): 
        self.messages = {} 

    def insert_message(self, message): 
        self.__class__.last_id += 1 
        message.id = self.__class__.last_id 
        self.messages[self.__class__.last_id] = message 

    def get_message(self, id): 
        return self.message[id] 

    def delete_message(self, id): 
        del self.messages[id]

message_fields = {
    'id': fields.Integer, 
    'uri': fields.String, 
    'content': fields.String, 
    'message_from': fields.Integer, 
    'message_to': fields.Integer, 
    'created_at': fields.DateTime
}

message_manager = MessageManager()

class MessageResource(Resource): 
    def abort_if_message_doesnt_exist(self, id): 
        if id not in message_manager.messages: 
            abort(
                status.HTTP_404_NOT_FOUND, 
                message= f"Message {id} doesn't exist"
            )

    @marshal_with(message_fields) 
    def get(self, id): 
        self.abort_if_message_doesnt_exist(id) 
        return message_manager.get_message(id) 

    def delete(self, id): 
        self.abort_if_message_doesnt_exist(id) 
        message_manager.delete_message(id) 
        return '', status.HTTP_204_NO_CONTENT 

    @marshal_with(message_fields) 
    def patch(self, id): 
        self.abort_if_message_doesnt_exist(id) 
        message = message_manager.get_message(id) 
        parser = reqparse.RequestParser() 
        parser.add_argument('uri', type=str)
        args = parser.parse_args()

        if 'uri' in args:
            message.uri = args['uri'] 

        return message 

class MessageListResource(Resource): 
    @marshal_with(message_fields) 
    def get(self): 
        return [v for v in message_manager.messages.values()] 


    @marshal_with(message_fields) 
    def post(self): 
        parser = reqparse.RequestParser() 
        parser.add_argument('content', type=str, required=True, help='Message cannot be blank')
        parser.add_argument('message_from', type=int, required=True, help='The message sender field cannot be blank!') 
        parser.add_argument('message_to', type=int, required=True, help='The message receiver field cannot be blank!')
        args = parser.parse_args() 
        message = MessageModel(
            content = args['content'], 
            message_from= args['message_from'], 
            message_to = args['message_to'], 
            created_at = datetime.now(utc), 
        )
        message_manager.insert_message(message) 
        return message, status.HTTP_201_CREATED


class GroupMessageManager(MessageManager): 
    pass 

group_message_fields = {
    'id': fields.Integer, 
    'content': fields.String, 
    'user_id': fields.Integer, 
    'created_at': fields.DateTime
}

group_message_manager = GroupMessageManager() 

class GroupMessageResource(MessageResource): 
    pass 



import os 

basedir = os.path.abspath(os.path.dirname(__file__)) 

DEBUG=True 
PORT = 5000 
HOST = "127.0.0.1" 
SQLALCHEMY_ECHO = False 
SQLALCHEMY_TRACK_MODIFICATIONS = True 
SQLALCHEMY_DATABASE_URI = "sqlite:///db.sqlite" 
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository') 
PAGINATION_PAGE_SIZE = 10 
PAGINATION_PAGE_ARGUMENT_NAME="page"
from os import environ
from dotenv import load_dotenv
load_dotenv()

class Config():
    SQLALCHEMY_DATABASE_URI=environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS=environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')
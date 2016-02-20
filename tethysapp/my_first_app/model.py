# Put your persistent store models in this filefrom sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Float
from sqlalchemy.orm import sessionmaker

from .app import MyFirstApp

# DB Engine, sessionmaker and base
engine = MyFirstApp.get_persistent_store_engine('stream_gage_db')
SessionMaker = sessionmaker(bind=engine)
Base = declarative_base()

class StreamGage(Base):
    '''
    Example SQLAlchemy DB Model
    '''
    __tablename__ = 'stream_gages'

    # Columns
    id = Column(Integer, primary_key=True)
    latitude = Column(Float)
    longitude = Column(Float)
    value = Column(Integer)

    def __init__(self, latitude, longitude, value):
        """
        Constructor for a gage
        """
        self.latitude = latitude
        self.longitude = longitude
        self.value = value